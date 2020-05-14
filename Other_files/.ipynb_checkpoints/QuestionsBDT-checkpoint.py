from Questions import *

Q1 = MultQuestion("What is the variable's data type? (type the output of your code cell).","str")

Q2 = MultQuestion("What function should you use to transform the data into an integer? \n\na) int()\n\nb) str()\n\nc) string()\n\nd) fl()", "a")

Q3 = MultQuestion("How can you recognize that the string has been transformed into an integer?\n\na) The characters are digits \n\nb) The characters are not surrounded by quotes \n\nc) The characters are surrounded by quotes \n\nd) The characters are surrounded by digits","b")

Q4 = MultQuestion("Can we operate on these numbers directly?\n\na) No, these aren't numbers \n\nb) Yes, these are numbers.","a")

Q5 = MultQuestion("What is the correct approach for figuring out the artist's life span?\n\na) Subtract Artist_Birth from Artist_Death \n\nb) Convert the variables to strings, then subtract\n\nc)Convert the variables to integers, then subtract\n\nd)None of the above.","c")

Q6 = Solution("print( Artist + \" (\"+ Artist_Birth +\"-\"+Artist_Death +\")\")")