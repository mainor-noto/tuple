fruit_tuple = ("apple","Banana","Cherry", "Date")
print(fruit_tuple[0])
print(fruit_tuple[-1])

slice_tuple = fruit_tuple[1:3]
print(slice_tuple)

num_tuple = (3, 5, 3, 2, 8, 3, 7)
count_three = num_tuple.count(3)
print(count_three)

index_eight = num_tuple.index(8)
print(index_eight)


person_info = ("Alice", 28, "Engineer")
name, age, profession = person_info
print(name)
print(age)
print(profession)