num1=int(input("enter first number "))
num2=int(input("enter second number "))
num3=int(input("enter  third number "))

if(num1>num2 and num1>num3):
    print(" first number is greatest",num1) 
elif(num2>num3):
    print("number second is greatest",num2)

elif(num1==num2==num3):
    print("all three number are equal",num1,num2,num3)


else:
    print("number third is greatest",num3)