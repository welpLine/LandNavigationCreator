#land nav calculator
#2ndLt Mokarry, USMC

import pyproj
import csv
import random

geodesic = pyproj.Geod(ellps='WGS84')
cds = list();
with open('coordinates.csv') as csvfile:
	cdreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in cdreader:
		coord = [row[0], row[1], row[2]]
		cds.append(coord)

print("Land Nav Simplifier\nPoints:")
print(cds)
print('')

import geopy.distance
#format (y1, x1, y2, x2)
#for i in range(0,len(cds)):
#	for j in range(0, len(cds)):
#		if i==j: continue
#		print ("From point {0} to point {1}, ({2} to {3})".format(i,j, cds[i][2], cds[j][2]))
#		fwd_azimuth, back_azimuth, distance = geodesic.inv(cds[i][1], cds[i][0], cds[j][1], cds[j][0])
#		print(str((fwd_azimuth,fwd_azimuth+360)[fwd_azimuth<0]) + ' degrees')
#		print(str(distance) + ' meters\n')

print("\nSample Problem")
s = 0;
for i in range(0,6):
	next = random.randrange(1,len(cds))
	if(next == s):
		i = i-1
		continue
	print ("From point {0} to point {1}".format(s,next))
	fwd_azimuth, back_azimuth, distance = geodesic.inv(cds[s][1], cds[s][0], cds[next][1], cds[next][0])
	print(str((fwd_azimuth,fwd_azimuth+360)[fwd_azimuth<0]) + ' degrees')
	print(str(distance) + ' meters')
	print("Solution: " + cds[next][2] + '\n')
	s = next

print ("From point {0} to point {1}".format(s,0))
fwd_azimuth, back_azimuth, distance = geodesic.inv(cds[s][1], cds[s][0], cds[0][1], cds[0][0])
print(str(fwd_azimuth) + ' degrees')
print(str(distance) + ' meters\nSolution: Start')
print("End Problem")


