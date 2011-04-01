import time
import csv
import difflib

def ignoredWords (word):
	filtered = word.lower()
	if "university" in filtered:
		filtered = filtered.replace("university", "")
	if "univ" in filtered:
		filtered = filtered.replace("univ", "")
	if " of " in filtered:
		filtered = filtered.replace("of", "")
	if "pharmaceuticals" in filtered:
		filtered = filtered.replace("pharmaceuticals", "")
	if "pharmaceutical" in filtered:
		filtered = filtered.replace("pharmaceutical", "")
	if "academy of sciences" in filtered:
		filtered = filtered.replace("academy of sciences", "")	
	return filtered
	
def create2DArray (list):
	array = []
	for item in list:
		clean = ignoredWords(item)
		array.append([item, clean])
	return array

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
	Match75.writerow(['File A', 'File B', 'Clean File A', 'Clean File B', 'Ratio'])
	for item in cleanListA:
		match = difflib.get_close_matches(item, cleanListB, 1, 0.75)
		if len(match) > 0:
			print (match[0])
			print (item)
			ratio = difflib.SequenceMatcher(None, item, match[0]).ratio()
			print (ratio)
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
				row = [origA.rstrip(), origB.rstrip(), item.rstrip(), match[0].rstrip(), ratio]
				Match75.writerow(row)
			elif found == 2:
				row = [origA.rstrip(), "NULL", item.rstrip(), match[0].rstrip(), ratio]
				Match75.writerow(row)
			elif found == 1:
				row = ["NULL", origB.rstrip(), item.rstrip(), match[0].rstrip(), ratio]
				Match75.writerow(row)
			else:
				row = ["NULL", "NULL", item.rstrip(), match[0].rstrip(), ratio]
				Match75.writerow(row)
			
finally:
	fMatch75.close()

	print (time.time() - t0, "seconds")