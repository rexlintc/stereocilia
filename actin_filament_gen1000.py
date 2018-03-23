#Code template to create invidual market sets and label them by color

lattice_spacing = 100	# Distance between parallel actin filaments, Angstroms.
actin_length = 1000		# Actin length in Angstroms.

from math import sqrt
plane_spacing = sqrt(3)/2 * lattice_spacing

radius = 30		# Radius of cylinder depicting actin filament, Angstroms.

# Colors
color1 = (1,1,.5,1)	# Light yellow. (red, green, blue, opacity) 0-1 scale
color2 = (.5,.5,1,1)	# Light blue.
color3 = (1,0,0,1)	#Red
color4 = (0,1,0,1)	#Green
color5 = (1,0,1,1)	#Purple
color6 = (1,1,0,1)	
color7 = (0.5,0.5,0.5,1)	

from VolumePath import Marker_Set, Marker, Link   #this is to import the module for Chimera
mset = Marker_Set('Actin Filament 01')  #defining the name of the marker set


# Marker(marker_set_name, id_number, (y_coordinate, x_coorinate, Z_coordinate), color, radius)


# m1_(filament_number)

# One actin filament with two colors.

# This is first segment in YELLOW. This is the origin.
m1_0 = Marker(mset, 0, (0,0,0), color2, radius)
m2_0 = Marker(mset, 1, (0,0,actin_length), color2, radius)
Link(m1_0, m2_0, color1, radius)    #link the first segment


