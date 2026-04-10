list1 = [1,2,3,4,5,6,6,5,6,]
list2 = [6, 8, 7.0, 80, ]
list = list1 + list2

print(list1)
print(list2)
print(list)

list.append(3)
print(list)


print(list.count(6))

list.insert(4, 100)
print(list)


list.remove(80)
print(list)

list.reverse()
print(list)

