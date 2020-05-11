#GEOG682 Final
#Rob Burns
#5/3/2020

#Part 1: Load and display 3 datasets
Districtpath = "S:/682/Spring20/rburns12/Final/Data/Ward_from_2012.shp"
DCdistricts = iface.addVectorLayer(Districtpath, "DCdistricts", "ogr")
Crimepath = "S:/682/Spring20/rburns12/Final/Data/Crime_Incidents_in_2017.shp"
Crime = iface.addVectorLayer(Crimepath, "GunCrime", "ogr")
Shotpath = "S:/682/Spring20/rburns12/Final/Data/Shot_Spotter_Gun_Shots.shp"
ShotsSpot = iface.addVectorLayer(Shotpath, "ShotsSpot", "ogr")

#Part 2: Automatically calculate the number of gun crimes committed per 10,000 people in 2017 in each ward

#First we filter out only the gun crimes in each ward.
processing.run("qgis:extractbyattribute",{ 'FIELD' : 'METHOD', 'INPUT' : 'S:/682/Spring20/rburns12/Final/Data/Crime_Incidents_in_2017.shp', 'OPERATOR' : 0, 'OUTPUT' : 'S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_2017.shp', 'VALUE' : 'GUN' })
#Next we create a count of all of the gun crime incidents within each ward.
processing.run("qgis:countpointsinpolygon",{ 'CLASSFIELD' : None, 'FIELD' : 'GUNINCIDENTS', 'OUTPUT' : 'S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_2017_per_Ward.shp', 'POINTS' : 'S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_2017.shp', 'POLYGONS' : 'S:/682/Spring20/rburns12/Final/Data/Ward_from_2012.shp', 'WEIGHT' : None })
Path1= "S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_2017_Per_Ward.shp"
GunCrimePerWard = iface.addVectorLayer(Path1, "GunCrimePerWard", "ogr")
#Then we calculate the number of gun crimes in each ward per each 10,000 residents in the ward in 2010.
processing.run("qgis:advancedpythonfieldcalculator",{ 'FIELD_LENGTH' : 10, 'FIELD_NAME' : 'GunCrimePer10K', 'FIELD_PRECISION' : 3, 'FIELD_TYPE' : 0, 'FORMULA' : 'value = <GUNINCIDEN> /(<POP_2010>/10000)', 'GLOBAL' : '', 'INPUT' : 'S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_2017_Per_Ward.shp', 'OUTPUT' : 'S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_Per_10k.shp' })
GunGrimePer10K = iface.addVectorLayer('S:/682/Spring20/rburns12/Final/Data/Gun_Crimes_Per_10k.shp', "GunCrimePer10K", "ogr")
#Finally, we will print our calculation for gun crimes per 10,000 residents in each ward.
#This command will print first the ward number (left), then the number of gun crimes per 10,000 people (right).
print("Gun Crime Incidents per 10,000 Residents in each DC Ward in 2017")
lyr = iface.activeLayer()
features = lyr.getFeatures()
for ft in features:print(ft["Ward"],ft["GunCrimePe"])

#The number of gun crimes per 10,000 people for each ward are as follows:
#Ward 1: 15
#Ward 2: 7
#Ward 3: 3
#Ward 4: 17
#Ward 5: 36
#Ward 6: 21
#Ward 7: 58
#Ward 8: 58

#Part 3: Automatically calculate the shooting incidents detected by ShotSpotter per 10,000 people in 2017 in each ward.

#Count the number of shots detected in each ward.
processing.run("qgis:countpointsinpolygon",{ 'CLASSFIELD' : None, 'FIELD' : 'Shots_Spot', 'OUTPUT' : 'S:/682/Spring20/rburns12/Final/Data/Shots_Spotted_per_Ward.shp', 'POINTS' : 'S:/682/Spring20/rburns12/Final/Data/Shot_Spotter_Gun_Shots.shp', 'POLYGONS' : 'S:/682/Spring20/rburns12/Final/Data/Ward_from_2012.shp', 'WEIGHT' : None })
#Then we calculate the number of gun shots in each ward per each 10,000 residents in the ward in 2010.
processing.run("qgis:advancedpythonfieldcalculator",{ 'FIELD_LENGTH' : 10, 'FIELD_NAME' : 'ShotsPer10K', 'FIELD_PRECISION' : 3, 'FIELD_TYPE' : 0, 'FORMULA' : 'value = <Shots_Spot> /(<POP_2010>/10000)', 'GLOBAL' : '', 'INPUT' : 'S:/682/Spring20/rburns12/Final/Data/Shots_Spotted_per_Ward.shp', 'OUTPUT' : 'S:/682/Spring20/rburns12/Final/Data/Shots_Per_10k.shp'})
ShotsPer10K = iface.addVectorLayer('S:/682/Spring20/rburns12/Final/Data/Shots_Per_10k.shp', "ShotsPer10K", "ogr")
#Finally, we will print our calculation for shots per 10,000 residents in each ward.
#This command will print first the ward number (left), then the number of shots per 10,000 people (right).
print("Shots detected by ShotSpotter per 10,000 Residents in each DC Ward in 2017")
lyr = iface.activeLayer()
features = lyr.getFeatures()
for ft in features:print(ft["Ward"],ft["ShotsPer10"])

#The number of shots per 10,000 people for each ward are as follows:
#Ward 1: 210
#Ward 2: 7
#Ward 3: 0
#Ward 4: 365
#Ward 5: 521
#Ward 6: 299
#Ward 7: 1352
#Ward 8: 1773


