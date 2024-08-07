def namata():
    number = float(input("Enter a number: "))
    for x in range(1, 11):
        print(number, "*", x, "=", number*x)

ask = input("Do you want to multiply a number?: ")
if ask.lower() != "yes":
     quit()
else:
    namata()



def hello(name, age):
    print("Hello", name )
    print("You are " + age + " years old")

# hello("Lihan", 17)
ask = input("What is your name?: ")
time = input("What is your age?: ")
if ask.lower() and time.lower() != "":
    hello(ask, time)              




