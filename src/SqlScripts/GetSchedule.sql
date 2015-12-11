/* ************************
*
* GetSchedule
* 
* Created Dec 7, 2015
* Josh Harmon
*
* PARAMETERS: 
* &id&
* &name&
* &days&
* &times&
* &active&
*
* ************************ */

SELECT
    s.ScheduleId,
    s.Name,
    s.Days,
    s.Times,
    s.Active
FROM
    Schedule s
WHERE
    (s.ScheduleId = &id& OR &id& IS NULL) 
    AND (s.Name = &name& or &name& IS NULL)
    AND (s.Days = &days& or &days& IS NULL)
    AND (s.Times = &times& or &times& IS NULL)
    AND (s.Active = &active& or &active& IS NULL);