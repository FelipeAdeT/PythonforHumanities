from Questions import *

Q1 = MultQuestion("I want to run the line of code 'import space' and add a comment about what I am doing ('here i am importing a python module named spacy'). Which of these would *not* work?\n\na) import spacy # here i am importing a python module named spacy\n\nb) #below I am importing a python module named spacy \nimport spacy\n\nc) #here I import a python module named spacy import spacy \n\nd) All of the above should work.\n\n","c","Correct! Comments can be added with a hashtag after code or in a separate line.","Incorrect, the hashtag invalidates any code after it on the same line.")

Q2 = MultQuestion("Python interprets whitespace as part of the structure of the language. Which of the following are true?\n\na)Lines represent statements \n\nb)Lines indented at the same level form part of a block of code \n\nc) Extra whitespace within a line, and extra blank lines, are not interpreted by Python \n\nd) All of the above.\n\n", "d", "Correct! Whitespace is important in Python in all these ways.", "Incorrect. Python uses whitespace in all the ways above.")

E1 = Solution("count = 10 \nwhile count > 0: \n    print(str(count) +'!') \n    count = count - 1 \nprint('lift off!')")

E2= Solution("You could choose any name for this variable, although it is best to choose one that makes sense to the reader (we chose 'donuts', but you could also use 'flavors' or 'donutflavors', for instance. The variable should be assigned to a list object, and remember to surround strings with quotes.\n\ndonuts = ['Plain-Glazed', 'Maple Bacon', 'Classic Chocolate']")

Q3=MultQuestion('Which of these statements assigns a variable to an object?\n\na) object = variable \n\nb) variable == object \n\nc) object == variable \n\nd) variable = object\n\n','d',"Correct! When assigning a variable to an object, the variable is on the left, followed by a single equals sign and then the object.","Try again. When assigning a variable to an object, the variable is on the left, followed by a single equals sign and then the object.")

Q4 =MultQuestion("The following is what type of object?\n\ninput()\n\n","input() is a ________\n\na) function \n\n b) variable \n\nc) method \n\n d) string","a")

Q5 =MultQuestion("The following is what type of object?\n \n string.replace()\n\nstring.replace() is a type of ______ called a ________\n\na)function, method\n\nb)variable,method\n\nc)function,variable\n\nd)module,function\n\n","a")

E3 =Solution("arts = ['Painting','Architecture','Sculpture','Literature','Music','Performing','Film']\n\nprint(x)\n\n\nThe problem was that the variable x we were trying to print is not defined. Instead, if we wanted to print our 'arts' list, we should have included that in the print function. Alternatively, you could define a variable x to be printed by the print(x) statement.\nFor example:\n\nx= 'Frida Kahlo'\n\nprint(x).\n\n\nNote that x is not the best variable name.")