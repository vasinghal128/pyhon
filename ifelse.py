age = input("What is your age")

if int(age)>=18:
    print("you are an adult")
    print("you can vote")
elif int(age) < 18 and int(age) > 3:
    print("You are in school")
else:
    print("You are a kid")