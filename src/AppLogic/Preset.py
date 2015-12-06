'''
Created on Dec 3, 2015

@author: jharm
'''
from DB import Database

class PresetManager():
    
    def Add(self, preset, fixtures):
        # Insert new preset first
        insertProc = 'INSERT INTO Preset (Name,) \
                      VALUES ({0})'.format(preset.Name)
        Database.ExecuteScript(insertProc)
        # Get id of new preset
        idProc = 'SELECT PresetId \
                  FROM Preset p \
                  WHERE p.Name = {0}'.format(preset.Name)
        idRows = Database.ExecuteScript(idProc)
        presetId = idRows['PresetId']
        # Add relation to fixtures via FixturePresetAssoc rows
        assocProc = ''
        for f in fixtures:
            assocProc += 'INSERT INTO FixturePresetAssoc (FixtureId, PresetId)\
                          VALUES ({0}, {1});'.format(f.Id, presetId)
        Database.ExecuteScript(assocProc)
    
    def Remove(self, preset):
        pass
    def GetPresets(self):
        proc = 'SELECT p.PresetId, p.Name, f.FixtureId \
                FROM Preset'
                
                
                
                
                
                
        rows = Database.ExecuteScript(presetProc)
        
        
    def GetPreset(self, id):
        
    
class Preset():
    
    def __init__(self, id, name, fixtures):
        self.Id
        self.Name = ""
        self.Fixtures = []
        
    def AddFixture(self, fixture):
        self.Fixtures.append(fixture)
    
    def RemoveFixture(self, fixture):
        self.Fixtures.remove(fixture)
    
    def ToDictionary(self):
        return {'name' : self.Name,
                'fixtures': self.Fixtures}