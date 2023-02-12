time = float(input("Check time"))
if(time>=1 and time<12):
    print("Good Morning")
elif(time>=12 and time<16):
    print("Good Afternoon")
elif(time>=16 and time<19):
    print("Good Evening")
else:
    print("Good night")