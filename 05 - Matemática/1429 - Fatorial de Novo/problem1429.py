fatorial = [1, 2, 6, 24, 120]
var = 1
while (var == 1):
    acm = input()
    racm = acm[::-1] 
    dec = int(0)

    if (acm == "0"):
        break

    for index in range (len(acm)):
        dec += int(racm[index])*int(fatorial[index])

    print(dec)