from Questions import *

E1 = Solution("import pandas as pd\nobjects = pd.read_excel('Other_files/NGADataSample.xlsx', sheet_name= 'objects')")

E2 = Solution("objects['testcolumn'] = ''\nobjects = objects.drop(columns ='testcolumn')")

E3 = Solution("ghettoes.melt(id_vars = ['GhettoID','GhettoName','Longitude','Latitude'], value_vars = ['UnspecE','UnknownE','UncertE','TyphusE','TyphoidE','TuberE','no_E','DysenteryE'], var_name ='Epidemic', value_name = 'EpidemicYN')")
E4 = Solution("join2 = join1.merge(people,how='left', on='constituentid')")

E5 = Solution("objects2 = pd.read_excel('Other_files/NGADataSample.xlsx',sheet_name='moreobjects')\n\nobjects = objects.append(objects2)\n\n\n or: \n\n\nobjects2 = pd.read_excel('Other_files/NGADataSample.xlsx',sheet_name='moreobjects')\n\ndflist=[objects,objects2]\n\n objects = pd.concat(dflist)")