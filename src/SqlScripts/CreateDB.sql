PRAGMA foreign_keys = on;

CREATE TABLE Fixture
    (FixtureId      INTEGER PRIMARY KEY AUTOINCREMENT,
    Name            VARCHAR(50)     NOT NULL,
    Location        VARCHAR(5)      NOT NULL,
    Brightness      INTEGER         NOT NULL,
    FixtureType     INTEGER         NOT NULL);
    
CREATE TABLE Preset
    (PresetId       INTEGER PRIMARY KEY AUTOINCREMENT,
    Name            VARCHAR(50)     NOT NULL);

CREATE TABLE FixturePresetAssoc
    (FixturePresetAssocId INTEGER PRIMARY KEY AUTOINCREMENT,
    FixtureId       INTEGER NOT NULL,
    PresetId        INTEGER NOT NULL,
    FOREIGN KEY(FixtureId) REFERENCES Fixture(FixtureId)
    FOREIGN KEY(PresetId) REFERENCES Preset(PresetId) );

CREATE TABLE Schedule
    (ScheduleId     INTEGER PRIMARY KEY AUTOINCREMENT,
    Name            VARCHAR(50) NOT NULL,
    Days            VARCHAR(250) NOT NULL,
    Times           VARCHAR(250) NOT NULL,
    Active          BOOL NOT NULL );
    
CREATE TABLE PresetScheduleAssoc
    (PresetScheduleAssocId   INTEGER PRIMARY KEY AUTOINCREMENT,
    PresetId        INTEGER NOT NULL,
    ScheduleId      INTEGER NOT NULL,
    FOREIGN KEY (PresetId) REFERENCES Preset(Preset),
    FOREIGN KEY (ScheduleId) REFERENCES Schedule(ScheduleId) );
    
CREATE TABLE User
    (UserId         INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName       VARCHAR(50) NOT NULL,
    LastName        VARCHAR(50) NOT NULL, 
    UserName        VARCHAR(50) NOT NULL,
    Password        VARCHAR(50) NOT NULL );