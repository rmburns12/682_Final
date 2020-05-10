# GEOG682 Final Project
## Washington, DC Gun Crime Analysis Mapping
Rob Burns

4/28/2020


##Introduction


##Analysis

      This analysis made use of 3 datasets made available by the Washington, DC Office of the Chief Technology Officer as shapefiles on the "Open Data DC" website (https://opendata.dc.gov/):

      - "Shot Spotter Gun Shots": A point layer showing the locations of gun shots in DC detected by the DC Metropolitan Police                 Department (MPD) Shot Spotter sensor network.
      - "Ward from 2012": A polygon layer representing the boundaries of DC's 2012 election wards.
      - "Crime Incidents in 2017": A point layer representing the locations and attributes of crime incidents reported in the ASAP               (Analytical Services Application) by the DC MPD in 2017.
      
      The first map provides an analysis of the number of gun crimes committed per 10,000 people in 2017 in each DC ward. This map was created manually within the QGIS 3.4.9 program, using some of the tools and functions within the program to perform the various analysis steps. First, I filtered out only the gun crimes from the "Crime_Incidents_in_2017" layer, within the Query Builder setting the field "METHOD" as equal to the value "GUN". This gave us a point layer of only the gun crime incidents in 2017, which I named "Gun_Crime_Incidents_2017". Next I used the "Count Points In Polygon" vector analysis to count the number of gun crime incident points in each ward polygon, counting the number of points from "Gun_Crime_Incidents_2017" within the different polygons from the "Ward_From_2012" layer. The output of this was a new layer named "Count" which contained a field called "GUN_CRIME_INCIDENTS" giving the number of points within each ward poygon. Then, using the "Field Calculator" tool within the Ptocessing Toolbox I used the "Count" layer to create a new attribute field called "GUN_CRIME_PER_10000" using the expression "GUN_CRIME_INCIDENTS /  ( POP_2010 / 10000)". Using the "Symbology" tab I categorized each of the ward polygons into a separate color based on the "WARD" field to show which ward was which. I labeled each ward with the numeric value of the "GUN_CRIME_PER_10000" field to show the number of gun crimes oer 10,000 residents of each ward. Finally, I used the Print Layout function to add in all of the necessary map components. The resulting map is pictured below.
      






