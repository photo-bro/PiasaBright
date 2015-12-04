class Preset():
    
    def __init__(self):
        self.Name = ""
        self.Fixtures = []
        
    def AddFixture(self, fixture):
        self.Fixtures.append(fixture)
    
    def RemoveFixture(self, fixture):
        self.Fixtures.remove(fixture)
    
    