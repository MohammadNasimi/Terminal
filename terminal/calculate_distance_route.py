from math import *
def calculate_distance(begin,destination):
    begin=begin.split(':')
    destination=destination.split(':')

    # The math module contains a function named 
    # radians which converts from degrees to radians. 
    lon1 = radians(float(begin[0])) 
    lon2 = radians(float(begin[1])) 
    lat1 = radians(float(destination[0])) 
    lat2 = radians(float(destination[1]))

    
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))  
    
    # Radius of earth in kilometers. Use 3956 for miles 
    r = 6371
    
    # calculate the result 
    return round(c * r,0) 

