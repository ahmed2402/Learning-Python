# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

dict = {
    "table" : ["a piece of furniture", "list of facts & figures" ] ,
    "cat" : "a small animal"
}
print(dict) 

# You are given a list of subjects for students. Assume one classroom is required for 1subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,“java”, “python”, “java”, “C++”, “C”

subjects = {
    "python","java","C++","python", "javascript","java", "python", "java", "C++", "C"
}

print("Classroms required : " ,len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# dict = {

# }

sub1 = int(input("Enter marks of 1st Subject : \n"))
dict.update({"Subject 1" : sub1})
sub2 = int(input("Enter marks of 2nd Subject : \n"))
dict.update({"Subject 2" : sub2})
sub3 = int(input("Enter marks of 3rd Subject : \n"))
dict.update({"Subject 3" : sub3})

print(dict)

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

set = {9,"9.0"}
set2 = {
    (9),(9.0)
}

print(set)
print(set2)