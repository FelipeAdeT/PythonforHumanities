from Questions import *

E1 = Solution("""def liftoff(count):\n"Counts down from 0, and then prints 'lift off!'"\n    while count > 0:\n        print(str(count) +'!')\n        count = count - 1\n    print('lift off!')""")

E2 = Solution("print(a,b,c)\n\nLooking at the documentation, you will find that print actually accepts multiple texts, and separates them automatically with a space (you can use the sep parameter to change this behavior). This is sometimes desirable, sometimes not, which is why concatenating with + does not include spaces.")

E3 = Solution("""def liftoff(count=10):\n    while count > 0:\n        print(str(count) +"!")\n        count = count - 1\n    print("lift off!")""")

E4 = Solution("""def liftoff(count=10):\n    a=''\n    while count > 0:\n        a = a + ' '+ str(count) +'!'\n        count = count - 1\n    return (a + 'Lift off!')""")

E5= Solution("def distance (point1,point2):\n    xdistance = abs(point1[0]-point2[0])\n    ydistance = abs(point1[1]-point2[1])\n    return xdistance, ydistance\n\ndistancex, distancey = distance(point1,point2)")