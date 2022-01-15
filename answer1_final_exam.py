secret_number=int(input("Enter secret number: "))
z=0
s=1
while s>0:
    s=int(input("Enter an integer number: "))
    if s==secret_number:
        print("\"Well done, muggle! You are free now.\"")
        break
    elif s!=secret_number:
        print("\"Ha ha! You're stuck in my loop!\"")
        z+=1
            
