/* ************************
*
* GetPreset
* 
* Created Dec 7, 2015
* Josh Harmon
*
* PARAMETERS: 
* &id&
* &name&
*
* ************************ */

SELECT
    p.PresetId,
    p.Name
FROM
    Preset p
WHERE
    (p.PresetId = &id& OR &id& IS NULL) 
    AND (p.Name = &name& or &name& IS NULL);