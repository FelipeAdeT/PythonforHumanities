from Questions import *

Q1 = Solution("artist = 'Frida Kahlo'\nlen(artist)>= 10")

Q2 = MultQuestion("Python is not making a qualitative argument about these artists' work. What is happening in the above comparisons?\n\na) Python is comparing the lengths of the strings\n\nb) Python is checking your computer's character tables, which place 'F' (in Frida) after 'D' but before 'P'\n\nc) Python is checking your computer's character tables, which place 'F' after 'P' but before 'D'\n\nd) None of the above\n\n", "b")

Q3= Solution("len(artist)>=10 and artist>'Diego Rivera'")

Q4= Solution("'Frida' in artist")

Q5 =Solution("if len(artist)>=10:\n    print(artist+ ': '+ str(len(artist)) + ' letters')")
             
Q6 = MultQuestion("Say we run this code. Which block will run and what will be the output?\n\nif len(artist)==10:\n    print(artist+ ': 10 letters')\nelse:\n    print(artist+ ': '+ str(len(artist)) + ' letters')\n\na) The else block, 'Frida Kahlo: 10 letters'\n\nb) The if block, 'Frida Kahlo: 11 letters' \n\nc) The else block, 'artist: 10 letters' \n\nd) The else block, 'Frida Kahlo: 11 letters'\n\n","d")
             
Q7 = Solution("if x<0:\n    print('x is less than 0')\nelif x<5:\n    print('x is less than 5')\nelif x<10:\n    print('x is less than 10')\nelse:\n    print('x is greater than 10')")
             
Q8 = MultQuestion("For x = -1, what would the following program's output?\n\nif x<5:\n    print('x is less than 5')\nelif x<0:\n    print('x is less than 0')\nelif x<10:\n    print('x is less than 10')\nelse:\n    print('x is greater than 10')\n\na)x is less than 5\n\nb) x is less than 10\n\nb)x is less than 5\nx is less than 10\n\nd)x is less than 0\n\n",'a')
             
Q9 = MultQuestion("For x = 4, what would the following program output?\n\nif x<0:\n    print('x is less than 0')\n    if x<5:\n        print('x is less than 5')\nif x<10:\n    print('x is less than 10')\nelse:\n    print('x is greater than 10')\n\na)x is less than 5\nx is less than 10\n\nb) x is less than 10\n\nb)x is less than 0\nx is less than 5\nx is less than 10\n\nd)x is less than 5\n\n",'b')
             
Q10= Solution("bandnumbers = []\nfor words in wordlist:\n    for token in words:\n        try:\n            bandnumbers.append(int(token))\n        except:\n            pass")