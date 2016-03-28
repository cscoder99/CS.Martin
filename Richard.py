class student(object):
    #lines 3-6: constructor function(a special function called when object is created) 
    def __init__(self, name, gender, age, grade):
        self.name = name #stores name in object
        self.gender = gender #stores age in object
        self.age = age #stores gender in object
        self.grade = grade #stores grade in object
        self.friends = [] #stores a LIST of friends in object
        self.special_friend = None #stores friends in object
        self.ethnicity = None #stores ethnicity in object
        self.nickname = None #stores nickname in object
    def print_info(self):
        print "Name:",self.name
        print "Gender:",self.gender
        print "Age:",self.age
        print "Grade:",self.grade
        print "Friends:",self.friends
        print "Special Friend:",self.special_friend
        print "Ethnicity:",self.ethnicity
        print "Nickname:",self.nickname
    def promote(self):
        self.grade += 1
    
    def add_friend(self, newFriend):
        self.friends.append(newFriend)
        
    def remove_friend(self, newFriend):
        self.friends.remove(newFriend)
        
    def new_relationship(self, bae):
        self.special_friend = bae
        
    def get_older(self):
        self.age += 1
        
    def my_ethnicity(self, race):
        self.ethnicity = race
        
    def my_nickname(self, other):
        self.my_nickname = other