def atmCode(Code):
    if Code.isdigit():
        if len(Code) == 4 or len(Code) == 6:
             return True
        else:
            return False
    else:
        return False


Password = input("Enter your ATM Code for transection ")
print(atmCode(Password))