import random

message = input("Guess the Number")
random_number = random.randint(1, 10)
print(random_number)
result = input("high , low or done : ")
i = 0
while result != "done":
    i = i + 1
    if result == "high":
        random_number = random.randint(1, random_number)
        print(random_number)
        result = input("high , low or done : ")
    elif result == "low":
        random_number = random.randint(random_number, 10)
        print(random_number)
        result = input("high , low or done : ")
    else:
        print("invalid Number")
        result = input("high , low or done : ")
    if i == 10:
        number = input("whats the number : ")
        number = int(number)
        print("Computer Loose")
        break

print("computer complete in turns {}".format(i))