from pandas import DataFrame
import numpy as np
# Making dataframe
d1 = DataFrame([['AU2020168', 'Nensi Sandeepbhai Mungra','Integrated MS'],
['AU2140218','Dharman Hirenkumar Popat','BTech in Mech Engineering'],
['AU2140219','Aayush Ashish Sheth','BTech in Mech Engineering'],
['AU2120105','Meyyappan S.l','BA (Hons)'],
['AU1920151','Oem Trivedi','BS (Hons)']]
,columns=["Enr_no","Std_name","Programme"])
#Renaming column name
d2 = d1.rename(columns = {'Enr_no':'EnrNo'}, inplace = True)
#Display last three record
d3 = d1.iloc[1:4,:]
# Filter Rows using DataFrame.query()
d4 = d1.query("Programme == 'Integrated MS'")
#Display total no. of student
d5 = d1.EnrNo.count()
# records in the acsending order of student name
d6 = d1.sort_values("Std_name")
# Displaying two random columns
d7 = d1[["Programme","Std_name"]] 
# index change
''' d1.index = ['AU2020168', 'AU2140218', 'AU2140219', 'AU2120105','AU1920151']'''
#Inserting column named Email
d1.insert(3,"Email",["1904@gmail.com","1203@gmail.com","1903@gmail.com","1232@gmail.com","1443@gmail.com"])
'''By d['Email']=" " it can be done '''
# Replace values of email column with NaN
d1["Email"] = np.NaN
# Replace email id. of first student with "nensi.m@ahduni.edu.in"
d1['Email'] = ["nensi.m@ahduni.edu.in",np.nan,np.nan,np.nan,np.nan]
#Change value of email to "dharman.p@ahduni.edu.in" where Enr no. = "AU2140218"
d1.loc[(d1.EnrNo=="AU2140218"),'Email'] = "dharman.p@ahduni.edu.in"
# Insert 3 columns with marks
d1.insert(4,"CSD102",[44,34,43,35,23])
d1.insert(5,"CSE101",[34,37,23,39,43])
d1.insert(6,"MAT105",[46,37,36,41,39])
# Add colunmn total as addition of CSD102,CSE101,MAT105 for each column
d1['Total'] = d1['CSD102'] + d1["CSE101"] + d1["MAT105"]
#Find percentage of each student
d1['percentage'] = d1["Total"]/1.5
# Round off the percentages to zero decimal
d1["percentage"] = round(d1["percentage"],0)
# Disply name of student who got higest percentage 
#By logic
'''d1.sort_values("percentage", ascending = False)
d8 = d1.iloc[0:1]'''# prints all columns

'''d9 = d1[d1.percentage == d1.percentage.max()]'''# prints all columns
'''d10 = d1[d1.percentage == d1.percentage.max()].Std_name'''# prints only name
# drop multiple columns
d11 = d1.drop(["Email","Programme"], axis = 1)
# VVIP Grade Question
d1.loc[(d1.percentage>=80),'grade'] = 'A'
d1['grade'] = np.where((d1['percentage']<80) & (d1['percentage']>=60),'B',d1['grade'])
d1['grade'] = np.where((d1['percentage']<60) & (d1['percentage']>=40),'C',d1['grade'])
d1['grade'] = np.where((d1['percentage']<40),'D',d1['grade'])

# Delete rows were CSD102 marks is less than 35 or CSE101 marks less than 30
d12 = d1[(d1['CSD102']<35)|(d1['CSE101']<30)].index
d1.drop(d12,inplace=True)
print(d1)



 

