from Questions import *

Q1 = MultQuestion("What do you expect print(filehandle) to output?\n\na) The contents of our file.\n\nb) Something else!\n\n","b","Let's have a look.","Let's have a look.")

Q2 = Solution("walrus = open('Other_files/TheWalrusandtheCarpenter.txt','r')\nwalrustext = walrus.read()\nprint(walrustext)\n\nYou can of course use other variable names, and could potentially combine the first two lines: walrustext = open('Other_files/TheWalrusandtheCarpenter.txt','r').read()")

Q3= Solution("walrus=open('Other_files/TheWalrusandtheCarpenter.txt','r')\nfor line in walrus:\n    print(line)")

Q4= MultQuestion("What were the necessary actions included above?\n\na) Open the file in read mode, write count to the file, (explicit) close the file.\n\nb) Open the file in write mode, convert count into a string, write count to file, (implicit) close file.\n\nc)Open the file in read mode, convert count into a string, write count to file, (implicit) close file.\n\nd) Open the file in write mode, write count to the file, (explicit) close the file.\n\n" , "b")