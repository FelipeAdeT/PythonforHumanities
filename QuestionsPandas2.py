from Questions import *

Q1 = Solution("import pandas as pd\nobjects_table = pd.read_excel('Other_files/NGAData.xlsx', sheet_name= 'objects')")

Q2 = Solution("df['testcolumn'] = ''\ndf = df.drop('testcolumn',1)")

Q3 = Solution("join2 = join1.merge(people,how='left', on='personid')")