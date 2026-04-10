list = [100, 200, 300, 400]
list.append("nitin")
print(list)

list = [100, 200, 300, 400, 200]
print(list.count(200))

list = [100, 200, 300, 400]
print(list.index(400))

list = [100, 200, 300, 400]
list.remove(200)
print(list)

list = [400, 300, 200, 100]
list.sort()
print(list)

list = [400, 300, 200, 100]
list.reverse()
print(list)

list = [400, 300, 200, 100, 500, 800, 1200, 50, 80]
print(max(list))

list = [400, 300, 200, 100, 500, 800, 1200, 50, 80]
print(min(list))

list1 = ["1", "8", "1.0", "50", "nitin"]
list2 = ["6", "8", "7.0", "80", "python"]
list = list1 + list2
print(list)

list = [400, 300, 200, 100, 500, 800, 1200, 50, 80]
print(len(list))
