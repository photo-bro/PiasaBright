


class FixtureType():
        Blank = 1
        Light = 2
        DimmableLight = 3
        ColoredLight = 4

class Fixture():
    
    def __init__(self):
        self.Name = ""
        self.Location = ""
        self.FixtureType = FixtureType.Blank
        self.Brightness = 0
        
    def Setup(self, name, location, fixtureType, brightness):
        self.Name = name
        self.Location = location
        self.FixtureType = fixtureType
        self.Brightness = brightness
