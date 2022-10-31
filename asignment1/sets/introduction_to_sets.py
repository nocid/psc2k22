def average(array):
    array = set(array)
    result = '{:.3f}'.format((sum(array)/len(array)))
    return result
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)