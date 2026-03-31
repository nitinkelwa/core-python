a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print("before = ", a)
a.clear()
print("after clear =", a)

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print(a.get("name"))

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print(a.keys())

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print(a.values())

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print(a.items())

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print(a.copy())

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
a.pop("name")
print(a)

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
a.popitem()
print(a)

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
a.update({"age": "22"})
print(a)

# a = {"name": "nitin", "surname": "kelwa", "age": "23"}
#  a.setdefault("add", "simrol")
#  print(a)

a = {"name": "nitin", "surname": "kelwa", "age": "23"}
print(len(a))


