import random
random_number = random.randint(1, 10)
# print(random_number)
user_input = input("Enter Guess Number inclusive (1, 10) : ")
user_input = int(user_input)
i = 0
while user_input != random_number:
    i = i + 1
    if random_number > user_input:
        print("Number is low")
        user_input = input("Enter again Guess Number : ")
        user_input = int(user_input)
    else:
        print("Number is high")
        user_input = input("Enter again Guess Number : ")
        user_input = int(user_input)


print("You Guess in {} turns ".format(i))