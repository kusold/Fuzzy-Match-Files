import time

def ignoredWords (word):
	filtered = word.lower()
	if "university" in word:
		filtered = word.replace("university", "")
	if "univ" in word:
		filtered = word.replace("univ", "")
	if " of " in word:
		filtered = word.replace("of", "")
	if "pharmaceuticals" in word:
		filtered = word.replace("pharmaceuticals", "")
	if "pharmaceutical" in word:
		filtered = word.replace("pharmaceutical", "")
	if "academy of sciences" in word:
		filtered = word.replace("academy of sciences", "")	
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
	index = 0
	for item in cleanListA:
		
		match = difflib.get_close_matches(item, cleanListB, 1, 0.75)		
		if len(match) > 0:
			setBMatch = [re.match(*.match.*, i) for i in setB_LeftOver]
			ratio = difflib.SequenceMatcher(None, setA_LeftOver[i], setBMatch).ratio()
			#print (match[0])
			#print (item)
			#print (ratio)
			row = [item.rstrip(), match[0].rstrip(), ratio]
			Match75.writerow(row)
		index = index+1	
finally:
	fMatch75.close()

	print (time.time() - t0, "seconds")