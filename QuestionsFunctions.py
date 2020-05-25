from Questions import *

Q1 = Solution("""def liftoff(count):\n    while count > 0:\n        print(str(count) +"!")\n        count = count - 1\n    print("lift off!")""")

Q2 = Solution("Looking at the documentation, you will find that print actually accepts multiple texts, and separates them automatically with a space (you can use the sep parameter to change this behavior). This is sometimes desirable, sometimes not, which is why concatenating does not include spaces.\n\nprint(a,b,c)")

Q3 = Solution("""def liftoff(count=10):\n    while count > 0:\n        print(str(count) +"!")\n        count = count - 1\n    print("lift off!")""")

Q4 = Solution("""def liftoff(count=10):\n    a=''\n    while count > 0:\n        a = a + '\n'+ str(count) +'!'\n        count = count - 1\n    return (a + 'Lift off!')""")