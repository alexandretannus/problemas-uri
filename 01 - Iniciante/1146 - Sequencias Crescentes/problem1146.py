
while(1):
    num = int(input())
    if num == 0: 
        break
        
    t = ""
    for i in range(1, num+1):
        t += "%i" % i
        if i != num:
            t += " "

    print(t)