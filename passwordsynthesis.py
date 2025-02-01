import random
condition = input("Would you like a password: ")
condition = condition.lower()
if condition == "yes":
    count = int(input("How long should it be?: "))
    list = ""
    
    for partoflist in range(count):
        partoflist = chr(random.randint(33,126))
        list += partoflist
else:
    exit()
print("Your new password is: ", list)