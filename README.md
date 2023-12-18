# Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials
Python scripting in Salome allows us to automatically generate random particles or pores. With subsequent operations we are able to build composite or porous bodies for study in Code_Aster.

Composite (e.g. metal matrix composites) and porous materials (e.g. metallic foams) are studied by generating a suitable geometries in .step format which are subsequently meshed in netgen or gmsh. Generating random particles by hand in geometry is a tedious task, that, very often, leads to particle distributions, that are not random. 
Salome is based on Python and offers to load and dump scripts. A first peek into how whis works is easy: draw something in Salome GEOM and dump the Python script. By importing other tools you might need (e.g Numpy) we can achieve the above task with ease. The attached script 'random_tets_random_size_and_orientation.py' generates a given number of random tets with random orientation in a box. The box and a suitable cutbox for planar surfaces are also generated. A typical random flock of 200 tets may look like this:

![Bildschirmfoto vom 2023-12-18 10-03-52](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/e966b600-60e3-4bdf-a5ff-d2d5935e4948)

Subtracting these from the box gets us the matrix for our particle reinforced composite body, together they look like this:

![Bildschirmfoto vom 2023-12-18 10-04-19](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/4d8662a6-54ff-437e-ac54-f9ab5e00bf15)

For a composite like shown above it is important to partition the box with the particles to get one single body with several volumes (here: 201 volumes, one for the matrix, remaining volumes are particles). Code_aster has a lot of difficulty using LIAISON_MAIL on these meshes, thus we need one body for meshing the whole thing in one go. This will ensure that the particles (their meshes that is) are connected to the matrix. There will be no delaminations etc.:

![Bildschirmfoto vom 2023-12-18 13-11-37](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/f10943bb-9b3d-4936-8972-954c42378360)


When doing this we really have to watch the mesh size. Remember, we only have 200 particles, but the corresponding mesh consists of 1.1M nodes and uses 3.4M DOFs, although it is still quite coarse in some regions! Such a simulation can quickly get out of hand memory-wise if the mesh gets larger (here we needed >100GB in memory). 
For this simple demonstration we only apply a step-wise displacement on one of the surfaces. From theoretical mechanics we know that edgy particles lead to very high maximum stresses, this can easily be followed by looking at Von Mises stresses:


