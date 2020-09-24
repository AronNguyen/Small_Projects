import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

total_number_of_students = 0
total_number_of_questions = 0
total_number_of_sections = 0

def basic_statistics(df):
    global total_number_of_students, total_number_of_questions, total_number_of_sections
    total_number_of_students = len(df.index)
    total_number_of_questions = len(df.columns) - 3
    total_number_of_sections = len(df['Section'].unique())
    print("Number of students: ", len(df.index))
    print("Number of questions: ", len(df.columns) - 3)
    print("Number of sections: ", len(df['Section'].unique()))

def sucess_by_student(df):
    dict_sucess = {}

    for (idx, row) in df.iterrows():
        student_name = row.loc['FirstName']
        dict_correct[student_name] = 0

        for i in range(1, total_number_of_questions):
            if i < 10:
                question_no = '1_0' + str(i)
            else:
                question_no = '1_' + str(i)
            if row.loc[question_no].isupper():
                dict_correct[student_name] += 1
            # if row.loc[question_no].islower():



df_raw_data = pd.read_csv('monthly_benchmark_dataset.csv')
print(df_raw_data)
basic_statistics(df_raw_data)
print('')
sucess_by_student(df_raw_data)
