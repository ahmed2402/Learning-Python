# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for val in list :
    print(val)


# Search for a number x in this tuple using loop:
#     (1, 4, 9, 16, 25, 36, 49, 64, 81,100)    

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

for val in tuple :
    print(val)
    if(val == 36):
        print("36 found")
        break

# Print numbers from 1 to 100.    

for i in range(1,101):
    print(i)

# Print numbers from 100 to 1.

for i in range(100,0,-1):
    print(i)


# Print the multiplication table of a number n.

num = int(input("enter a number : "))

for i in range(num,num*11,num):
    print(i)

for i in range(1,11):
    print(num*i)


# WAP to find the sum of first n numbers. (using while)

sum = 0 
i=0
while(i<100) :
    sum = sum +i
    i+=1
print(sum)    

# WAP to find the factorial of first n numbers. (using for)

num = int(input("Enter a number : "))
fact = 1
for i in range(1,num+1):
      fact = fact * i
      i+=1

print("fact : ", fact)      