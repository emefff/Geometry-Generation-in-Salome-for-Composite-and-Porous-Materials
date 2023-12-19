#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.8.0 with dump python functionality
###

import sys
import salome
import numpy as np

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/mario')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
# from salome.geom import geomtools as gt
from salome.geom.geomtools import GeomStudyTools as gst
import math
import SALOMEDS

geompy = geomBuilder.New()

print(50*"*")
print("dir(geompy) = ", dir(geompy), "\n")
print(50*"*")
print("dir(gst) = ", dir(gst), "\n")
print(50*"*")

box_length = 200 # edge length of the cube that is our playfield
num_spheres = 100 # number of generated spheres
sphere_min_radius = 10
sphere_max_radius = 25


# origin and axes
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

# We draw the original box as Box_1, Cutbox for planar surfaces or our tets (Cut_1_for_planar_surfs)
Box_1 = geompy.MakeBoxDXDYDZ(box_length, box_length, box_length)
geompy.addToStudy( Box_1, 'Box_1' )
plus_length = sphere_max_radius+100
Box_2 = geompy.MakeBoxDXDYDZ(box_length+plus_length, box_length+plus_length, box_length+plus_length)
geompy.TranslateDXDYDZ(Box_2, -plus_length/2, -plus_length/2, -plus_length/2)
Cut_1_for_planar_surfs = geompy.MakeCutList(Box_2, [Box_1]) # use this object to Cut spheres in order to get plana surfaces
geompy.addToStudy(Cut_1_for_planar_surfs, 'Cut_1_for_planar_surfs' )

spheres_center_x = np.random.uniform(0, 200, num_spheres)
spheres_center_y = np.random.uniform(0, 200, num_spheres)
spheres_center_z = np.random.uniform(0, 200, num_spheres)

spheres_radii = np.random.uniform(sphere_min_radius, sphere_max_radius, num_spheres)

spheres_dict = {}

for i in range(num_spheres): #generate centers for spheres
    key_str = 'Sphere_'+str(i)
    spheres_dict[key_str] = [spheres_center_x[i], spheres_center_y[i], spheres_center_z[i], spheres_radii[i]]
    
locals().update(spheres_dict) # creates var names from dict

print("")
print("Generating spheres ...")
for i in range(num_spheres):
    key_str = 'Sphere_'+str(i)
    var = exec(key_str)
    sphere = geompy.MakeSphereR(float(spheres_dict[key_str][3])) # sphere in origin
    var = geompy.MakeTranslation(sphere, float(spheres_dict[key_str][0]), float(spheres_dict[key_str][1]), float(spheres_dict[key_str][2]) )
    geompy.addToStudy(var, key_str)

print(50*"*")
#print(spheres_dict)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
