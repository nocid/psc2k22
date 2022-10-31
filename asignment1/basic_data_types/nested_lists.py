if __name__ == '__main__':
    nested_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
        scores.append(score)
        
scores.sort()
x = scores[0]
a = scores.count(x)
x_value = scores[a]

nest_dic = dict(nested_list)
for key, value in sorted(nest_dic.items()):
     if value == x_value :
         print(key)