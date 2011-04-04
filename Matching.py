###############################################################################
##	Description: FuzzyMatch.py takes two files with one keyword per line as	 ##
##				 command line arguments. It then creates a file with matches ##
##				 at least 75% similar. If more than one match occurs, it     ##
##				 picks the best match and outputs it to Match75.csv.		 ##
##																			 ##
##				 Note: Currently the two files are hardcoded in. Arguments	 ##
##					  will be implemented later.							 ##
##																			 ##
##				Current Limitations: Sometimes words that should be filtered ##
##									 out are left because of whitespace.     ##
##								Example: Zhejiang Yongtai Technology Co Ltd  ##
##								Ltd is removed first, then because Co ends   ##
##								the string without a space, it isn't removed.##
##								I am searching for a reason.				 ##
##																			 ##
##																			 ##
##	Author:		Mike Kusold													 ##
##	Created:	Apr 4th, 2011												 ##
##	Version:	1.0															 ##
##																			 ##
##							Modification Notes								 ##
##---------------------------------------------------------------------------##
##																			 ##
##																			 ##
##																			 ##
##																			 ##
##																			 ##
##																			 ##
##																			 ##
###############################################################################
import time
import csv
import difflib

###	Filters out common words in an attempt to get better results ###
def ignoredWords (word):
	filtered = word.lower()
	if "university" in filtered:
		filtered = filtered.replace("university", "")
	if "univ" in filtered:
		filtered = filtered.replace("univ", "")
	if "academy of sciences" in filtered:
		filtered = filtered.replace("academy of sciences", "")	
	if "pharmaceuticals" in filtered:
		filtered = filtered.replace("pharmaceuticals", "")
	if "pharmaceutical" in filtered:
		filtered = filtered.replace("pharmaceutical", "")
	if " ltd" in filtered:
		filtered = filtered.replace(" ltd", "")
	if " inst" in filtered:
		filtered = filtered.replace(" inst", "")
	if " of " in filtered:
		filtered = filtered.replace(" of ", "")
	if " co " in filtered:
		filtered = filtered.replace(" co ", "")
	if " inc" in filtered:
		filtered = filtered.replace(" inc", "")
	if "  " in filtered: #Two White Spaces
		filtered = filtered.replace("  ", " ")
	return filtered

### Takes in a list, then outputs a 2D list. array[Original, Filtered] ###
def create2DArray (list):
	array = []
	for item in list:
		clean = ignoredWords(item)
		array.append([item, clean])
	return array

	
### Begin MAIN function ###
#Measure execution time
t0 = time.time()

############INPUT FILENAME############
fileA = open("comm.names.txt", 'r')
try:
	setA = fileA.readlines()
finally:
	fileA.close()
	
fileB = open("acad.names.txt", 'r')
try:
		setB = fileB.readlines()
finally:	
		fileB.close()

#Put Set A and Set B into their own 2 dimmensional arrays. array[Original Word][Cleaned Up Word]
arrayA = create2DArray(setA)
arrayB = create2DArray(setB)

#Create clean list versions for use with difflib
cleanListA = []
for item in arrayA:
	cleanListA.append(item[1])

cleanListB = []
for item in arrayB:
	cleanListB.append(item[1])
	
############OUTPUT FILENAME############
fMatch75 = open("Match75.csv", 'w')
Match75 = csv.writer(fMatch75, dialect='excel')
try:
	Match75.writerow(['File A', 'File B', 'Clean File A', 'Clean File B', 'Filtered Ratio', 'Unfiltered Ratio', 'Average Ratio'])
	for item in cleanListA:
		match = difflib.get_close_matches(item, cleanListB, 1, 0.75)
		
		if len(match) > 0:
			filteredratio = difflib.SequenceMatcher(None, item, match[0]).ratio()
			found = 0
			for group in arrayB:
				if match[0] == group[1]:
					origB = group[0]
					found = found + 1
			for group in arrayA:
				if item == group[1]:
					origA = group[0]
					found = found + 2
			if found == 3:
				unfilteredratio = difflib.SequenceMatcher(None, origA, origB).ratio()
				averageratio = (filteredratio + unfilteredratio)/2
				row = [origA.rstrip(), origB.rstrip(), item.rstrip(), match[0].rstrip(), filteredratio, unfilteredratio, averageratio]
				Match75.writerow(row)
			#These Else Ifs are for debugging. If NULL is found anywhere in the CSV, then an error has occurred
			elif found == 2:
				row = [origA.rstrip(), "NULL", item.rstrip(), match[0].rstrip(), filteredratio, "NULL", "NULL"]
				Match75.writerow(row)
			elif found == 1:
				row = ["NULL", origB.rstrip(), item.rstrip(), match[0].rstrip(), filteredratio, "NULL", "NULL"]
				Match75.writerow(row)
			else:
				row = ["NULL", "NULL", item.rstrip(), match[0].rstrip(), filteredratio, "NULL", "NULL"]
				Match75.writerow(row)
			
finally:
	fMatch75.close()

	print (time.time() - t0, "seconds")