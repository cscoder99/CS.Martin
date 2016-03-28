from Richard import *

student1 = student('Richard', 'M', 16, 12)
student2 = student('Delilah', 'F', 17, 12)

print 'Student 1 info: '
print student1.name
print student1.gender
print student1.age
print student1.grade
print student1.friends
print student1.special_friend
print student1.ethnicity
print student1.nickname
print''
print 'Student 2 info: '
print student2.name
print student2.gender
print student2.age
print student2.grade
print student2.friends
print student2.special_friend
print student2.ethnicity
print student2.nickname
print''
print 'New Friends: '
print student1.add_friend('Lemuel')
print student2.add_friend('Janet')
print''
print 'Lose a friend: '
student1.remove_friend('Irving')
student2.remove_friend('Tianay')

print student2.friends
print''
print'New grade: '
student1.promote()
print student1.grade

student2.promote()
print student2.grade
print''
print'New age: '
student1.get_older()
print student1.age

student2.get_older()
print student2.age

