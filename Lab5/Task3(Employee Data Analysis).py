import numpy as np
import pandas as pd
import random as rand
import matplotlib.pyplot as plt

Emp_names=['Emp1','Emp2','Emp3','Emp4','Emp5','Emp6','Emp7','Emp8','Emp9','Emp10','Emp11','Emp12','Emp13','Emp14','Emp15','Emp16','Emp17','Emp18','Emp19','Emp20']
Dept_names=['Dept1','Dept2','Dept3','Dept4','Dept5']

Name=[]
Dept=[]
Salary=[]
Experience_Year=[]

for i in range(1,301):
    Name.append(Emp_names[rand.randint(0, 19)])
    Dept.append(Dept_names[rand.randint(0, 4)])
    Salary.append(rand.randint(30000, 120000))
    Experience_Year.append(rand.randint(1, 25))
    
    
data={
"Name": Name,
"Departement":Dept,
"Salary": Salary,
"Year of Experience":Experience_Year      
} 


Data_frame = pd.DataFrame(data,index=np.arange(1,301))

print(Data_frame)   



Salary_array = np.array(Data_frame['Salary'])

Avg_Salary = np.average(Salary_array)
print("The Average Salary is: ", Avg_Salary)
Min_Salary= np.min(Salary_array)
print("The minimum of salary is: ",Min_Salary)
Max_Salary=np.max(Salary_array)
print("The Maximum Salary is: ",Max_Salary)


filter_emp = Data_frame [(Data_frame ["Year of Experience"] > 5) & (Data_frame ["Salary"] > Avg_Salary)]
print("The Employee who have a salary abovve than Average Salary and have a more than 5 year of Experience:\n ",filter_emp)


group_Emp = Data_frame.groupby("Departement").mean(True)["Salary"]

print(group_Emp)

plt.title("Average Salary in each Department")
plt.bar(group_Emp.index, group_Emp.values)
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()



sorted_data = Data_frame.sort_values(by='Year of Experience')
plt.plot(sorted_data['Year of Experience'], sorted_data['Salary'], color='orange', marker='o')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary Distribution for Employees with Increasing Years of Experience")
plt.show()



