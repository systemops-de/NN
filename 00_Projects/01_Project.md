# Project 1

create an application (Functional, OOP, modules) which reads the current weatch from owm for several cities (ex: berlin, aachen, bonn)
and store the information in sqlite DB. API Key should be extern in a JSON file (not in code) as well as lang and unit.

you bests:
- Documentation
- PEP8
- Modules


## OWM Information

1. Temperature
2. Min Temperature
3. Max Temperature


## DB Record should have the following information
0. Curennt Date
0. city
1. Temperature
1. Min Temperature
2. Max Temperature

## DB Design
1. Table cities: with all required cities and also a column of (active/inactive)
2. Table weather

Check if the request already done for today and if there are records already stored in DB, then ask the user 
1. to delete the old record and insert the new records
2. to keep the old records and ignore the new responsed data



