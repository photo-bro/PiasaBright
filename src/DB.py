'''
Created on Dec 5, 2015

@author: jharm
'''
import sqlite3


class Database:
    __connection = None
    __cursor = None

    @classmethod
    def OpenDb(cls):
        cls.__connection = sqlite3.connect('PiasaBright.db')
        cls.__cursor = __connection.cursor()
    
    @classmethod
    def GenerateDb(cls):
        cls.ExeceuteScript('CreateDb.sql')
    
    @classmethod
    def ExeceuteScript(cls, script):
        '''
        script is the file name (not full path) for the SQL script
        NOTE: script must be in src/SqlScripts/ to run.
        '''
        try:
            with open ('SqlScripts/' + script, "r") as myfile:
                data=myfile.read()
            cls.__cursor.executescript(data)
            return cls.__cursor.fetchall()
        except FileNotFoundError:
            raise
        except:
            return []
    
    @classmethod
    def IsConnected(cls):
        return cls.__cursor == None