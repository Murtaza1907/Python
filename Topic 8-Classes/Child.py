class Animal:
    def eat(self):
        print("Animal can eat")
        
    def sleep(self):
        print("Animal can sleep")    

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

myobj = Dog()
myobj.eat() #Call parent class function from child class
myobj.sleep() #Call parent class function from child class
myobj.bark()  #Call child class function from child class