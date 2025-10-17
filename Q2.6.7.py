def bt7():      # result :343
    return print((a()+b()) % 999)
def a(): # Trả về phần tử thứ 1000 của a
    arr = [0]*2
    arr[0] = 1
    arr[1] = 3
    for i in range(2,1001):
        arr.append(6*arr[i-1] - 2*arr[i-2])
    return arr[1000]
def b(): # Trả về phần tử thú 1000 của b
    arr = [0]*2
    arr[0] = 0
    arr[1] =-1
    for i in range(2,1001):
        arr.append(6*arr[i-1] - 2*arr[i-2])
    return arr[1000]
bt7()