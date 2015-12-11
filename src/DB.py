'''
Created on Dec 5, 2015

@author: jharm
'''
import os
from sqlite3 import dbapi2 as sqlite

class Database:
    _connection = None
    _cursor = None
    _isConnected = False
    
    @classmethod
    def OpenDb(cls):
        if cls._connection is None or cls._cursor is None:
            dbName = 'PiasaBright.db'
            cls._connection = sqlite.connect(dbName, 
                                            detect_types=sqlite.PARSE_DECLTYPES,
                                            check_same_thread=False)
            cls._cursor = cls._connection.cursor()
            cls._isConnected = True
    
    @classmethod
    def GenerateDb(cls):
        path = os.path.dirname(__file__)
        with open (path + '/SqlScripts/' + 'CreateDB' + '.sql', "r") as myfile:
            data=myfile.read()
        cls._cursor.executescript(data)
         
    
    @classmethod
    def ExecuteScriptFile(cls, script, args = None):
        '''
        script is the file name (not full path) for the SQL script
        NOTE: script must be in src/SqlScripts/ to run.
        '''
        if not cls.IsConnected():
            return False
        data = cls.GetProcedure(script, args)
        try:
            cls._cursor.execute(data)
            rows = cls._cursor.fetchall()
            return rows
        except:
            raise
        
    @classmethod
    def ExecuteScript(cls, script):
        if not cls.IsConnected():
            return False
        try:
            cls._cursor.executescript(script)
            return cls._cursor.fetchall()
        except:
            raise
    
    @classmethod
    def IsConnected(cls):
        return cls._isConnected
    
    @staticmethod
    def GetProcedure(procedureName, arguments):
        '''
        procedureName: File name for SQL script sans '.sql'. Must be in local
        /SqlScripts folder
        arguments: Dictionary (argumentName, argumentValue) where argumentName
        is the placeholder name in script that argumentValue will replace
        '''
        # open procedure file
        path = os.path.dirname(__file__)
        try:
            with open(path + '/SqlScripts/' + procedureName + '.sql', 'r') as procFile:
                rawProc = procFile.read()
        except FileNotFoundError:
            raise
        
        # replace placeholder names with arguments
        if arguments:
            for argName, argVal in arguments.items():
                rawProc = rawProc.replace('&{}&'.format(argName), argVal)
                        
        return rawProc
    
    
        
        
        
    
    
    
    
    
    
    
    
    