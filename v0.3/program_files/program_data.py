import math
import sys
import os

current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
sys.path.insert(0, parent_dir)
import Area_calculator_v0_3 as area_calc

def units_metric(unit):
	units = {f'q{unit}': 0, f'r{unit}': 1, f'y{unit}': 2, f'z{unit}': 3, f'a{unit}': 4, f'f{unit}': 5, f'p{unit}': 6, f'n{unit}': 7, f'μ{unit}': 8, f'm{unit}': 9, f'c{unit}': 10, f'd{unit}': 11, f'{unit}': 12, f'da{unit}': 13, f'h{unit}': 14, f'k{unit}': 15, f'M{unit}': 16, f'G{unit}': 17, f'T{unit}': 18, f'P{unit}': 19, f'E{unit}': 20, f'Z{unit}': 21, f'Y{unit}': 22, f'R{unit}': 23, f'Q{unit}': 24}
	return units

def units_imperial_distance():
	units = {'twip': 0, 'point (Imperial)': 1, 'point (Digital Standard)': 2, 'point (European Traditional)': 3, 'line/poppyseed': 4, 'pica (Imperial)': 5, 'pica (Digital Standard)': 6, 'barleycorn': 7, 'digit': 8, 'finger (cloth measure)': 9, 'finger (fingerbreadth)': 10, 'inch': 11, 'stick': 12, 'nail': 13, 'palm': 14, 'span': 15, 'link': 16, 'shaftment': 17, 'foot': 18, 'hand': 19, 'cubit': 20, 'pace': 21, 'yard': 22, 'ell': 23, 'grade/step': 24, 'fathom': 25, 'rope': 26, 'rod/pole/perch': 27, 'Ramsden\'s chain': 28, 'Gunter\'s chain': 29, 'shackle/shot': 30, 'furlong': 31, 'cable (British Admiralty)': 32, 'cable (US Navy)': 33, 'Roman mile': 34, 'mile': 35, 'nautical mile': 36, 'league': 37, 'AU': 38, 'ly': 39, 'pc': 40}
	return units

unit_table_metric = (10**30, 10**27, 10**24, 10**21, 10**18, 10**15, 10**12, 10**9, 10**6, 10**3, 10**2, 10, 1, 0.1, 10**-2, 10**-3, 10**-6, 10**-9, 10**-12, 10**-15, 10**-18, 10**-21, 10**-24, 10**-27, 10**-30)

unit_table_imperial_distance1 = (30856775814913673, 9460730472580800, 149597870700, 4828.032, 1852, 1609.344, 1480, 219.456, 185.3184, 201.168, 27.432, 20.1168, 30.48, 5.0292, 6.096, 1.8288, 0.762, 1.143, 0.9144, 0.762, 0.4572, 0.1016, 0.3048, 0.1524, 0.201168, 0.2286, 0.0762, 0.05715, 0.0508, 0.0254, 0.01905, 0.1143, 0.01905, 0.00846667, 0.0042333, 0.0042175176, 0.00211667, 0.0003759398, 0.0003527, 0.0003514598, 0.0000176389)
unit_table_imperial_distance2 = (56692.91, 2845.35, 2834.65, 2660, 472.4412, 237.11, 236.22, 118.11, 52.63, 8.7489, 52.49, 39.3700787, 19.685, 17.4978, 13.123, 4.374, 4.97096, 6.56168, 3.28084, 9.8425, 2.1872, 1.3123, 1.0936, 0.87489, 1.0936, 0.5468, 0.16404, 0.198838, 0.0328, 0.0497, 0.03645, 0.00497096, 0.005396, 0.0046, 0.0006757652, 0.000621, 0.00053996, 0.00020712, 6.6845871222684 * 10**-12, 1.057 * 10**-16, 3.2408 * 10**-17)


def unit_conversion(unit_input, unit_output, unit):
	if unit_input in units_metric(unit):
		conversion_from_unit_input = unit_table_metric[-(1 + units_metric(unit)[unit_input])]
	else:
		conversion_from_unit_input = unit_table_imperial_distance1[-(1 + units_imperial_distance()[unit_input])]

	if unit_output in units_metric(unit):
		conversion_to_unit_output = unit_table_metric[units_metric(unit)[unit_output]]
	else:
		conversion_to_unit_output = unit_table_imperial_distance2[units_imperial_distance()[unit_output]]

	print(conversion_from_unit_input * conversion_to_unit_output)
	return conversion_from_unit_input * conversion_to_unit_output



def area_rectangle(length, width, unit_length, unit_width, unit_final, unit = 'm'):
	length *= unit_conversion(unit_length, unit_final, unit)
	width *= unit_conversion(unit_width, unit_final, unit)

	area = length * width
	return area

def area_triangle(base, height, unit_base, unit_height, unit_final, unit = 'm'):
	base *= unit_conversion(unit_base, unit_final, unit)
	height *= unit_conversion(unit_height, unit_final, unit)

	area = base * height * 0.5
	return area

def area_ellipse(radius1, radius2, unit_radius1, unit_radius2, unit_final, unit = 'm'):
	radius1 *= unit_conversion(unit_radius1, unit_final, unit)
	radius2 *= unit_conversion(unit_radius2, unit_final, unit)

	area = math.pi * radius1 * radius2
	return area

def area_trapezoid(base1, base2, height, unit_base1, unit_base2, unit_height, unit_final, unit = 'm'):
	base1 *= unit_conversion(unit_base1, unit_final, unit)
	base2 *= unit_conversion(unit_base2, unit_final, unit)
	height *= unit_conversion(unit_height, unit_final, unit)

	area = (base1 + base2) * height * 0.5
	return area

def area_pentagon(length, unit_length, unit_final, unit = 'm'):
	length *= unit_conversion(unit_length, unit_final, unit)

	area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (length ** 2)
	return area

def area_hexagon(length, unit_length, unit_final, unit = 'm'):
	length *= unit_conversion(unit_length, unit_final, unit)

	area = 3 * math.sqrt(3) * 0.5 * (length ** 2)
	return area

def volume_cuboid(length, width, height_form, unit_length, unit_width, unit_height_form, unit_final, unit = 'm'):
	length *= unit_conversion(unit_length, unit_final, unit)
	width *= unit_conversion(unit_width, unit_final, unit)
	height_form *= unit_conversion(unit_height_form, unit_final, unit)

	volume = length * width * height_form
	return volume

def volume_ellipsoid(radius1, radius2, radius3, unit_radius1, unit_radius2, unit_radius3, unit_final, unit = 'm'):
	radius1 *= unit_conversion(unit_radius1, unit_final, unit)
	radius2 *= unit_conversion(unit_radius2, unit_final, unit)
	radius3 *= unit_conversion(unit_radius3, unit_final, unit)

	volume = 4 * math.pi * radius1 * radius2 * radius3 / 3
	return volume

def volume_cylinder(radius1, radius2, height_form, unit_radius1, unit_radius2, unit_height_form, unit_final, unit = 'm'):
	radius1 *= unit_conversion(unit_radius1, unit_final, unit)
	radius2 *= unit_conversion(unit_radius2, unit_final, unit)
	height_form *= unit_conversion(unit_height_form, unit_final, unit)

	volume = math.pi * radius1 * radius2 * height_form
	return volume

def volume_pyramid(pyr_base, height_form, unit_pyr_base, unit_height_form, unit_final, unit = 'm'):
	pyr_base *= unit_conversion(unit_pyr_base, unit_final, unit)
	height_form *= unit_conversion(unit_height_form, unit_final, unit)

	volume = pyr_base * height_form / 3
	return volume