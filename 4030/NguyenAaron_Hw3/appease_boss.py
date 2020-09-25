from heapq import heappush, heappop
def appease_boss(number_task):
    task_done = []
    task = []

    for i in range(len(number_task)):

        if len(number_task[i]) > 0:
            for j in range(len(number_task[i])):
                heappush(task, number_task[i][j])
            task_done.append(heappop(task))
        elif len(task) > 0:
            task_done.append(heappop(task))
        else:
            task_done.append(None)

    output = []
    for i in range(len(task_done)):
        if task_done[i] == None:
            output.append(None)
        else:
            output.append(task_done[i][1])
    print(output)





#
# task = [[(2, 100), (1,101)],
#         [(3, 102)],
#         [],
#         [],
#         [(2, 103), (3, 104), (1, 105)],
#         []]
# print(task)
appease_boss([[(2, 100), (1,101)],
              [(3, 102)],
              [],
              [],
              [(2, 103), (3, 104), (1, 105)],
              []])
