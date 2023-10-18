def solve(word):
    updatedstring = ""
    for i in range(len(word)):
        if word[i].isupper():
            updatedstring = updatedstring + " " + word[i]

        else:
            updatedstring = updatedstring + word[i]
    return (updatedstring)


print(solve("camleCasingHello"))