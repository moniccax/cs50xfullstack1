import shutil #shell utilities
import os
import re

## REVIEW: re

#honeNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
#>>> print('Phone number found: ' + mo.group())

#Calling os.unlink(path) will delete the file at path .
#Calling os.rmdir(path) will delete the folder at path . This folder must be
#empty of any files or folders.
#Calling shutil.rmtree(path) will remove the folder at path , and all files
#and folders it contains will also be deleted.


#Using send2trash is much safer than Python’s regular delete functions,
#send2trash.send2trash('bacon.txt')


#To read the contents of a ZIP file, first you must create a ZipFile object
#newZip = zipfile.ZipFile('new.zip', 'w')
#newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)



#Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

listdir = os.listdir()
#for i in len(listdir):
print(listdir)

datePatternAmerican = re.compile(r"""^(.*?) ((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)

#res = [x for x in listdir if re.search(datePatternAmerican, x)]
#print(res)
#len = len(res)

for amerFilename in os.listdir('.'):
    res = datePatternAmerican.search(amerFilename)
        # Skip files without a date.
    if res == None:
        continue

    # Get the different parts of the filename.
    beforePart = res.group(1)
    monthPart  = res.group(2)
    dayPart    = res.group(4)
    yearPart   = res.group(6)
    afterPart  = res.group(8)

  # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing
#send2trash.send2trash('bacon.txt')

#datePattern = re.compile(r"""^(.*?) ((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
