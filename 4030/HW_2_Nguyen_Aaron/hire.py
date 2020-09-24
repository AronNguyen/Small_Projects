import math
def hire(x):
    max_time_current = 0
    max_time_last = math.inf

    for i in range(len(x)):
        for j in range(len(x[i])):
            if max_time_current < x[i][j]:
                max_time_current = x[i][j]
        if max_time_current < max_time_last:
            max_time_last = max_time_current
            company = x.index(x[i])
        max_time_current = 0
    print(company, x[company].index(max_time_last))











hire([[1, 4], [3, 2]])
