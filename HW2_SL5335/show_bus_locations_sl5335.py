
# coding: utf-8

# In[1]:

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


# In[2]:
key = sys.argv[1]
buslineref = sys.argv[2]

def show_bus_locations_sl5335(key, buslineref):
    
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
    buses = get_jsonparsed_data(url)
    with open ("Buses.json", "w") as f:
        json.dump(buses, f)
        
    numberofbuses = len(buses['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    my_buses = buses['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


    
    print ("Bus Line: " + buslineref)
    print ("Number of Active Buses: " + str(numberofbuses))
    for x in range(numberofbuses):
        vehiclelocate = my_buses[x]['MonitoredVehicleJourney']['VehicleLocation']
        print ("Bus number %i is at %f latitude and %f longitude." % (x, vehiclelocate['Latitude'], vehiclelocate['Longitude']))
        
show_bus_locations_sl5335(key, buslineref)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



