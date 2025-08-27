import string
import random
print("-------------------------------")
print("|   RANDOM PASSWORD GENERATOR  |")
print("-------------------------------\n")
a=int(input("SET THE LENGTH OF YOUR PASSWORD: "))
list=string.ascii_letters+string.digits+string.punctuation
passw=""
for i in range(1,a):
    randomm=random.choice(list)
    passw+=randomm
print("PASSWORD:",passw)