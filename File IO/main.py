# Create a new file “practice.txt” using python. Add the following data in it: 
# Hi everyone
# we are learning File I/O
# using Java. I like programming in Java

# with open("practise.txt", "w") as f :
    # f.write("Hi everyone we are learning File I/O\n")
    # f.write("using Java. I like programming in Java\n")
# WAF that replace all occurrences of “java” with “python” in above file.

with open("practise.txt", "r") as f :
    data = f.read()
    newData = data.replace("Java","Python")
    print(newData)

with open("practise.txt", "w") as f :
    new = f.write(newData)    
    print(new)
# Search if the word “learning” exists in the file or not. 
