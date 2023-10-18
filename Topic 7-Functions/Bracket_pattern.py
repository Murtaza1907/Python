def check(given):
    mylist = []
    for a in given:
        if len(given) %2 ==0:
            if a == "(":
                mylist.append(a)
            elif a == ")" and "(" not in mylist:
                return False
            elif a == ")":
                mylist.pop()
        else:
            return False
    if len(mylist) == 0:
        return True
    else:
        return False

a = "()((()))"
print(check(a))