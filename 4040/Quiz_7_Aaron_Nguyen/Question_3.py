def cal_Average_Formal(t1, t2, t3, t4, t5):

    return (t1 + t2 + t3 + t4 + t5)/ 5

def determine_Grade_Formal(score):

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

# score = input("To find letter grade enter a score. Enter -1 to find Average of 5 test scores: ")
# determine_Grade_Formal(int(score))
# score_1 = input("Enter 5 test scores\n")
# score_2 = input()
# score_3 = input()
# score_4 = input()
# score_5 = input()
# print(cal_Average_Formal(int(score_1),int(score_2),int(score_3),int(score_4),int(score_5)))

def cal_Average_Keyword(**kwarg):
    avg = 0
    for value in kwarg.items():
        avg += value[1]
    avg = avg / 5
    return avg

def determine_Grade_Keyword(**kwarg):
    for value in kwarg.items():
        score = value[1]
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

score = input("To find letter grade enter a score. Enter -1 to find Average of 5 test scores: ")
determine_Grade_Keyword(score = int(score))
score_1 = input("Enter 5 test scores\n")
score_2 = input()
score_3 = input()
score_4 = input()
score_5 = input()
print(cal_Average_Keyword(first = int(score_1),sec = int(score_2),third = int(score_3),fourth = int(score_4),fifith = int(score_5)))
