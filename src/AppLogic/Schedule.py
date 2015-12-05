'''
Created on Dec 3, 2015

@author: jharm
'''
from datetime import datetime

class Schedule():
    
    def __init__(self):
        self.Name = ""
        self.Days = [] # days of the week
        self.Times = [] # tuples, (startTime, endTime)
        self.Presets = []
        self.Active = False
        
    def ToDictionary(self):
        return {'name' : self.Name,
                'days' : self.Days,
                'times' : self.Times,
                'presets' : self.Presets,
                'active' : self.Active}