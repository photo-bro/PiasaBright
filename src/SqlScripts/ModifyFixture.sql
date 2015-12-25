/* ************************
*
* ModifyFixture
* 
* Created Dec 7, 2015
* Josh Harmon
*
* PARAMETERS: 
* &id&
* &name&
* &location&
* &fixtureType&
* &brightness&
*
* ************************ */

UPDATE 
    Fixture f
SET
    f.Name = CASE WHEN &name& = NULL THEN f.Name
                   ELSE &name& END,
    f.Location = CASE WHEN &location& = NULL THEN f.Location
                   ELSE &location& END,
    f.FixtureType = CASE WHEN &fixtureType& = NULL THEN f.FixtureType
                   ELSE &fixtureType& END,
    f.Brightness = CASE WHEN &brightness& = NULL THEN f.Brightness
                   ELSE &brightness& END
WHERE
    f.Id = &id&;