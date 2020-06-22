from Questions import *

E1 = Solution("This solution must include a variable assignment. You can use any variable name for the list, though it is good practice to make it intelligible (maybe 'donuts', or 'flavors'). \nThen, open square brackets and include each string value. Separate each item with a comma, and remember to enclose strings in quotes. \n\ndonuts = ['plain-glazed', 'chocolate', 'strawberry sprinkle', 'lemon']")

E2 = Solution("donuts[0:3]\n\nRecall that indexing starts at position 0, and slicing goes up to, but not including, the final number in our range. Thus, list[0:3] gives item 1 (position 0), item 2 (position 1), item 3 (position 2), up to, but not including item 4.")

E3 = Solution("donuts[2] = 'strawberry shortcake'")

E4 = Solution("donuts2 = ['apple cider', 'boston cream', 'lemon', 'raspberry']\ndonuts.extend(donuts2)\nlen(donuts)\ndonuts.pop()\nprint(donuts)\ndonuts.remove('lemon')\ndonuts.append('raspberry')")

E5 = Solution("prices['chocolate sea salt']=2.00\nprices['boston cream']=2.00")