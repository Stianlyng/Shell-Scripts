from os import listdir
from os.path import isfile, join


filepath = "/Users/macbook-air/Downloads/pybook"
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
count = 0
txt = ""
for i in onlyfiles:
    if i == ".DS_Store":
        continue
    else:
        txt += "### " + str(i) + "\n"

        with open(str(filepath) + "/" +str(i)) as file_object:
            content = file_object.read()   
        #print("´´´python")
        txt += "```python \n"
        #print(str(content))
        txt += str(content) + "\n"
        #print("´´´")
        txt += "``` \n---\n\n"

        #print("######\n\n") 
        

        count += 1

myText = open(r'/Users/macbook-air/Desktop/file name.txt','w')
myText.write(txt)
myText.close()
#print(txt)
print(count)    