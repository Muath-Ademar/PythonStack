x = [ [5,2,3], [10,8,9] ] 

x[1][0]= 15
print (x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print (students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]



sports_directory['soccer'][0] =  'Andres'
print(sports_directory)

z [0]['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
            for student in students:
                for x in student.items():
                    print(x)

iterateDictionary(students)
    
def iterateDictionary2(key_name, students):
    for student in students:

            print(student[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name',students)


