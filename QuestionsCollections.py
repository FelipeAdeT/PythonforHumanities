from Questions import *

Q1 = Solution("This solution must include a variable assignment. You can use any variable name for the list, though it is good practice to make it intelligible (maybe 'donuts', or 'flavors'). \nThen, open square brackets and include each string value. Separate each item with a comma, and remember to enclose strings in quotes. \n\ndonuts = ['Plain Glaze', 'Classic Chocolate', 'Strawberry Sprinkle', 'Lemon Glaze']")

Q2 = Solution("donuts[0:3]\n\nRecall that indexing starts at position 0, and slicing goes up to, but not including, the final number in our range. Thus, list[0:3] gives item 1 (position 0), item 2 (position 1), item 3 (position 2), up to, but not including item 4.")

Q3 = Solution("donuts[2] = 'Strawberry Shortcake'")

Q4 = Solution("donuts2 = ['Apple Cider', 'Boston Cream', 'Lemon Glaze', 'Raspberry']\ndonuts.extend(donuts2)\nlen(donuts)\ndonuts.pop()\nprint(donuts)\ndonuts.remove('Lemon Glaze')\ndonuts.append('Raspberry')")

Q5 = MultQuestion("Which slice would you use?\n\na) artist[0,6] \n\nb) artist[0:6] \n\nc) artist[0:7] \n\nd) artist[1:6] \n\n","c")

Q6 = MultQuestion("In which two ways could we extract the artist's last name?\n\na) print(artist[6]) or print(artist[6:]) \n\nb) print(artist[6:11]) or print(artist[6]) \n\nc) print(artist[6:10]) or print(artist[6:]) \n\nd) print(artist[6:11]) or print(artist[6:]) \n\n","d")

Q7 = Solution("""artists=artists.replace('_',' ')\nartists=artists.replace('0','o')\nartists=artists.title()\nartists=artists.split(',')\n\nThis could also be done on the same line: \nartists= artists.replace('_',' ').replace('0','o').title().split(',') """)