from Questions import *

E1 = Solution("people_table = pd.read_excel('Other_files/NGADataSample.xlsx', sheet_name='people')\npeople_table.head() # or people_table.tail() or people_table.columns\npeople_table.set_index('constituentid',inplace=True)")

E2 = Solution("people_table['preferreddisplayname']\n\npeople_table[['preferreddisplayname','constituenttype']]")

Q1 = MultQuestion("What type of containers were outputted by the two cells above? \n\na) A list (one-dimensional) and a dictionary (two-dimensional) \n\nb) A list (two-dimensional) and a DataFrame (one-dimensional)\n\nc) Two DataFrames (one-dimensional and two-dimensional) \n\nd) A Series (one-dimensional) and a DataFrame (two-dimensional)","d")

E3 = Solution("people2 = people_table[['preferreddisplayname','constituenttype']].copy()")

E4 = Solution("people_table[people_table['nationality']=='American']")

E5 = Solution("people_table[(people_table['nationality']=='American') & (people_table['constituenttype']=='corporate')]")

E6 = Solution("objects_table.loc[73098,'title']")

E7 = Solution("people_table.loc[people_table['artistofngaobject']==1,['preferreddisplayname','nationality']]")
