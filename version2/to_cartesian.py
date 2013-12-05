import math

def to_cartesian(theta, phi, r):
    '''Converts spherical or cylindrical coordinates to cartesian ones. Angles in radians.'''
	x = math.cos(theta)*math.sin(phi)*r
    y = math.sin(theta)*math.sin(phi)*r
    z = math.cos(phi)*r

    return(x,y,z)