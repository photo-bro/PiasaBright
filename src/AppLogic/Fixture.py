'''
Created on Dec 3, 2015

@author: jharm
'''
from DB import Database

class FixtureManager():
    
    def __init__(self):
        self.DB = Database.Instance
        if not Database.IsConnected()
            self.DB.OpenDb()

    def Add(self, fixture):
        proc = 'INSERT INTO Fixture (Name, Location, Brightness, FixtureType) \
                VALUES ({0}, {1}, {2}, {3})'.format(fixture.Name,
                                                     fixture.Location,
                                                     fixture.Brightness,
                                                     fixture.FixtureType)
        Database.ExecuteScript(proc)
    
    def Remove(self, fixture):
        proc = 'DELETE FROM Fixture f \
                WHERE f.Id = {0}'.format(fixture.Id)
        return Database.ExecuteScript(proc)
    
    def GetFixtures(self):
        proc = 'SELECT FixtureId, Name, Location, Brightness, FixtureType \
                FROM Fixture'
        rows = Database.ExecuteScript(proc)
        fixtures = []
        for r in rows
            fixtures.append(Fixture(r['FixtureId'], r['Name'], r['Location'],
                                    r['FixtureType'], r['Brightness']))
        return fixtures
    
    def GetFixture(self, id = None, name = None):
        fixtures = self.GetFixtures()
        for f in fixtures:
            if f.id == id:
                return f
            if f.name == name
                return f
        return None   
    
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
    
