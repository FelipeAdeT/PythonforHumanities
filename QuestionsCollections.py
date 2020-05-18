from Questions import *

Q1 = Solution("This solution must include a variable assignment. You can use any variable name for the list, though it is good practice to make it intelligible (maybe 'donuts', or 'flavors'). \nThen, open square brackets and include each string value. Separate each item with a comma, and remember to enclose strings in quotes. \n\ndonuts = ['Plain Glaze', 'Classic Chocolate', 'Strawberry Sprinkle', 'Lemon Glaze']")

Q2 = Solution("donuts[0:3]\n\nRecall that indexing starts at position 0, and slicing goes up to, but not including, the final number in our range. Thus, list[0:3] gives item 1 (position 0), item 2 (position 1), item 3 (position 2), up to, but not including item 4.")

Q3 = Solution("donuts[2] = 'Strawberry Shortcake'")

Q4 = Solution("donuts2 = ['Apple Cider', 'Boston Cream', 'Lemon Glaze', 'Raspberry']\ndonuts.extend(donuts2)\nlen(donuts)\ndonuts.pop()\nprint(donuts)\ndonuts.remove('Lemon Glaze')\ndonuts.append('Raspberry')")

Q5 = Solution("for donut in donuts:\n    prices[donut]=''")