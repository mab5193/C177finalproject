Pseudocode:

##Webscraping threatened felidae species data

#curl felidae database from http://www.iucnredlist.org onto a file
#get species name, status, population trend:
    #find div for species name
    #species_name= div1
    #find div for status
    #status= div2
    #find div for population trend
    #pop_trend = div3
    #print species_name + status + pop_trend and trim extra spaces
#save onto felidae data file
         
 #Open felidae data file 
     #get threatlevels: 
         #sort by (NE, DD, LC, NT, VU, EN, CR, EW, EX)
             #return threatlevels
             #save threatlevels onto threatlevels.txt

 #Open threatlevels.txt
     #count (LC)
         #return
     #count (NT)
     #count (VU)
     #count (EN)
     #count (CR)
     #count (EW)
     #return count
     #save count

#Open felidae data file
    #Get causesofthreat:
        #sort by alphabet
            #return causesofthreat
                #save causesofthreat onto causesofthreat.txt

#Open felidae data file
    #get population trend:
        #find "stable" > save onto stablespecies.txt
        #find "decreasing" > save onto decreasingspecies.txt
        #find "unknown" > save onto unknownspecies.txt

#Open ourdata file

##Plotting species on a map

#import map
#import matplotlib
#import numpy
#define base map by lat, lon, resolution
#draw coastlines
#draw countries
#fill continents by different colors
#draw boundaries
#plot species points
#assign labels to points
#show map