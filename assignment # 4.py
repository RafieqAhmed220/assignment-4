#reverse string using for loop
name=input("enter string:")
print("original string is:",name)
r_name=""
for char in name:
    r_name=char+r_name
print("reversed string is:",r_name)