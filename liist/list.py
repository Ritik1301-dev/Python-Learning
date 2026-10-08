marks = [34,43,3,'R',43 , "+",234,]

print(marks , type(marks))

print(len(marks))

print(marks[4])

print(marks[-2])

# slicing a list 
print(marks[3:5])
print(marks[0:-1])

for score in marks:
    print(score)

marks.append(40)
print(marks)

marks.insert(4 ,'aaaaaaaaa')
print(marks)