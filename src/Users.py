'''
Created on Dec 3, 2015

@author: jharm
'''


class User:
    __users = {'josh':'1234'}
    
    @classmethod
    def IsAuthorized(cls, username, password):
        if cls.__users[username] == password:
            return True
        else:
            return False
    