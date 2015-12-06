'''
Created on Dec 5, 2015

@author: jharm
'''
import sqlite3
from Singleton import Singleton

@Singleton
class Database:
    _connection = None
    _cursor = None

    @classmethod
    def OpenDb(cls):
        if cls._connection is None or cls._cursor is None:
            cls._connection = sqlite3.connect('PiasaBright.db')
            cls._cursor = cls._connection.cursor()
    
    @classmethod
    def GenerateDb(cls):
        cls.ExeceuteScriptFile('CreateDb')
    
    @classmethod
    def ExeceuteScriptFile(cls, script):
        '''
        script is the file name (not full path) for the SQL script
        NOTE: script must be in src/SqlScripts/ to run.
        '''
        if not cls.IsConnected():
            return False
        try:
            with open ('SqlScripts/' + script + '.sql', "r") as myfile:
                data=myfile.read()
            try:
                cls._cursor.executescript(data)
                return cls._cursor.fetchall()
            except:
                raise
        except FileNotFoundError:
            raise
        except:
            return []
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
        return cls._cursor == None
    
class ProcedureManager:
    
    def GetProcedure(self, procedureName, arguments):
        '''
        procedureName: File name for SQL script sans '.sql'. Must be in local
        /SqlScripts folder
        arguments: Dictionary (argumentName, argumentValue) where argumentName
        is the placeholder name in script that argumentValue will replace
        '''
        # open procedure file
        try:
            with open('SqlScripts/' + procedureName + '.sql', 'r') as procFile:
                rawProc = procFile.read()
        except FileNotFoundError:
            raise
        
        # replace placeholder names with arguments
        for argName, argVal in arguments:
            rawProc.replace('&{}&'.format(argName), argVal)
            
        return rawProc
        
        
        
    
    
    
    
    
    
    
    
    