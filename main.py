# 1. Сreate a class hierarchy of animals with at least 5 animals that
# have additional methods each, create an instance for each of the animal
# and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
# class Animals:


class Animal:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + self.age )

    def sleep(self):
        print(self.name + self.age )


class Animal1(Animal):

    def eat(self):
        print(self.name + self.age)

    def sleep(self):
        print(self.name + self.age)



class dog(Animal):
    def barks(self):
        print("Барон"+"3года")

    def eat(self):
        print("мясо")

class cat(Animal):
    def purrs(self):
        print("Барсик"+" 5лет")

    def eat(self):
        print("молоко")

class pig(Animal):
    def grunts(self):
        print("наф-наф"+"1год")

    def eat(self):
        print("кашу")

class duck(Animal):
    def quacks(self):
        print("Ганс"+"2года")

    def eat(self):
            print("зерно")

class cow(Animal):
    def mooing(self):
        print("Марта"+"4года")

    def eat(self):
        print("зеленую траву")






#1a Create a new class Human and use multiple inheritance to create Centaur class,
# create an instance of Centaur class and call the common method of these classes and unique.

class Animal :
    def eat(self):
        print("eats when he wants")

    def sleep(self):
        print("Good sleep 8 hours")

    def work(self):
        print("a human working day is 8 hours")

    def study(self):
        print("a human working day is 8 hours")

class human:
    def work(self):
        print("a human working day is 8 hours")

    def study(self):
        print("a human working day is 8 hours")


class centaur(Animal,human ):
    def eat(self):
        print("eats when he wants")

    def sleep(self):
        print("Good sleep 8 hours")

a = human()
b = centaur()
print(human)
print(centaur)


# 2. Сlass Profile:
# Create regular class taking 8 params on
# init - name, last_name, phone_number, address, email, birthday, age, sex
# Override a printable string representation of Profile class and return:
# list of the params mentioned above


class my_Profile:
    def __init__(self, name, last_name,  phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex


    def __str__(self):
        return F"name ={self.name}\n," \
               F"Last_name:{self.last_name}\n," \
               F"Phone_number:{self.phone_number}\n," \
               F"Address:{self.address}\n," \
               F"Email:{self.email}\n," \
               F"Birthday:{self.birthday}\n," \
               F"Age:{self.age }\n," \
               F"Sex:{self.sex}\n," \

    my_Profile = prof ("Margo\n", "Kostian\n","+380507251563\n","Kherson\n",
                          "kostanm15@gmail.com\n", "6 October\n","39\n","woman\n")

    print(prof)





#3 Create an interface for the Laptop with the next methods:
# Screen, Keyboard, Touchpad, WebCam, Ports, Dynamicsand
# create an HPLaptop class by using your interface.


class Laptop_Lenovo(interface):

    def Screen(self):
        print("screenshot")

    def Keyboard(self):
        print("Keyboard Lenovo")

    def Touchpad(self):
        print("Touchpad Lenovo")

    def WebCam(self):
        print("WebCam Lenovo")

    def Ports(self):
        print("Ports Lenovo")

    def Dynamic(self):
        print("Dynamic Lenovo")

len = Laptop_Lenovo()
len.Keyboard()
len.Ports()
len.WebCam()
len.Screen()
len.Dynamic()
len.Touchpad()






























