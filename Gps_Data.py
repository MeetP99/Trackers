'''
-> Project definiton : GPS tracking system using Raspberry pi
-> subject : Emerging Capstone Project 
-> Team name : Trackers
-> Team number: 20
-> Team Member: Patel Meet Sanjaykumar(8765458)
                Mehta Parth Sanjaybhai(8725788)
				Aviya Janki Ashokbhai(8719638) 
-> Date : 30/05/2022
-> Submitted to : Amrinder Singh Ghotra 

'''

import gps    # Importing the gps module in python
import time   # Importing the Time module in python
session = gps.gps("127.0.0.1", "2947") 
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    try:
	time.sleep(0.5)
        raw_data = session.next()                # tranfering raw data into variable  
	if raw_data['class'] == 'TPV':       
		if hasattr(raw_data, 'lat'):
        		print "Latitude is = "+str(raw_data.lat)           # printing the Latitude value from NMEA data 
	if raw_data['class'] == 'TPV':
		if hasattr(raw_data,'lon'):
			print "Longitude is = "+str(raw_data.lon)              # printing the Longitude value from NMEA data 
	if raw_data['class'] =='TPV':
		if hasattr(raw_data,'speed'):
			print "Vehicle is moving at = "+str(raw_data.speed)+" KPH"     # printing the Speed  value from NMEA data 
	if raw_data['class'] =='TPV':
		if hasattr(raw_data,'alt'):
			print "The altitude is = "+str(raw_data.alt)+" m"      # printing the Altitude  value from NMEA data 
	if raw_data['class'] == 'TPV':
		if hasattr(raw_data,'time'):
			print "The current date and time is = "+str(raw_data.time)+"\n"    # printing the Date and time  from NMEA data 
		
    except KeyError:    # error handlers
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "No incoming data from the GPS module"
