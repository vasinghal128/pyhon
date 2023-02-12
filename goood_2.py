import time 
samay =  time.strftime('%H:%M:%S')
print(samay)
hour = int(time.strftime('%H'))
if(hour>=0 and hour<12):
    print("Good morning")
elif(hour>=12 and hour<16):
    print("Good afternoon")
elif(hour>=16 and hour<19):
    print("Good Evening")
else:
    print("Good night")