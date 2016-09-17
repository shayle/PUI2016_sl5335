
# coding: utf-8

# In[2]:

from __future__ import print_function
import os
import sys
import json
import csv
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

key = sys.argv[1]
buslineref = sys.argv[2]
buslinecsv = sys.argv[3]


# In[ ]:

def get_bus_info(key, buslineref, buslinecsv):

    def get_jsonparsed_data(url):   
        response = urllib.urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)
    """
    from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """

    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + buslineref
    buses_parsed = get_jsonparsed_data(url)
    buses = buses_parsed['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    def get_latitude(buses): 
        latitude = []
        for bus in buses:
            latitude.append(bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
        return latitude

    def get_longitude(buses): 
        longitude = []
        for bus in buses:
            longitude.append(bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        return longitude

    def get_stop(buses):
        stop = []
        for bus in buses:
            if bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'] == '':
                stop.append('N/A')
            else: 
                stop.append(bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        return stop

    def get_presentable_distance(buses):
        present_dist = []
        for bus in buses:
            if bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] == '':
                present_dist.append('N/A')
            else: 
                present_dist.append(bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
        return present_dist
    
    latitude = get_latitude(buses)
    longitude = get_longitude(buses)
    stop = get_stop(buses)
    stop_status = get_presentable_distance(buses)
    
    results = pd.DataFrame({
        'latitude': latitude,
        'longitude': longitude,
        'stop': stop,
        'stop status': stop_status
    })
    
    
    results.to_csv(buslinecsv, index=False)
    


# In[ ]:

get_bus_info(key, buslineref, buslinecsv)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



