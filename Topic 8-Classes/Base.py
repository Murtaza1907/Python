class Manu:
    def __init__(self):
        print('Sandwich')
        print('Salad')
        print('Soup')
        print('Coffee')
        print('Tea')

class Sandwich(Manu):
    pirce_sandwich = 10

myobj = Sandwich()
print(myobj.pirce_sandwich)    