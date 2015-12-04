from datetime import datetime



class Schedule():
    
    def __init__(self):
        self.Name = ""
        self.Days = [] # days of the week
        self.Times = [] # tuples, (startTime, endTime)
        self.Presets = []
        self.Active = False
        
        
        