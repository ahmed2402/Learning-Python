# Create a new file “practice.txt” using python. Add the following data in it: 
# Hi everyone
# we are learning File I/O
# using Java. I like programming in Java

# with open("practise.txt", "w") as f :
#     f.write("Hi everyone we are learning File I/O\n")
#     f.write("using Java. I like programming in Java\n")
# WAF that replace all occurrences of “java” with “python” in above file.

# with open("practise.txt", "r") as f :
#     data = f.read()
#     newData = data.replace("Java","Python")
#     print(newData)

# with open("practise.txt", "w") as f :
#     new = f.write(newData)    
#     print(new)
# Search if the word “learning” exists in the file or not. 
# def checkWord() :
#  with open("practise.txt","r") as f :
#     data = f.read()
#     word = "xlearning"
#     if(data.find(word) != -1):
#         print("exists")
#     else :
#         print("doesnt exists")

# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

# def checkLine():
#     word = "learning1"
#     data = True
#     line_no = 1
#     with open("practise.txt","r") as f :
#        while data:
#           data = f.readline()
#           if(word in data):
#              print(line_no)
#              return
#           line_no += 1

#     return -1       
  
# print(checkLine())
# 
# From a file containing numbers separated by comma, print the count of even numbers.

with open("123.txt", "r") as f :
    data = f.read()
    count = 0 
    numbers = data.split(',')
    count = 0
    for number in numbers:
        if int(number) % 2 == 0:
            count += 1
    print(count)
