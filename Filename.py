filename = input("enter the filename")
ext = filename.split('.')

def checkKey(dict,key)
if key in dict:
   print("extension of file is:" , dict[key])
else:
   print("no such file exists!")

dict = { "py":"python , "txt":"text" , "zip":"zipfile")

key = ext[1]
checkKey(dict, key)
