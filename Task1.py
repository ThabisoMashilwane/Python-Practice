
name = input("Please Enter you full name: ")
name_lst = name.split()
clean_name = " ".join(name.split())
print("Name: "+clean_name)
print("Type : "+ str(type(name)))
print("Greetings "+ clean_name.title()+"!")
initials = ".".join(word[0].upper() for word in name_lst)
print("Your intials are: "+initials)

