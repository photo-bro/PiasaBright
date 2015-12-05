'''
Created on Dec 2, 2015

@author: Josh Harmon
'''
from flask_restful import Resource, reqparse

# local imports
from Facade import *
from Authorization.Session import SessionManager
from Authorization.Users import User

class Ping(Resource):
    # Returns App Name and Version
    def get (self):
        return {'App Name': AppName, 
                 'Version': GetVersion()}
    
class Auth(Resource):
    
    def __init__(self):
        self.requestParser = reqparse.RequestParser()
        self.requestParser.add_argument('username', type=str, required=True,
                                   help='No username provided', location='json')
        self.requestParser.add_argument('password', type=str, required=True,
                                   help='No password provided', location='json')
        super(Auth, self).__init__()
    
    def post(self):
        args = self.requestParser.parse_args()
        if User.IsAuthorized(args['username'], args['password']):
            newSession = SessionManager.CreateActiveSession(args['username'])
            return {'message':'User: {} is authorized'.format(args['username']),
                        'sid': newSession.id,
                     'valid time (min)': newSession.activePeriod / 60}
        else:
            return {'message':'User not authorized'}
















