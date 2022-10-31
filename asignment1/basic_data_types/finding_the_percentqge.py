if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
from statistics import mean
for key in student_marks:
    if query_name == key:
        listx = student_marks[key]
        avrg = mean(listx)
        avrgrn = "{:.2f}".format(avrg)
        print(avrgrn)