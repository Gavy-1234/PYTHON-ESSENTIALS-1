I=float(input("Enter any natural number: "))
d=0
f=1
if(I%1==0 and I>0):
    while(I//f>=1):
        d+=1
        f=f*10
        print("The total number of digit is: ",d)
else:print("This is not a natural number.")         
