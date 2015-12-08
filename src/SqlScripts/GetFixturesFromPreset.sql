/* ************************
*
* GetFixturesFromPreset
* 
* Created Dec 7, 2015
* Josh Harmon
*
* PARAMETERS: 
* &id&
*
* ************************ */

SELECT
    f.FixtureId,
    f.Name,
    f.Location,
    f.Brightness,
    f.FixtureType
FROM
    Preset p
    INNER JOIN FixturePresetAssoc fpa ON fpa.PresetId = p.PresetId
    INNER JOIN Fixture f ON fpa.FixtureId = f.FixtureId
WHERE
    (p.PresetId = &id& OR &id& IS NULL)