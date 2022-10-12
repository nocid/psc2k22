if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
 
arr = list(arr)
print(max([a for a in arr if a!=max(arr)]))
