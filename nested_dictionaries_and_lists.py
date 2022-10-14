x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #1-1
x[1][0] = 15
# #1-2
students[0]["last_name"] = "Bryant"
# #1-3
sports_directory["soccer"][0] = "Andres"
# #1-4
z[0]["y"] = 30

students = [
         {'first_name' : 'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#2

def iterateDictionary(some_list):
    i = 0
    while i < len(some_list):
        print("first_name - " + students[i]["first_name"] + ", last_name - " + students[i]["last_name"])
        i += 1
iterateDictionary(students)

#3

def iterateDictionary2(key_name, some_list):
    i = 0
    while i < len(some_list):
        print(some_list[i][key_name])
        i += 1

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#4
def printInfo(some_dict):
    for key in dojo :
        print( len(dojo[key]), key)
        for value in dojo[key]:
            print(value)
printInfo(dojo)