#  A Function is a reusable block of code that performs a specific task. 

# -------------------------Local Scope :- Variable defined within a function---------------------------------

def my_function():
    x = 10   # x is a local variable
    print(x)

my_function()



def nikki():
    x = 120
    print(x**2)

nikki()


# --------------------------Global Scope :- Variable defined within a global function--------------------------------
x = 10                 # x is a global variable

def my_global_function():
    print(x)

my_global_function()


#------------------------------------------Non-Local Scope---------------------------------------------- 

x = 10     # global variable

def modify_global():
    global x   
    x = 20       






import random 

def guess_number():
    return random.randint(1,100)

target_number = guess_number()
attempts = 0 

while True:
    user_guess = int(input("Guess the number :"))
    attempts += 1

    if user_guess == target_number:
        print("congratulations! You guessed the number n " , attempts , "attempts" )

    elif user_guess > target_number:
        print("Too Large , please guess Lower number")

    else:
        print("Too low , please guess higher number")