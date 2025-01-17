info = {"talha", 19, "pakppatan", 5042, 7429, "pakppatan",}
print(info)
print(len(info)) #in which length not account the doblicate value 
#empty set
collection = set()
print(collection)
#method of set in python
#add method 
collection = set()
collection.add(1)
collection.add("talha")
collection.add("rao")
collection.add(1)
collection.add("starc")
print(collection)
#remove set    set.remove()
collection.remove("rao")
print(collection)
#clear set      set.clear()
collection.clear()
print(collection)
#set pop remove a rnadom value set.pop()
timetable = {'sun', 'mon','tue','wed','thu','fri','sat'}
print(timetable.pop())
print(timetable.pop())
#set union
set1 = {1,3,3,4,5}
set2 = {3,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
#paractice question
marks = {}
x = int(input("eneter phy :"))
marks.update({"phy": x})
x = int(input("eneter math :"))
marks.update({"math": x})
x = int(input("eneter bio :"))
marks.update({"bio": x})
print(marks)