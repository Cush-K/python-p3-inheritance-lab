#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, firstname, lastname, knowledge = None):
        super().__init__(firstname, lastname)
        if knowledge is None:
            knowledge = [
                "str is a data type in Python",
                "programming is hard, but it's worth it",
                "JavaScript async web request",
                "Python function call definition",
                "object-oriented teacher instance",
                "programming computers hacking learning terminal",
                "pipenv install pipenv shell",
                "pytest -x flag to fail fast",
            ]
            
        self.knowledge = knowledge
    
    def learn(self, new_info):
        self.knowledge.append(new_info)
        return self.knowledge
    

boy = Student("John","Doe")
print(boy.learn("stuffs!"))