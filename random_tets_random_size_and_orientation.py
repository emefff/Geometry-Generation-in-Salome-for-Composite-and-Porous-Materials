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

################################################################################


def generate_random_tet():
    """
    Generates a single random tetrahedron (solid) near the origin.

    Returns
    -------
    Solid_1 : TYPE Salome solid
        DESCRIPTION. Tetraedric random solid with max length tet_length. Size,
                     edge lengths, orientation, every aspect is random. Still
                     has to be added to study with geompy.addToStudy(*args)

    """
    tet_corners_4triples = np.random.uniform(0, tet_length, 12) - tet_length/2 
    # we want to keep the tet around the origin, therefore we subtract tet_length/2
    Vertex_1 = geompy.MakeVertex(tet_corners_4triples[0], tet_corners_4triples[1], tet_corners_4triples[2])
    Vertex_2 = geompy.MakeVertex(tet_corners_4triples[3], tet_corners_4triples[4], tet_corners_4triples[5])
    Vertex_3 = geompy.MakeVertex(tet_corners_4triples[6], tet_corners_4triples[7], tet_corners_4triples[8])
    Vertex_4 = geompy.MakeVertex(tet_corners_4triples[9], tet_corners_4triples[10], tet_corners_4triples[11])
    Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
    Line_2 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_3)
    Line_3 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
    Line_4 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_4)
    Line_5 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_4)
    Line_6 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_4)
    Face_1 = geompy.MakeFaceWires([Line_1, Line_2, Line_3], 1)
    Face_2 = geompy.MakeFaceWires([Line_3, Line_4, Line_5], 1)
    Face_3 = geompy.MakeFaceWires([Line_2, Line_4, Line_6], 1)
    Face_4 = geompy.MakeFaceWires([Line_1, Line_5, Line_6], 1)
    Shell_1 = geompy.MakeShell([Face_1, Face_2, Face_3, Face_4])
    Solid_1 = geompy.MakeSolid([Shell_1])
    return Solid_1


################################################################################

geompy = geomBuilder.New()

print(50*"*")
print("dir(geompy) = ", dir(geompy), "\n")
print(50*"*")
print("dir(gst) = ", dir(gst), "\n")
print(50*"*")

box_length = 200 # length of cube that is our playfield
tet_length = 50 # a number to limit size of tets
num_tets = 200 # number of tets to be generated

# origin and axes
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

# We draw the original box as Box_1, Cutbox for planar surfaces or our tets (Cut_1_for_planar_surfs)
Box_1 = geompy.MakeBoxDXDYDZ(box_length, box_length, box_length)
geompy.addToStudy( Box_1, 'Box_1' )
plus_length = tet_length+100
Box_2 = geompy.MakeBoxDXDYDZ(box_length+plus_length, box_length+plus_length, box_length+plus_length)
geompy.TranslateDXDYDZ(Box_2, -plus_length/2, -plus_length/2, -plus_length/2)
Cut_1_for_planar_surfs = geompy.MakeCutList(Box_2, [Box_1]) # use this object to Cut spheres in order to get plana surfaces
geompy.addToStudy(Cut_1_for_planar_surfs, 'Cut_1_for_planar_surfs' )

tets_dict = {}

# generate num_tets random translation vectors
translate_x = np.random.uniform(0, box_length, num_tets)
translate_y = np.random.uniform(0, box_length, num_tets)
translate_z = np.random.uniform(0, box_length, num_tets)


for i in range(num_tets): # generate dict for tets
    key_str = 'Tet_'+str(i)
    tets_dict[key_str] = [translate_x[i], translate_y[i], translate_z[i]]

locals().update(tets_dict) # creates var names from dict

# gt.TEST_createAndDeleteShape()

tet_list = []
print("")
print("Generating tetrahedrons ...")
for i in range(num_tets):
    key_str = 'Tet_'+str(i)
    tet_list.append(key_str)
    tet = generate_random_tet()
    var = geompy.MakeTranslation(tet, float(tets_dict[key_str][0]), float(tets_dict[key_str][1]), float(tets_dict[key_str][2]) )
    geompy.addToStudy(var, key_str)

print(50*"*")
#print("tets_dict = ", tets_dict)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
