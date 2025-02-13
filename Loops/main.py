# Print numbers from 1 to 100. 

i = 1 
while i<=100 : 
    print(i)
    i += 1

# Print numbers from 100 to 1.
i = 100 
while i>=1 : 
    print(i)
    i -= 1

# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
i = 0
while i<len(list) :
    print(list[i])
    i += 1

# Print the multiplication table of a number n. 

num = int(input("Enter a number : "))
i=1
while i<=10 :
    print(num * i)
    i+=
    
# Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

search = int(input("Enter a number : "))
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

i=0
while i<len(tuple) :
    if tuple[i] == search :
        print("here u go : ", tuple[i])
    else :
        print("not found") 
    i+=1        
