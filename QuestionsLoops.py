from Questions import *

Q1 = Solution("Your code might look something like:\n\ncount = 6\n\nwhile count > 0:\n    if count %2 ==0:\n        print('tick')\n    else:\n        print('tock')\n    count = count-1\nprint('Ring!')")

Q2 = Solution("from random import shuffle\ngame = ['duck', 'duck', 'duck', 'goose', 'duck']\n\nwhile game[0]=='duck':\n    print('safe')\n    shuffle(game)\n\nprint('Run!')")

Q3 = Solution("value = 0\nwhile True:\n    if value%2==0:\n        print(value)\n    if value ==20:\n        break\n    value= value+1")

Q4 = Solution("value = 0\n\nwhile value<=20:\n    value= value+1\n    if value%2==0:\n        print(value)\n")

Q5 = Solution("You could use any term to refer to the items in the list, as long as you keep them consistent, and preferably, easy to understand. I chose 'donut'.\n\nMonutsDonuts = ['Classic Chocolate','Strawberry','Maple-Bacon','Plain Glazed', 'Raspberry','Lemon Glaze']\n\nfor donut  in  MonutsDonuts:\n    if 'Glaze' in donut:\n        print(donut)")