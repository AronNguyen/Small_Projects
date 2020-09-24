def main():
    test = open('test_file.txt', 'w')
    test.write('A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A\n')

    test.write('A, C, A, A, D, B, C, A, C, B, A, D, C, A, D, C, B, B, D, A\n')
    test.close()


    correct_answser = ['A', 'C', 'A', 'A', 'D',
                         'B', 'C', 'A', 'C', 'B',
                         'A', 'D', 'C', 'A', 'D',
                         'C', 'B', 'B', 'D', 'A']

    intest = open('test_file.txt', 'r')

    for line in intest:
        student_ans = line.rstrip()
        tuple_result = compare_ans(student_ans, correct_answser)

        if(tuple_result[0] >= 15):
            print("Passed with", tuple_result[0], "correct and", 20 - tuple_result[0], "missed")
            print("Questions missed: ", tuple_result[1])
        else:
            print("Failed with", tuple_result[0], "correct and", 20 - tuple_result[0], "missed")
            print("Questions missed: ", tuple_result[1])

def compare_ans(x, y):
    x = x.split(', ')
    print(x)
    cor = 0
    index_miss = []
    for i in range(20):

        if y[i] == x[i]:

            cor += 1
        else:
            index_miss.append(i)

    return (cor, index_miss)

main()
