# FuzzyMatch.py
## Description:
FuzzyMatch.py takes two files with one keyword per line as command line arguments. It then creates a file with matches at least 75% similar. If more than one match occurs, it picks the best match and outputs it to Match75.csv. 

### Note:
Currently the two files are hardcoded in. Arguments will be implemented later.                            
                                                                         
## Current Limitations:
Sometimes words that should be filtered out are left because of whitespace.

### Example:
`Zhejiang Yongtai Technology Co Ltd`

`Ltd` is removed first, then because `Co` ends the string without a space, it isn't removed. I am searching for a reason.


## Author
Author:   Mike Kusold

Created:  Apr 4th, 2011

Version:  1.0