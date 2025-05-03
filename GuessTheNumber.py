import random
print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
num=int(input("Enter the number b/w 1 to 9:"))
for num in range(1,10):
    int(input("Please enter again in b/w 1 to 9:"))
print(num,"is the number entered by user:")
comp_num= random.randint(1, 10)
print(comp_num,"is the number randomly taken by comp:")
if num==comp_num:
    print("user guess is Absoluetly Correct!!!!!!!!!!")
else:
    print("Oh NO user guess is Incorrect!!!!!!!!!!")
