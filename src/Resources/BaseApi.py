'''
Created on Dec 2, 2015

@author: Josh Harmon
'''
from flask_restful import Resource, reqparse

# local imports
from Facade import *
from Session import Session
from Users import User

class Ping(Resource):
    # Returns App Name and Version
    def get (self):
        return {'App Name': AppName, 'Version': GetVersion()}
    
class Login(Resource):
    
    def __init__(self):
        self.requestParser = reqparse.RequestParser()
        self.requestParser.add_argument('username', type=str, required=True,
                                   help='No username provided', location='json')
        self.requestParser.add_argument('password', type=str, required=True,
                                   help='No password provided', location='json')
        super(Login, self).__init__()
    
    def post(self):
        args = self.requestParser.parse_args()
        for k, v in args:
            print('{} : {}'.format(k, v))
        if User.IsAuthorized(args['username'], args['password']):
            sessionId = Session.CreateActiveSession(args['username'])
            return {'message':'User {} authorized'.format(args['username']),
                     'sid':sessionId}
        else:
            return {'message':'User not authorized'}
    
    def get(self):
        return {'App Name': AppName, 'Version': GetVersion()}
    
    
    
    
    
    
    
    
    
