person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
print(person["children"][1])

# print out the name of the cat
print(person["pets"]["cat"])

# iterate through all children and print out each child
for c in person["children"]:
    print(c)

# print out the pets in this format:
# type of pet: dog name of pert: Fido
for p, n in person["pets"].items():
    print(f"type of pet: {p} name of pet {n}")
