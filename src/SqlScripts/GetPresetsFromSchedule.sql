/* ************************
*
* GetPresetsFromSchedule
* 
* Created Dec 7, 2015
* Josh Harmon
*
* PARAMETERS: 
* &id&
*
* ************************ */

SELECT
    p.PresetId,
    p.Name
FROM
    Schedule s
    INNER JOIN PresetScheduleAssoc psa ON psa.ScheduleId = s.ScheduleId
    INNER JOIN Preset p ON fpa.PresetId = p.PresetId
WHERE
    (s.ScheduleId = &id& OR &id& IS NULL)