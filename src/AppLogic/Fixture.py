'''
Created on Dec 3, 2015

@author: jharm
'''
class FixtureManager():
    __Fixtures = {}
    
    @classmethod
    def Add(cls, fixture):
        cls.__Fixtures.append(fixture)

    @classmethod
    def Remove(cls, fixture):
        try:
            cls.__Fixtures.remove(fixture)
            return True
        except:
            return False
        
    @classmethod
    def GetFixtures(cls):
        return cls.__Fixtures
    
    @classmethod
    def GetFixture(cls, id):
        fixture = cls.__Fixtures[id]
        return fixture
        
    
class FixtureType():
        Blank = 1
        Light = 2
        DimmableLight = 3
        ColoredLight = 4

class Fixture():
    
    def __init__(self, name, location, fixtureType, brightness):
        self.Name = name
        self.Location = location
        self.FixtureType = fixtureType
        self.Brightness = brightness
        
    def ToDictionary(self):
        return {'name' : self.Name,
                'location' : self.Location,
                'fixtureType' : self.FixtureType,
                'brightness' : self.Brightness}
    
