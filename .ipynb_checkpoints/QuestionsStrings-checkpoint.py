from Questions import *

E1 = Solution("a = \"Scarlett O'Hara\", a =\"Scarlett O\\'Hara\" or a ='Scarlett O\\'Hara'\n\nb = '\"The time has come,\" the walrus said, \"to talk of many things\"'\n\nc)'''\"But wait a bit,\" the Oysters cried,\n\"Before we have our chat;\nFor some of us are out of breath,\nAnd all of us are fat!\" '''\n\n(Other solutions may be possible.)")

E2 = Solution("print(artist + \" (\"+ str(year_of_birth) +\"-\"+str(year_of_death) +\")\")")

E3 = Solution("artist[1]\n\nOutput: 'r'")

E4 = Solution("firstinitial = artist[_]\nlastinitial = artist[_]\n\nprint(firstinitial + '.' + lastinitial + '.')")

E5 = Solution("artist[0:7]")

Q6 = MultQuestion("In which two ways could we extract the artist's last name?\n\na) artist[6] or artist[6:] \n\nb) artist[6:11] or artist[6] \n\nc) artist[6:10] or artist[6:] \n\nd) artist[6:11] or artist[6:] \n\n","d")

E7 = Solution("""artists=artists.replace('_',' ')\nartists=artists.replace('0','o')\nartists=artists.title()\nartists=artists.split(',')\n\n We could also apply multiple methods in one line of code. For instance: \nartists= artists.replace('_',' ').replace('0','o').title().split(',') """)