import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_sheet = pd.read_csv("monthly_benchmark_dataset.csv")

##Question 1
##Number of Students
print('Number of students')
print(len(data_sheet['FirstName']))

number_Students = len(data_sheet['FirstName'])
##Number of Sections
grouped = data_sheet.groupby('Section')
print('Number of Sections')
print(len(grouped))

##Number of Questions
print('Number of Questions')
print(len(data_sheet.iloc[0]) - 3)

print('')

##Question 7 Begin
for name,group in grouped:
    print('Group Name: ', name)
    print('Number of students in this Section: ', len(group))
    print('')
    ##print(group)
    ##prints the entire data_sheet sorted by group
##Quetsion 7 End

##
##
##check from 3 to 32

##Question 4,5

FinalEval = {}
cor_answ = []
stud_Name = []
total = 0
for i in range(number_Students):
    for j in range(3, 32):
        if(data_sheet.iloc[i,j].istitle()):
            total += 1
    cor_answ.append(total)
    stud_Name.append(data_sheet.iloc[i,0])
    total = 0

df = pd.DataFrame(FinalEval)
df['Student'] = pd.Series(stud_Name)
df['Correct_Answers'] = pd.Series(cor_answ)

# print(df.sort_values(by= 'Correct_Answers').head())
print(df.sort_values(by= 'Correct_Answers')[:5])
##prints the sorted version by least to greatest
print('')
# print(df.sort_values(by= 'Correct_Answers', ascending=False).head())
print(df.sort_values(by= 'Correct_Answers', ascending=False)[:5])


def get_section_info():
    sections = list(data_sheet['Section'].unique())
    print(sections)

    print('Grouped by Sections')
    grouped = data_sheet.groupby(['Section'])

print(get_section_info)






# print(df)

# y_pos = np.arange(len(stud_Name))
# # plt.bar(y_pos, cor_answ, align='center', alpha=0.5)
# # plt.xticks(y_pos, stud_Name)
# # plt.ylabel('Correct Answers')
# # plt.title('Questions')
#
# plt.barh(y_pos, cor_answ, align='center', alpha=0.5)
# plt.yticks(y_pos, stud_Name)
# plt.xlabel('Correct Answers')
# plt.title('Questions')
# plt.show()
