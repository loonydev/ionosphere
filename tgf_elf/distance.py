from __future__ import division
from __future__ import print_function
from numpy import pi,cos,arcsin,sqrt


class Distance_Class(object):
    # R - rasius of Earth
    CONST_R = 6372795
    # P = pi/180
    CONST_P = pi/180

    def __init__(self,lat1,lon1,lat2,lon2):
        self.lat1 = lat1
        self.lat2 = lat2
        self.lon1 = lon1
        self.lon2 = lon2

    def distance(self):
        a = 0.5 - cos((self.lat2 - self.lat1)*self.CONST_P)/2 + \
            cos(self.lat1*self.CONST_P)*cos(self.lat2*self.CONST_P)* \
            (1 - cos((self.lon2 - self.lon1)*self.CONST_P))/2
        return 2*self.CONST_R*arcsin(sqrt(a))

if __name__ == '__main__':
    # latitude  N +, S -
    # longitude E +, W -

    lat1 = -12.43
    lon1 = 159.7

    lat2 = 49.19
    lon2 = 22.55

    distance_class = Distance_Class(lat1=lat1,lon1=lon1,lat2=lat2,lon2=lon2)
    res = distance_class.distance()

    print ('r =',res/1000,'km')
    print ('excpect 14370 km')
