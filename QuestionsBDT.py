from Questions import *

Q1 = Solution("type(year_of_birth) outputs 'str' (a string). We enclosed the variable in quotes, so Python has interpreted them not as a number, but as text. This sometimes desirable, but will also prevent us from conducting mathematical operations on its numerical value.")

Q2 = MultQuestion("How can you recognize that the string has been transformed into an integer?\n\na) The characters are digits \n\nb) The characters are not surrounded by quotes \n\nc) The characters are surrounded by quotes \n\nd) The characters are surrounded by digits\n\n","b")

Q3 = MultQuestion("Can we operate on these numbers directly?\n\na) No, Python gives us an error because one of these is not a number. \n\nb) Yes, Python allows us to subtract strings.\n\nb) No, Python does not allow us to subtract numbers.\n\nd)None of the above.\n\n","a", right='Correct! We must be careful with data types', wrong='Are you sure? Be mindful of data types')

Q4 = MultQuestion("What is the correct approach for figuring out the artist's life span?\n\na) Subtract year_of_birth from year_of_death \n\nb) Convert the variables to strings, then subtract\n\nc)Convert the year_of_death to a number, then subtract\n\nd)None of the above.\n\n","c")

E1 = Solution("year_of_birth = int(year_of_birth)")

E2 = Solution("(x-y)**2/2")
E3 = Solution("lifespan = year_of_death - year_of_birth\nprint(lifespan)")