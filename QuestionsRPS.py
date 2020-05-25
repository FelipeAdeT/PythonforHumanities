from Questions import *

Q1 = MultQuestion("I want to run a line of code and add a comment about what I am doing. Which of these would not work?\n\na) import spacy # here i am importing spacy\n\nb) #below I am importing Spacy \nimport spacy\n\nc) #here I import spacy import spacy \n\nd) All of the above should work.\n\n","c","Correct! Comments can be added with a hashtag after code or in a separate line.","Incorrect, the hashtag invalidates any code after it on the same line.")

Q2 = MultQuestion("Python interprets whitespace as part of the structure of the language. Which of the following are true?\n\na)Lines represent statements \n\nb)Lines indented at the same level form part of a block of code \n\nc) Extra whitespace within a line, and extra blank lines, are not interpreted by Python \n\nd) All of the above.\n\n", "d", "Correct! Whitespace is important in Python in all these ways.", "Incorrect. Python uses whitespace in all the ways above.")

Q3 = Solution("count = 10 \nwhile count > 0: \n    print(str(count) +"!") \n    count = count - 1 \nprint("lift off!"))

Q4= Solution("donuts = ['Plain-Glazed', 'Classic Chocolate']")

Q5=MultQuestion('Which of these statements assigns a variable to an object?\n\na) object = variable \n\nb) variable == object \n\nc) object==variable \n\nd) variable=object\n\n','d',"Correct! When assigning a variable to an object, the variable is on the left, followed by a single equals sign and then the object.","Try again. When assigning a variable to an object, the variable is on the left, followed by a single equals sign and then the object.")

Q6 =FillQuestion("The following is what type of object?\n\ninput()\n\n","input() is a ________\n\n","function")

Q7 =MultQuestion("The following is what type of object?\n \n string.replace()\n\nstring.replace() is a type of ______ called a ________\n\na)function, method\n\nb)variable,method\n\nc)function,variable\n\nd)module,function\n\n","a")