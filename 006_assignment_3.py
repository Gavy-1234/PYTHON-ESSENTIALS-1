h=int(input("Give me the start time(hour): "))
m=int(input("Give me the start time(minute): "))
d=int(input("Give me the duration in minutes: "))
r=(h*60)+m+d
print("The finish time is: ",end="")
print(r//60,r%60,sep=":")
