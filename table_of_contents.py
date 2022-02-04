# Create a table of content based on headings (##) in markdownfile

# Copy the title of the file and the script will find the correct note and generate a table
# after a tiny second you can again press cmd + V or press paste and the table will get pasted 

import os
import re
import pyperclip

fileName = pyperclip.paste() + '.md'
searchFolder = '/Users/macbook-air/notes-vault/'  # spesify the folderlocation

def find_files(filename, search_path):
   result = ""

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result += os.path.join(root, filename)
   return result


filePath = find_files(fileName,searchFolder)


# Leser filen
with open(filePath) as file_object:
   content = file_object.read()


# Removes all the text between the ``` character - Codeblocks in particular
regex = r"```.*?```"
txt = str(content)
txt = re.sub(regex, '', txt, 0, re.DOTALL)

removeComma = txt.replace(",",";-;")
cleanTitles = removeComma.replace("\n",",")
cleanTitlesList = cleanTitles.split(",")

finishedList = []
for i in cleanTitlesList:
    noComma= i.replace(";-;", ",")
    finishedList.append(noComma)


tab = "\t"
print("- [[" + fileName + "]]")

fullTxt = "- [[" + fileName + "]]\n"

for i in finishedList:
    if i[:2] == "# ":
        fullTxt += (tab * 0) + "- [[" + fileName + '#' + i[2:] + '|' + i[2:] + "]]\n"

    if i[:3] == "## ":
        fullTxt += (tab * 1) + "- [[" + fileName + '#' + i[3:] + '|' + i[3:] + "]]\n"

    if i[:4] == "### ":
        fullTxt += (tab * 2) + "- [[" + fileName + '#' + i[4:] + '|' + i[4:] + "]]\n"

    if i[:5] == "#### ":
        fullTxt += (tab * 3) + "- [[" + fileName + '#' + i[5:] + '|' + i[5:] + "]]\n"

    if i[:6] == "##### ":
        fullTxt += (tab * 4) + "- [[" + fileName + '#' + i[6:] + '|' + i[6:] + "]]\n"

    if i[:7] == "###### ":
        fullTxt += (tab * 5) + "- [[" + fileName + '#' + i[7:] + '|' + i[7:] + "]]\n"


pyperclip.copy(fullTxt)