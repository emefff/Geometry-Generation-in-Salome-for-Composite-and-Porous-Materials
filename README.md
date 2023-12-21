# Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials
Python scripting in Salome allows us to automatically generate random particles or pores. With subsequent operations we are able to build composite or porous bodies for study in Code_Aster.

__________________________________________________________________________
**Composite Materials**

Composite (e.g. metal matrix composites) and porous materials (e.g. metallic foams) are studied by generating a suitable geometries in .step format which are subsequently meshed in netgen or gmsh. Generating random particles by hand in geometry is a tedious task, that, very often, leads to particle distributions, that are not random. 
Salome is based on Python and offers to load and dump scripts. A first peek into how whis works is easy: draw something in Salome GEOM and dump the Python script. By importing other tools you might need (e.g Numpy) we can achieve the above task with ease. The attached script 'random_tets_random_size_and_orientation.py' generates a given number of random tets with random orientation in a box. The box and a suitable cutbox for planar surfaces are also generated. A typical random flock of 200 tets may look like this:

![Bildschirmfoto vom 2023-12-18 10-03-52](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/e966b600-60e3-4bdf-a5ff-d2d5935e4948)

Subtracting these from the box gets us the matrix for our particle reinforced composite body, together they look like this:

![Bildschirmfoto vom 2023-12-18 10-04-19](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/4d8662a6-54ff-437e-ac54-f9ab5e00bf15)

For a composite like shown above it is important to partition the box with the particles to get one single body with several volumes (here: 201 volumes, one for the matrix, remaining volumes are particles). Code_aster has a lot of difficulty using LIAISON_MAIL on these meshes, thus we need one body for meshing the whole thing in one go. This will ensure that the particles (their meshes that is) are connected to the matrix. There will be no delaminations etc.:

![Bildschirmfoto vom 2023-12-18 13-11-37](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/f10943bb-9b3d-4936-8972-954c42378360)


When doing this we really have to watch the mesh size. Remember, we only have 200 particles, but the corresponding mesh consists of 1.1M nodes and uses 3.4M DOFs, although it is still quite coarse in some regions! Such a simulation can quickly get out of hand memory-wise if the mesh gets larger (here >150GB in memory were needed). Now what is this good for? With such models we can study the influence of particles/pores on our bulk/matrix material. For a much more complex real part we would for example, calculate a change in elastic modulus in this model and use the derived modulus for a simulation of the real part. As you can imagine, there are many more possibilities (thermal conductivity, maximum allowable stresses to stay below delamination ... etc.).

For this simple demonstration we only apply a step-wise displacement in -x on the surface on the right-hand side. From solid mechanics we know that edgy particles lead to very high maximum stresses (if in tension, delamination may occur), this can easily be followed by looking at Von Mises stresses:

![VMIS_1](https://github.com/emefff/Mesh-Generation-In-Salome-For-Composite-And-Porous-Materials/assets/89903493/28f9ac2d-8cfa-489a-8ad2-60c1dba78156)

__________________________________________________________________________
**Porous Materials**

Our second script generates random spheres in a box. A porous material is easily created by subtracting the spheres from the box. It results in a cheese-like body like this:

![Bildschirmfoto vom 2023-12-19 09-02-37](https://github.com/emefff/Mesh-Generation-in-Salome-for-Composite-and-Porous-Materials/assets/89903493/9f3bd01a-64d4-491c-9d34-9a4416e21767)

Again, we mesh it with netgen. Above said also holds: the mesh size can easily get out of hand size-wise:

![Bildschirmfoto vom 2023-12-19 09-03-59](https://github.com/emefff/Mesh-Generation-in-Salome-for-Composite-and-Porous-Materials/assets/89903493/fe54cf62-d970-4be6-a0db-594550ccd9f0)

The load case is the same for this geometry, we look at the Von Mises stresses of the structure. With applied displacements we find some of the walls severly deformed:

![VMIS_DEPLx1](https://github.com/emefff/Mesh-Generation-in-Salome-for-Composite-and-Porous-Materials/assets/89903493/46d7e43f-47a0-43fa-a7c5-115db6cfb65f)

Both scripts may be adapted to your needs, the possibilites are nearly endless. If you have the computing possibilities, you can also use the to make 'real' parts with particles, just adapt the box-parameters to your needs and subtract the particles or pores from your real part.

emefff@gmx.at
