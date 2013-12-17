import math

def to_cartesian(theta, phi, r):
    '''Converts spherical or cylindrical coordinates to cartesian ones. Angles in radians.

    theta: Angle in the xy plane
    phi: Angle from z-axis
    r: radius

    return: tuple representing position in (x,y,z) format
    '''
	x = math.cos(theta)*math.sin(phi)*r
    y = math.sin(theta)*math.sin(phi)*r
    z = math.cos(phi)*r

    return(x,y,z)