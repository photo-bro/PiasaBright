'''
Created on Dec 3, 2015

@author: jharm
'''

class PresetManager():
    __Presets = []
    
    @classmethod
    def Add(cls, preset):
        cls.__Presets.append(preset)

    @classmethod
    def Remove(cls, preset):
        try:
            cls.__Presets.remove(preset)
        except:
            pass

class Preset():
    
    def __init__(self):
        self.Name = ""
        self.Fixtures = []
        
    def AddFixture(self, fixture):
        self.Fixtures.append(fixture)
    
    def RemoveFixture(self, fixture):
        self.Fixtures.remove(fixture)
    
    def ToDictionary(self):
        return {'name' : self.Name,
                'fixtures': self.Fixtures}