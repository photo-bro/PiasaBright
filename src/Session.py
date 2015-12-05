'''
Created on Dec 3, 2015

@author: jharm
'''
import uuid, time
from builtins import classmethod

class SessionManager:
    __activeSessions = []
    
    @classmethod
    def CreateActiveSession(cls, username):
        newSession = Session(username)
        cls.__activeSessions.append(newSession)
        return newSession
    
    @classmethod
    def DeactivateSession(cls, session):
        try:
            cls.__activeSessions.remove(session)
        except:
            return 'Session does not exist or already deactivated'

    @classmethod
    def GetActiveSessions(cls):
        return [s for s in cls.__activeSessions if s.IsValid()]

class Session:

    def __init__(self, username, activePeriod = 60):
        rawGuid = uuid.uuid4()
        cleanGuid = str(rawGuid).replace('-', '')
        self.id = cleanGuid
        self.username = username
        self.timeCreated = time.time()
        self.activePeriod = activePeriod * 60 # store in seconds
    
    def __initId(self):
        rawGuid = uuid.uuid4()
        cleanGuid = str(rawGuid).replace('-', '')
        return cleanGuid
    
    def IsValid(self):
        timeDelta = self.timeCreated - time.time()
        return (timeDelta > self.activePeriod)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        