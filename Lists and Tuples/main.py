# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
movie1 = input("Enter your fav movie : ")
movie2 = input("Enter your fav movie : ")
movie3 = input("Enter your fav movie : ")
# list = [movie1,movie2,movie3] #alternativee
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method

list = [1,2,3,3,2,1]
palindrome = list.copy()
palindrome.reverse()

if(palindrome == list):
    print("palindrome list")
else : 
    print("not a palindrome list")    

# WAP to count the number of students with the 'A' grade in the following tuple.
#['C', 'D', 'A', 'A', 'B', 'B', 'A']

tup = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
tup.count('A')
print(tup.count('A'))

# Store the above values in a list & sort them from “A” to “D”..

list = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
list.sort()
print(list)

