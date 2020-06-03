from Questions import *

E1 = Solution("artist = 'Frida Kahlo'\nlen(artist)>= 10")

E2= Solution("len(artist)>=10 and len(artist)<15")

E3= Solution("'Frida' in artist")

E4 =Solution("if len(artist)>=10:\n    print(artist+ ': '+ str(len(artist)) + ' letters')")
             
Q1 = MultQuestion("Say we run the following code. Which block will run and what will be the output?\n\nartist = 'Frida Kahlo\n\nif len(artist)==10:\n    print(artist+ ': 10 letters')\nelse:\n    print(artist+ ': '+ str(len(artist)) + ' letters')\n\na) The else block, 'Frida Kahlo: 10 letters'\n\nb) The if block, 'Frida Kahlo: 11 letters' \n\nc) The else block, 'artist: 10 letters' \n\nd) The else block, 'Frida Kahlo: 11 letters'\n\n","d")
             
E5 = Solution("if x<0:\n    print('x is less than 0')\nelif x<5:\n    print('x is less than 5')\nnelse:\n    print('x is greater than or equal to 5')")
             
E6 = Solution("if x<0:\n    print('x is less than 0')\nelif x<5:\n    print('x is less than 5')\nelif x<10:\n    print('x is less than 10')\nelse:\n    print('x is greater or equal to 10')")

             
Q2 = MultQuestion("For x = 4, what would the following program output?\n\nif x<0:\n    print('x is less than 0')\n    if x<5:\n        print('x is less than 5')\nif x<10:\n    print('x is less than 10')\nelse:\n    print('x is greater than 10')\n\na)x is less than 5\nx is less than 10\n\nb) x is less than 10\n\nb)x is less than 0\nx is less than 5\nx is less than 10\n\nd)x is less than 5\n\n",'b')
             
