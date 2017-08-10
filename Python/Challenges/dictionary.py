'''Part I

Given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel'''

#def list_names(items):

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for student_dict in students:
    # student_dict['first_name'] + ' ' + student_dict['last_name']
    print "{} {}".format(student_dict['first_name'], student_dict['last_name'])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_part_deux(dict):
    for key in dict:
        print key
        for idx, user in enumerate(dict[key]):
            print "{} - {} {} - {}".format(
            idx+1,
            user['first_name'].upper(),
            user['last_name'].upper(),
            len(user['first_name']+user['last_name']) )

print_part_deux(users)
