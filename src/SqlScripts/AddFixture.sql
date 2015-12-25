/* ************************
*
* AddFixture
* 
* Created Dec 11, 2015
* Josh Harmon
*
* PARAMETERS: 
* &name&
* &location&
* &fixtureType&
* &brightness&
*
* ************************ */

INSERT INTO
    Fixture (Name, Location, FixtureType, Brightness)
VALUES
    (&name&, &location&, &fixtureType&, &brightness&);
