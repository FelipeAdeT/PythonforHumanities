from Questions import *

Q1 = Solution("""def liftoff(count):\n    while count > 0:\n        print(str(count) +"!")\n        count = count - 1\n    print("lift off!")""")

Q2 = MultQuestion("How can you resolve the space issue with print?\n\na) By including the 'sep' keyword with a value\n\nb) By including the 'end' keyword with a value\n\nc) By including the 'file'keyword with a value\n\nd) None of the above\n\n","a")

Q3 = Solution("""def liftoff(count=10):\n    while count > 0:\n        print(str(count) +"!")\n        count = count - 1\n    print("lift off!")""")

Q4 = Solution("""def liftoff(count=10):\n    a=''\n    while count > 0:\n        a = a + str(count) +'!'\n        count = count - 1\n    return (a + 'Lift off!')""")