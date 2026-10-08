marks = {"Math": 99 , "Chemistry": 98 , "AIML": 97}
print(marks , type(marks)) 
print(marks["Math"])

marks["English"] = 99
print(marks["English"])

for key in marks:
    print(key , marks[key])