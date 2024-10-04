import numpy as np
import pandas as pd
import random as rand
import matplotlib.pyplot as plt


Std_name=['Std1','Std2','Std3','Std4','Std5','Std6','Std7','Std8','Std9','Std10']
Subject_name=['Sub1','Sub2','Sub3','Sub4','Sub5']

Name=[]
Subject=[]
Score=[]
Total_Marks=[]


for i in range(1,201):
    Name.append(Std_name[rand.randint(0, 9)])
    Subject.append(Subject_name[rand.randint(0, 4)])
    Score.append(rand.randint(0, 100))
    Total_Marks.append(100)
    
    
data={
"Name":Name,
"Subject":Subject,
"Total Marks":Total_Marks,
"Score":Score    
}    


Data_frame= pd.DataFrame(data,index=np.arange(1,201))

print(Data_frame)



Score_array = np.array(Data_frame["Score"])
Score_Mean = np.mean(Score_array)
print("The Score mean is : ", Score_Mean)
Score_Median = np.median(Score_array)
print("The Score Median is : ", Score_Median)
Score_StDev =np.std(Score_array)
print("The Score Standard Deviation is: ",Score_StDev)


filter_Std= Data_frame[Data_frame['Score']>80]
print("Total Students who Achieved more than 80% score: ",len(filter_Std))



Group_data = Data_frame.groupby("Subject").mean(True)["Score"]
print(Group_data)

plt.title("Distribution of Score across all the Students")
plt.hist(Data_frame["Score"], bins=10, rwidth=0.7)
plt.xlabel("Score")
plt.ylabel("No of Students")
plt.show()


plt.title("Average scores across different subjects")
plt.bar(Group_data.index,Group_data.values,color='purple')
plt.xlabel("Subjects")
plt.ylabel("Score")
plt.show()