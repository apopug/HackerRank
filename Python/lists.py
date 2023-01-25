if __name__ == '__main__':
    N = int(input())
    listhack = []
    for i in range(0,N):
        text = input().split()
        if text[0] == "append":
            listhack.append(int(text[1]))
        elif text[0] == "print":
            print(listhack)
        elif text[0] == "remove":
            listhack.remove(int(text[1]))
        elif text[0] == "sort":
            listhack.sort()
        elif text[0] == "pop":
            listhack.pop()
        elif text[0] == "reverse":
            listhack.reverse()
        elif text[0] == "insert":
            listhack.insert(int(text[1]), int(text[2]))
        
