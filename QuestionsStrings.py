from Questions import *

Q1 = Solution("a = \"Scarlett O'Hara\", a =\"Scarlett O\\'Hara\" or a ='Scarlett O\\'Hara'\n\nb = '\"The time has come,\" the walrus said, \"to talk of many things\"'\n\nc)'''\"But wait a bit,\" the Oysters cried,\n\"Before we have our chat;\nFor some of us are out of breath,\nAnd all of us are fat!\" '''\n\n(Other solutions may be possible.)")

Q2 = Solution("print(artist + \" (\"+ str(year_of_birth) +\"-\"+str(year_of_death) +\")\")")

Q3 = Solution("artist[1]")

Q4 = MultQuestion("At what positions were the artist's first and last initials, respectively?\n\na) 1,6 \n\nb) 0,6 \n\nc) 0,5 \n\nd) 1,7 \n\n","b")

Q5 = MultQuestion("Which slice would you use?\n\na) artist[0,6] \n\nb) artist[0:6] \n\nc) artist[0:7] \n\nd) artist[1:6] \n\n","c")

Q6 = MultQuestion("In which two ways could we extract the artist's last name?\n\na) artist[6] or artist[6:] \n\nb) artist[6:11] or artist[6] \n\nc) artist[6:10] or artist[6:] \n\nd) artist[6:11] or artist[6:] \n\n","d")

Q7 = Solution("""artists=artists.replace('_',' ')\nartists=artists.replace('0','o')\nartists=artists.title()\nartists=artists.split(',')\n\nThis could also be done on the same line: \nartists= artists.replace('_',' ').replace('0','o').title().split(',') """)