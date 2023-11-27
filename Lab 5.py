number1 = int(input("Enter number1"))
for number1 in range(1, number1):
    if (number1 %3==0) and (number1 %5==0):
        print(number1, "Tic Tac")
    if (number1%3==0):
        print(number1, "Tic")
    if (number1%5==0):
        print(number1, "Tac")
#To print number from 1-20
i=1
while i<21:
    i+=1
    print(i)
input1=int(input("Enter input1:"))
input=1
while input1<16:
    input1+=1
    if input1%3==0 and input1%5==0:
        print(input1, "Tic Tac")
    elif input1%3==0:
        print(input1, "Tic")
    elif input1%5==0:
        print(input1, "Tac")
#using random generator to genrate random number
import random
print(random.randint(20, 50))
limit = 5
while limit>0:
    user_value = int(input("Enter the value:")
    if user_value>0

print("Successful")
        #break
else:
        limit-=1
        print("invalid entry, please enter a valid value")
import random
user_value = int(input("Enter intvalue:"))
main = randint(1,user_value)
limit = 0
while True:
    limit+= 1
    my_value = int(input("first value:"))
    if my_value== main:
        print("perfect")
    #break
    elif my_value!=main:
        print("both numbers don't match")
else:
        print("invalid")