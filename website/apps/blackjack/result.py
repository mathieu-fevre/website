from utils import compare, initial_deck2

print(compare('T2', '3', '-', 'H', 10000000, initial_deck2))
(-25.44778, -23.13322)
'temps total': 224

print(compare('T2', '4', '-', 'H', 10000000, initial_deck2))
(-21.13734, -21.04396)
'temps total': 217

print(compare('T2', '5', '-', 'H', 10000000, initial_deck2))
(-16.35954, -18.86291)
'temps total': 219

print(compare('T2', '6', '-', 'H', 10000000, initial_deck2))
(-15.49702, -16.88194)
'temps total': 191

print(compare('A7', '2', '-', 'D', 10000000, initial_deck2))
(12.45472, 12.11238)
'temps total': 212

print(compare('A4', '4', 'H', 'D', 10000000, initial_deck2))
(5.96427, 6.34692)
'temps total': 263

print(compare('A2', '5', 'H', 'D', 10000000, initial_deck2))
(13.34882, 13.87706)
'temps total': 250

print(compare('A2', '6', 'H', 'D', 10000000, initial_deck2))
(15.99045, 18.7667)
'temps total': 246

print(compare('54', '3', 'H', 'D', 10000000, initial_deck2))
(10.70734, 13.27676)
'temps total': 250

print(compare('44', '4', 'H', 'S', 10000000, initial_deck2))
(4.68805, -1.85665)
'temps total': 338

print(compare('44', '5', 'H', 'S', 10000000, initial_deck2))
(8.07285, 8.22973)
'temps total': 345

print(compare('44', '6', 'H', 'S', 10000000, initial_deck2))
(12.25988, 13.93653)
'temps total': 331

print(compare('33', '2', 'H', 'S', 10000000, initial_deck2))
(-14.21406, -17.66871)
'temps total': 352

print(compare('33', '3', 'H', 'S', 10000000, initial_deck2))
(-10.82053, -8.72201)
'temps total': 366

print(compare('T3', '2', 'H', '-', 10000000, initial_deck2))
(-30.76101, -29.55882)
'temps total': 228

print(compare('T6', 'T', 'H', '-', 10000000, initial_deck2))
(-57.09678, -57.66748)
'temps total': 161

#############

print(compare('A3', '4', 'H', 'D', 10000000, initial_deck2))
(8.22492, 6.7479)
'temps total': 258

print(compare('T7', 'A', 'H', '-', 10000000, initial_deck2))
(-69.31837, -63.7216)
'temps total': 157

print(compare('T6', 'A', 'H', '-', 10000000, initial_deck2))
(-66.46375, -76.80762)
'temps total': 163

print(compare('65', 'T', 'H', 'D', 10000000, initial_deck2))
(3.12508, 1.00404)
'temps total': 198

print(compare('A7', 'A', 'H', '-', 10000000, initial_deck2))
(-38.68594, -37.99646)
'temps total': 204

print(compare('63', '2', 'H', 'D', 10000000, initial_deck2))
(7.67801, 7.01894)
'temps total': 246

print(compare('66', '7', 'H', 'S', 10000000, initial_deck2))
(-22.09187, -29.03631)
'temps total': 345

print(compare('66', '2', 'H', 'S', 10000000, initial_deck2))
(-25.36591, -20.6662)
'temps total': 329

print(compare('22', '2', 'H', 'S', 10000000, initial_deck2))
(-11.49275, -13.46946)
'temps total': 387

print(compare('22', '3', 'H', 'S', 10000000, initial_deck2))
(-8.13619, -6.00278)
'temps total': 380


print(compare('22', '7', 'H', 'S', 10000000, initial_deck2))
(-8.88471, -14.1122)
'temps total': 416

print(compare('33', '7', 'H', 'S', 10000000, initial_deck2))
(-15.36563, -16.51287)
'temps total': 355