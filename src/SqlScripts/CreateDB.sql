PRAGMA foreign_keys = on;

CREATE TABLE Fixture
    (FixtureId      INT PRIMARY KEY NOT NULL AUTOINCREMENT,
    Name            VARCHAR(50)     NOT NULL,
    Location        VARCHAR(5)      NOT NULL,
    Brightness      INT             NOT NULL,
    FixtureType     INT             NOT NULL);
    
CREATE TABLE Preset
    (PresetId       INT PRIMARY KEY NOT NULL AUTOINCREMENT,
    Name            VARCHAR(50)     NOT NULL);

CREATE TABLE FixturePresetAssoc
    (FixturePresetAssocId INT PRIMARY KEY NOT NULL AUTOINCREMENT,
    FixtureId       INT NOT NULL,
    PresetId        INT NOT NULL,
    FOREIGN KEY(FixtureId) REFERENCES Fixture(FixtureId)
    FOREIGN KEY(PresetId) REFERENCES Preset(PresetId) );

CREATE TABLE Schedule
    (ScheduleId     INT PRIMARY KEY NOT NULL AUTOINCREMENT,
    Name            VARCHAR(50) NOT NULL,
    Days            VARCHAR(250) NOT NULL,
    Times           VARCHAR(250) NOT NULL,
    Active          BOOL NOT NULL );
    
CREATE TABLE PresetScheduleAssoc
    (PresetScheduleAssocId   INT PRIMARY KEY NOT NULL AUTOINCREMENT,
    PresetId        INT NOT NULL,
    ScheduleId      INT NOT NULL,
    FOREIGN KEY (PresetId) REFERENCES Preset(Preset),
    FOREIGN KEY (ScheduleId) REFERENCES Schedule(ScheduleId) );
    
CREATE TABLE User
    (UserId         INT PRIMARY KEY NOT NULL AUTOINCREMENT,
    FirstName       VARCHAR(50) NOT NULL,
    LastName        VARCHAR(50) NOT NULL, 
    UserName        VARCHAR(50) NOT NULL,
    Password        VARCHAR(50) NOT NULL );