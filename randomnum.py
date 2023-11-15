import random
import time


randomnum = input("Please choise the random number (10/20/30/40/50): ") # --- new version
print("Generating random number for you!! ")
print("Please wait! ")
time.sleep(3)

if randomnum == "10": 
    print(random.randrange(1, 10)) # ---- new version
elif randomnum == "20":
    print(random.randrange(10, 20))
elif randomnum == "30":
    print(random.randrange(20, 30))
elif randomnum == "40":
    print(random.randrange(30, 40))
elif randomnum == "50":
    print(random.randrange(40, 50))

print("Do you like the number??")
a = input(" --> (yes/no): ")

def number():
    b = input("Oh no, Do want me to generate another number? (yes/no): ")
    if b == 'yes':
        print(random.randrange(1, 50))
    else:
        print("Ok, be healthy! ")

if a == 'no':
    number()
elif a == "yes":
    print("I am very happy!! Thank you! ")

