name = input ("enter your full name : ")
lowercase_name = name.lower ()
find_space = lowercase_name.count(" ")

find_letter = lowercase_name.count("a")


print(lowercase_name)
print(find_letter)
print(find_space)
print(len(name))
print(f" The first letter of your name : {name[0]} and last letter your name : {name[len(name)- 1]}")