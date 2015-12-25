/* ************************
*
* ModifyFixture
* 
* Created Dec 24, 2015
* Josh Harmon
*
* PARAMETERS: 
* &id&
*
* ************************ */

DELETE FROM 
    Fixture f
WHERE
    f.Id = &id&;