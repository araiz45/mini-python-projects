first_person_name = input("Enter first person name : ")
first_person_age = input("Enter {}'s age : ".format(first_person_name))
second_person_name = input("Enter second person name : ")
second_person_age = input("Enter {}'s age : ".format(second_person_name))


first_person_age = int(first_person_age)
second_person_age = int(second_person_age)
difference_a = first_person_age - second_person_age
difference_b = second_person_age - first_person_age
difference_a = str(difference_a)
difference_b = str(difference_b)

# print(first_person_age, second_person_age, type(first_person_age), type(second_person_age))

if first_person_age > second_person_age:
    print("{} is {} Years Older than {} ".format(first_person_name, difference_a, second_person_name))
elif second_person_age > first_person_age:
    print("{} is {} Years Older than {} ".format(second_person_name, difference_b, first_person_name))
else:
    print("{} and {} have same age ".format(first_person_name, second_person_name))
