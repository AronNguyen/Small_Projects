import pandas as pd
##to use pandas us python not py to run the program
# numbers = [10, 20, 30, 40, 50]
## prints in column form
##numbers = [[10, 20, 30, 40, 50]]
## prints in row form
# students = [['Jack', 'Daniel', 90],
#             ['John', 'Doe', 88],
#             ['Mary', 'Jennnings', 96],
#             ['Mustafa', 'Hizir', 96]]
# # df = pd.DataFrame(numbers)
# df = pd.DataFrame(students, columns = ['First name', 'Last Name', 'Grade'],
#                             index = ['student 1', 'student 2', 'student 3', 'student 4'])
# print(df)
# print(df['Grade'])
# print(print(df['First Name']))

# ##############################################################################################################
# ####################                    Dictionary                          ##################################
#
# students = [{'First Name': 'John', 'Last Name': 'Doe': 'Grade': 90},
#             {'First Name': 'Mary', 'Last Name': 'Jennings': 'Grade': 88},
#             {'First Name': 'Mustafa', 'Last Name': 'Hizir': 'Grade': 96},
#             {'First Name': 'Jack', 'Last Name': 'Daniel': 'Grade': 96}]
#
# df = pd.DataFrame(students)
# print(df)
#
#
# ##############################################################################################################
# ####################                    Series                              ##################################
#
# students =  {'First Name': pd.Series(['John', 'Mary', 'Mustafa', 'Jack'])},
#             {'Last Name':  pd.Series(['Doe', 'Jennings', 'Hizir', 'Daniel'])},
#             {'Grade':      pd.Series([90, 88, 79, 96])}
#
# df = pd.DataFrame(students)
# print(df)
# print(df.columns)
# ## gives you the columns
# print(list(df.columns))
# ## gives you the columns but in list form
# print(df['First Name'])
# ## gives the column names
# print(type(df['First Name']))
# ## gives the type of 'First Name'
# print(df[['First Name'], ['Grade']])
# ## gives you muliple columns
# ## type is DataFrame
#
#
# df['Grade 2'] = pd.Series([68,86,92,95])
# ## adds an addtional column
# print(df)
#
#
# df['Grade 3'] = pd.Series([45,55,65,48])
# ## adds an addtional column
# print(df)
#
# df['Middle Name'] = pd.Series(['K', 'M', 'J', 'I'])
# print(df)
#
# df['Total Grade'] = s1 + s2 + s3
# print(df)
#
# del df['Total Grade']
# print(df)
#
#
#
# ##############################################################################################################
# ####################                    Rows                                ##################################
#
# df = pd.DataFrame(students)
#
# print(df.index)
# print(len(df.index))
# print(type(df.index))
#
# df2 = pd.DataFrame(students2)
# ##students2 is another set of data didnt make it
# df = df.append(df2)
# print(df)
#
# # print(df.drop(0))
# ## deletes rows that have index 0
# df.drops(0, inplace= True)
#
# ##Row selction by index
# print(df[2:3])
# ##printing the 3 row
#
# print(df[2:4])
##printing the 3 and 4 row

##Row selection by lable
# my_data = [{'x':10, 'y':20},
#            {'x':55, 'y': 33},
#            {'x': 39, 'y': 41}]
#
# my_data = [{'x':10, 'y':20, 'z': 11, 't':48, 'k':137},
#            {'x':55, 'y': 33, 'z': 22, 't':5, 'k':83},
#            {'x': 39, 'y': 41, 'z': 19, 't':55, 'k':94},
#            {'x': 29, 'y': 62, 'z': 3, 't':76, 'k':182}]
#
# df = pd.DataFrame(my_data, index=['row_1','row_2','row_3', 'row_4'])
# print(df)
# print()
# # print(df.loc['row_2'])
# ##prints the row_2
# print(df.loc[['row_1', 'row_2']])
# #prints row_1 and row_2
# print(df.loc[['row_1', 'row_2'], ['x']])
# #prints row_1 and row_2 with only the x column
# print(df.iloc[2])
##prints out row_3
# print(type(df.iloc[2]))
# print(df.iloc[2,3])
##prints the value at 3rd row 4th column == 41
## use iloc to find specfifc values
# print(df.iloc[[2,3]])
##prints row_3 and row_4
# print(df.iloc[:3])

# ##############################################################################################################
# ####################                    Grouping                            ##################################


student_grades =  {'First Name': pd.Series(['John', 'Mary', 'Mustafa', 'Jack', 'Smith', 'Joshua', 'Adam', 'Robert'])},
{'Last Name':  pd.Series(['Doe', 'Jennings', 'Hizir', 'Daniel', 'Mullings', 'Stevens', 'Sander', 'Deniro' ])},
{'Grade':      pd.Series([90, 88, 79, 96, 68, 92, 82, 98])},
{'Section':    pd.Series(['A', 'B', 'C', 'C', 'B', 'A', 'A'])}

df = pd.DataFrame(student_grades)
grouped = df.groupby('Section')
print(grouped)
print(grouped.groups)

for name,group in grouped:
    print('Group Name: ', name)
    print(group)
