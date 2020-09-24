import pandas as pd
###Question 3
try:
    customer_file = pd.read_csv("customer_file.csv")
    n = len(customer_file['Name'])
    print("Name, PhoneNumber")
    for i in range(n):
        print(customer_file.iloc[i, 0], customer_file.iloc[i, 1])

except IOError:
    print('File not found')

print('Question 4')
### Question 4

class ScoreIsLessException():

    def __init__(self, msg):
        self.msg = msg

score = 86
# score = 49
try:

    if score < 50:
        raise(ScoreIsLessException('Score is too low'))
except ScoreIsLessException as e:
    print(e.msg)

finally:
    print(score)

### Question 5
print('Question 5')
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = list(filter(lambda x: x%2 == 1, my_list))
print( result)
