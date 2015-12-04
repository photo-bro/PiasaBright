'''
Created on Dec 3, 2015

@author: jharm
'''
import uuid
from builtins import classmethod

# local
from Singleton import Singleton


class Session:
    __activeSessions = {}

    
    @classmethod
    def IsSessionValid(cls, sessionId):
        for k in cls.__activeSessions:
            if cls.__activeSessions[k] == sessionId:
                return True
        else:
            return False
    
    @classmethod
    def CreateActiveSession(cls, username):
        rawGuid = uuid.uuid4()
        cleanGuid = str(rawGuid).translate('', '-')
        cls.__activeSessions[username] = cleanGuid
        return cleanGuid
    
    @classmethod
    def DeactivateSession(cls, username, sessionId):
        if cls.__activeSessions[username] != sessionId:
            return 'Invalid sessionId for username'
        try:
            del cls.__activeSessions[username]
        except:
            return 'Username does not exist or already deactivated'