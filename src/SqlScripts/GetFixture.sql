/* ************************
*
* GetFixture
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

SELECT
    f.FixtureId, 
    f.Name,
    f.Location,
    f.FixtureType,
    f.Brightness
FROM
    Fixture f
WHERE
    (f.FixtureId = &id& OR &id& IS NULL) 
    AND (f.Name = &name& or &name& IS NULL)
    AND (f.Location = &location& or &location& IS NULL)
    AND (f.Brightness = &brightness& or &brightness& IS NULL)
    AND (f.FixtureType = &fixtureType& or &fixtureType& IS NULL); 
