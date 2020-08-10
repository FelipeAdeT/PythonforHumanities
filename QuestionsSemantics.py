from Questions import *

Q1 = MultQuestion("Fill in the blanks:\n\nBasic data types for storing ___ values include _____. Basic data types for storing multiple values are called _____, and include _____.\n\na)multiple,strings, booleans, lists.\n\nb) single, strings, collections, dictionaries.\n\nc) single, dictionaries, collections, strings\n\nd) string, integers, dictionaries, collections")

E1=Solution("type(artists)\nsorted(artists)\nlen(artists)")

Q2 =MultQuestion("The following is what type of object?\n\ninput()\n\ninput() is a ________\n\na) function \n\n b) variable \n\nc) method \n\n d) string","a")

Q3 =MultQuestion("The following is what type of object?\n \n string.replace()\n\nstring.replace() is a type of ______ called a ________\n\na)function, method\n\nb)variable,method\n\nc)function,variable\n\nd)module,function\n\n","a")

E2 = Solution("file = open('Other_files/TheWalrusandtheCarpenter.txt','r')\nwalrus = file.read()\nprint(walrus)\nfile.close()\n\nYou can of course use other variable names, and could potentially combine the first two lines: walrus = open('Other_files/TheWalrusandtheCarpenter.txt','r').read()")

E3=Solution("walrus=open('Other_files/TheWalrusandtheCarpenter.txt','r')\nfor line in walrus:\n    print(line)")

Q4= MultQuestion("What were the necessary actions included above?\n\na) Open the file in read mode, write count to the file, (explicit) close the file.\n\nb) Open the file in write mode, convert count into a string, write count to file, (implicit) close file.\n\nc)Open the file in read mode, convert count into a string, write count to file, (implicit) close file.\n\nd) Open the file in write mode, write count to the file, (explicit) close the file.\n\n" , "b")

E4= Solution("import emoji as em\nemoji.emojize('Python is :thumbs_up:')")