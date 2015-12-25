'''
Created on Dec 3, 2015

@author: jharm
'''
from DB import Database

class FixtureManager():
    
    def __init__(self):
        self.DB = Database()
        if not Database.IsConnected():
            self.DB.OpenDb()

    def Add(self, fixture):
        if not fixture:
            raise Exception('fixture')
        args = {'name' : fixture.Name, 
                'location':fixture.Location,
                'brightness':fixture.Brightness,
                'fixtureType': fixture.FixtureType}    
        errMsg = Database.ExecuteScriptFile('AddFixture', args)
        return errMsg;
        
    def Remove(self, fixture):
        if not fixture:
            raise Exception('fixture')
        args = {'id' : fixture.Id}
        errMsg = Database.ExecuteScriptFile('DeleteFixture', args)
        return errMsg
    
    def GetFixtures(self):
        args = {'id' : 'NULL',
                'name' : 'NULL', 
                'location':'NULL',
                'brightness':'NULL',
                'fixtureType':'NULL' }
        rows = Database.ExecuteStatementFile('GetFixture', args)
        fixtures = [] 
        for r in rows:
            fixtures.append(Fixture(r[0], r[1], r[2], r[3], r[4]))
        return fixtures
    
    def GetFixture(self, fixtureId = 'NULL', name = 'NULL'):
        if not fixtureId:
            fixtureId = 'NULL'
        if not name:
            name = 'NULL'
        args = {'id' : fixtureId, 'name' : name, 'location':'NULL',
                 'brightness':'NULL', 'fixtureType':'NULL'}
        rows = Database.ExecuteStatementFile('GetFixture', args)
        fixtures = []
        for r in rows:
            fixtures.append(Fixture(r[0], r[1], r[2], r[3], r[4]))
        return fixtures
    
class FixtureType():
        Blank = 1
        Light = 2
        DimmableLight = 3
        ColoredLight = 4

class Fixture():
    
    def __init__(self, id, name, location, fixtureType, brightness):
        self.Id = id
        self.Name = name
        self.Location = location
        self.FixtureType = fixtureType
        self.Brightness = brightness
        
    def ToDictionary(self):
        return {'name' : self.Name,
                'location' : self.Location,
                'fixtureType' : self.FixtureType,
                'brightness' : self.Brightness}
    
