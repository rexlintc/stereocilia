# Prints curvature of actin filaments

def curvature(m1, m2):
	"""
	returns the curvature between two atoms (m1, m2)
	"""
	m1_x = m1.xyz()[0] # x coordinate
	m1_y = m1.xyz()[1] # y coordinate
	m2_x = m2.xyz()[0]
	m2_y = m2.xyz()[1]

	# deviation along the x axis
	delta_x = m2_x - m1_x # positive delta x corresponds to deviation towards positive x
	delta_y = abs(m2_y - m1_y)
	curvature = delta_x/delta_y
	return curvature

from VolumePath import markerset

links = markerset.selected_links()

# 6 links 7 markers
for i in range(0, len(links), 6):
	filament_data = []
	for j in range(i, i+6):
		m1 = links[j].marker1
		m2 = links[j].marker2
		link_curvature = curvature(m1, m2)
		filament_data.append(link_curvature)

	# deviation along the x axis
	print('%8.4g %8.4g %8.4g %8.4g %8.4g %8.4g' % (filament_data[0], filament_data[1], filament_data[2], filament_data[3], filament_data[4], filament_data[5]))