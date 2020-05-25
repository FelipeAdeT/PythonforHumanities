from Questions import *

Q1 = Solution("objects_table.set_index('objectid',inplace=True)")

Q2 = Solution("objects_table.loc[100,'title']")

Q3 = Solution("join2 = join1.merge(people,how='left', on='personid')")