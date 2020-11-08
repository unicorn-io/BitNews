# import package for extracting information on the ip addres
import ipinfo
import math
import gmplot

ACCESS_TOKEN = "5e25582731ecec"
request_handler = ipinfo.getHandler(ACCESS_TOKEN)

# function to retrieve the Latitude and Longitude from an IP Address
def get_lat_long(ip_address):
    details = request_handler.getDetails(ip_address)
    return [details.latitude, details.longitude]

# Function to calculate the distance between two points
def get_dist(lat1, lat2, lon1, lon2):
    '''
    Haversine Formula: Formula to calulate the great-circle distance between two points - that is
    , the shortest distance over the earth's surface - giving an 'as-the-crow-flies' distance b/w
    the points (ignoring any hills they fly over, of course!)

    Haversine
    formula: 	a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    where 	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
    note that angles need to be in radians to pass to trig functions!
    '''
    R = 6371e3
    phi1 = lat1 * math.pi/180
    phi2 = lat2 * math.pi/180
    del_phi = (lat2-lat1) * math.pi/180
    del_lambda = (lon2-lon1) * math.pi/180

    a = math.sin(del_phi/2) * math.sin(del_phi/2) + math.cos(phi1) * math.cos(phi2) * math.sin(del_lambda/2) * math.sin(del_lambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R*c # distance in meters
    return d

def dist_bw_ip(ip1, ip2):
    [a, b] = get_lat_long(ip1)
    [c, d] = get_lat_long(ip2)    
    print(get_dist(float(a), float(c), float(b), float(d)))

def get_plot_html(lat_list, long_list, path=""):
    gmap3 = gmplot.GoogleMapPlotter(lat_list[0], 
                                long_list[0], 13) 
  
    # scatter method of map object  
    # scatter points on the google map s
    gmap3.scatter( lat_list, long_list, '# FF0000', 
                                size = 40, marker = False ) 
    
    # Plot method Draw a line in 
    # between given coordinates 
    gmap3.plot(lat_list, long_list,  
            'cornflowerblue', edge_width = 2.5) 
    
    gmap3.draw( "map.html" ) 
