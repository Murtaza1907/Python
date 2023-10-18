def dig_pow(number,power):
    total = 0
    strnum = str(number)
    for i in range(len(strnum)):
        total = total + int(strnum[i]) ** power
        power = power + 1
    print("Total =",total)
    quotent = total // number
    print(total,"/",number,"=",quotent)

dig_pow(46288, 3)