if __name__ == '__main__':
    N = int(input())
    arr = []
    for x in range(N):
        tmp = input().split()
        input1 = 0
        input2 = 0
        
        if(tmp[0] == "insert"):
            input1 = int(tmp[1])
            input2 = int(tmp[2])
            arr.insert(input1, input2)
        if(tmp[0] == "append"):
            input1 = int(tmp[1])
            arr.append(input1)
        if(tmp[0] == "print"):
            print(arr)
        if(tmp[0] == "remove"):
            input1 = int(tmp[1])
            arr.remove(input1)
        if(tmp[0] == "sort"):
            arr.sort()
        if(tmp[0] == "pop"):
            arr.pop()
        if(tmp[0] == "reverse"):
            arr.reverse()
