import random
import time


print("Generating random number for you!! ")
print("Please wait! ")
time.sleep(3)
print(random.randrange(1, 50))

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

