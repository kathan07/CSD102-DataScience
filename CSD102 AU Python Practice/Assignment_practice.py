import pandas as pd
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt


df = pd.read_excel (r'C:\Notes\Bank Aggregated Details.xlsx', sheet_name='Bank_AggregatedData')

#Q10
d2 = df.iloc[50:101,:]


#Q9
d3 = df.rename(columns = {"Festival Religion (H-Holiday,C-Closing, NH-Not Holoday)":"Fest_Rel"}, inplace = True)


#Q2
d4 = df.query("Weekday == 'Sunday'")


#Q3
d5 = df["Total amount Withdrawn"].sum()


#Q4
d6 = df[["Transaction Date","No Of Withdrawals","No Of XYZ Card Withdrawals","No Of Other Card Withdrawals","Total amount Withdrawn"]]


#Q6
new_df = df[["Weekday","Total amount Withdrawn"]]



#Q5
extra_df = df[["ATM Name","No Of XYZ Card Withdrawals","No Of Other Card Withdrawals"]]
extra_df.rename(columns = {'No Of XYZ Card Withdrawals':'XYZ'}, inplace = True)
extra_df.rename(columns = {'No Of Other Card Withdrawals':'Other'}, inplace = True)
d7 = extra_df.query('XYZ>Other')



#Q7
d_1 = df[["Weekday","Total amount Withdrawn"]]
d_2 = d_1.query("Weekday == 'Sunday'")
a = int(d_2["Total amount Withdrawn"].sum())
d_3 = d_1
d_4 = d_3.query("Weekday == 'Monday'")
b = int(d_4["Total amount Withdrawn"].sum())
d_5 = d_1
d_6 = d_5.query("Weekday == 'Tuesday'")
c = int(d_6["Total amount Withdrawn"].sum())
d_7 = d_1
d_8 = d_7.query("Weekday == 'Wednesday'")
d = int(d_8["Total amount Withdrawn"].sum())
d_9 = d_1
d_10 = d_1.query("Weekday == 'Thursday'")
e = int(d_10["Total amount Withdrawn"].sum())
d_11 = d_1
d_12 = d_1.query("Weekday == 'Friday'")
f = int(d_12["Total amount Withdrawn"].sum())
d_13 = d_1
d_14 = d_13.query("Weekday == 'Saturday'")
g = int(d_14["Total amount Withdrawn"].sum())
# x-coordinates of left sides of bars
x = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
 
# heights of bars
y = [a,b,c,d,e,f,g]
 
# labels for bars
tick_label = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
 
# plotting a bar chart
plt.bar(x, y, tick_label = tick_label,width = 0.7, color = ['red'])
 # naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 # function to show the plot
plt.show()


#Q8
a1 =df["No Of XYZ Card Withdrawals"]
a2 = df["No Of Other Card Withdrawals"]
 
plt.scatter(a1, a2, c ="pink",
            linewidths = 2,
            marker ="s",
            edgecolor ="green",
            s = 50)
 
# To show the plot
plt.show()


#Q1
d1 = df.sort_values("Total amount Withdrawn",ascending = False)
d2 = d1[["ATM Name","Total amount Withdrawn"]]




#                  End of Assignment




