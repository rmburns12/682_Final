# GEOG682 Final Project
## Washington, DC Gun Crime Analysis Mapping
Rob Burns

4/28/2020


## Introduction


## Analysis

 This analysis made use of 3 datasets made available by the Washington, DC Office of the Chief Technology Officer as shapefiles on 
 the "Open Data DC" website (https://opendata.dc.gov/):

 1) "Shot Spotter Gun Shots": A point layer showing the locations of gun shots in DC detected by the DC Metropolitan Police   
 Department (MPD) Shot Spotter sensor network.
 2) "Ward from 2012": A polygon layer representing the boundaries of DC's 2012 election wards.
 3) "Crime Incidents in 2017": A point layer representing the locations and attributes of crime incidents reported in
 ASAP (Analytical Services Application) by the DC MPD in 2017.
      
The first map provides an analysis of the number of gun crimes committed per 10,000 people in 2017 for each DC ward. This map was 
created manually within QGIS 3.4.9, using some of the tools and functions within the program to perform the various analysis 
steps. First, I filtered out only the gun crimes from the "Crime_Incidents_in_2017" layer, within the Query Builder setting the field 
"METHOD" as equal to the value "GUN". This gave us a point layer of only the gun crime incidents in 2017 which I named 
"Gun_Crime_Incidents_2017". Next I used the "Count Points In Polygon" vector analysis tool to count the number of gun crime incident 
points in each ward polygon, counting the number of points from "Gun_Crime_Incidents_2017" within the different polygons from the 
"Ward_From_2012" layer. The output of this was a new layer named "Count" which contained a field called "GUN_CRIME_INCIDENTS" which gave 
the number of points within each ward poygon. Then, using the "Field Calculator" tool within the Processing Toolbox I ran an expression 
on the "Count" layer dividing the number of gun crime incidents by the 2010 population of each ward divided by 10,000 
("GUN_CRIME_INCIDENTS /  ( POP_2010 / 10000)"). The result was a new attribute field called "GUN_CRIME_PER_10000". Using 
the "Symbology" tab I categorized each of the ward polygons into a separate color based on the "WARD" field to differentiate the wards 
from each other. I labeled each ward with the numeric value of the "GUN_CRIME_PER_10000" field to show the number of gun crimes per 
10,000 residents of each ward. Finally, I used the Print Layout window to add in all of the necessary map components. The resulting map 
is pictured below.

The second map is an analysis of the number of shots detected by Shot Spotter per 10,000 people in 2017 for each ward, also done
manually in QGIS 3.4.9. No filtering was required for this layer since it already only displayed the relevant points captured by Shot 
Spotter. I started this processing by using the "Count Points In Polygon" function, using "Shot_Spotter_Gun_Shots" as the point layer 
and "Ward_From_2012" as the polygon layer. The output was a new layer called "Shot Count" containing a field called "SHOT_SPOTS" which 
gave the number of gun shots detected in each ward. Next I used the "Field Calculator" tool on the "Shot Count" layer to determine the 
number of shots detected per 10,000 people in each ward. Within the "Field Calculator" I ran an expression to divide the number of shots 
detected in each ward by the 2010 population in each ward divided by 10,000 ("SHOT_SPOTS /  ( POP_2010 / 10000)"). The output was a new
attribute field called "SHOTS_SPOT_PER_10000". Using the “Symbology” tab I categorized each of the ward polygons into a separate color 
based on the "WARD" field to show which ward was which. I labeled each ward with the value of the "SHOTS_SPOT_PER_10000" field to give 
the number of shots detected per 10,000 people in each ward. As with the previous map I used the Print Layout window to add in all of 
the necessary map components in order to fully complete the map. The resulting map is pictured below.

      
