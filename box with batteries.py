import Part
from FreeCAD import Base;

# Create a document with a name
document = App.newDocument('FreeCAD filler test')

batteryWidth = float(300.0)                             # Cube width (x)
batteryDepth = float(300.0)                             # Depth of cube (y)
batteryHeight = float(300.0)                            # Cube height (z)
row_betweenBattery = float(50.0)                        # Distance between batteries
boxThickness = float(20.0)                              # Box wall thickness
additionalHeight = float(50.0)                          # + to the height of the box wall from the battery

# Left side of the box (x, y, z)
wallLeftWidth = float(boxThickness)                     # Width (x)
wallLeftDepth = float((5*(batteryDepth)+
                row_betweenBattery*6)
                )                                       # Depth (y)
wallLeftHeight = float(batteryHeight+additionalHeight)  # Height (z)

# Coordinates of the left wall of the box  (x,y,z)
LeftWall_X = float((-batteryWidth - 
             2*row_betweenBattery-
             boxThickness)
             )
LeftWall_Y = float(-row_betweenBattery)
LeftWall_Z = float(0.0)

# Shape of the left wall of the box
boxShape = Part.makeBox(wallLeftWidth, wallLeftDepth, 
           wallLeftHeight, Base.Vector(LeftWall_X, 
           LeftWall_Y, LeftWall_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Right side of the box (x, y, z)
wallRightWidth = float(boxThickness)                    # Width (x)
wallRightDepth = float((5*(batteryDepth)+ 
                 row_betweenBattery*6)
                 )                                      # Depth (y)
wallRightHeight = float((batteryHeight+
                  additionalHeight)
                  )                                     # Height (z)

# Coordinates of the right wall of the box (x,y,z)
RightWall_X = float(batteryWidth+row_betweenBattery)
RightWall_Y = float(-row_betweenBattery)
RightWall_Z = float(0.0)

# Shape of the right wall of the box
boxShape = Part.makeBox(wallRightWidth, wallRightDepth, 
           wallRightHeight, Base.Vector
           (RightWall_X, RightWall_Y, RightWall_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Front of the box (x, y, z)
wallAnteriortWidth = float((2*batteryWidth+
                     row_betweenBattery*
                     3 + 2*boxThickness)
                     )                                  # Width (x)
wallAnteriortDepth = float(boxThickness)                # Depth (y)
wallAnteriortHeight = float((batteryHeight+
                      additionalHeight)
                      )                                 # Height (z)

# Coordinates of the front wall of the box  (x,y,z)
AnteriortWall_X = float((-batteryWidth - 
                  2*row_betweenBattery-
                  boxThickness)
                  )
AnteriortWall_Y = float((-row_betweenBattery-
                  boxThickness)
                  )
AnteriortWall_Z = float(0.0)

# Shape of the front wall of the box
boxShape = Part.makeBox(wallAnteriortWidth, 
           wallAnteriortDepth, wallAnteriortHeight, 
           Base.Vector(AnteriortWall_X, 
           AnteriortWall_Y, 
           AnteriortWall_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Back side of the box (x, y, z)
wallPosteriorWidth = float((2*batteryWidth+
                     row_betweenBattery*3 +
                     2*boxThickness)
                     )                                   # Width (x)
wallPosteriorDepth = float(boxThickness)                 # Depth (y)
wallPosteriorHeight = float((batteryHeight+
                      additionalHeight)
                      )                                  # Height (z)

# Coordinates of the rear wall of the box  (x,y,z)
PosteriorWall_X = float((-batteryWidth - 
                  2*row_betweenBattery-
                  boxThickness)
                  )
PosteriorWall_Y = float((5*row_betweenBattery + 
                  5*batteryDepth)
                  )
PosteriorWall_Z = float(0.0)

# Shape of the back wall of the box
boxShape = Part.makeBox(wallPosteriorWidth, 
           wallPosteriorDepth, wallPosteriorHeight, 
           Base.Vector(PosteriorWall_X, 
           PosteriorWall_Y, PosteriorWall_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# The underside of the box (x, y, z)
wallLowerWidth = float((2*batteryWidth+
                 row_betweenBattery*3 +
                 2*boxThickness)
                 )                                         # Width (x)
wallLowerDepth = float(6*row_betweenBattery + 
                 + 5*batteryDepth + 2*boxThickness
                 )                                         # Depth (y)
wallLowerHeight = float(boxThickness)                      # Height (z)

# Coordinates of the bottom wall of the box  (x,y,z)
LowerWall_X = float((-batteryWidth - 
              2*row_betweenBattery-
              boxThickness)
              )
LowerWall_Y = float((-row_betweenBattery-
              boxThickness)
              )
LowerWall_Z = float(-boxThickness) 

# Shape of the bottom wall of the box
boxShape = Part.makeBox(wallLowerWidth, 
           wallLowerDepth, wallLowerHeight, 
           Base.Vector(LowerWall_X, 
           LowerWall_Y, LowerWall_Z)

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Cube locations for the 1st row  (x,y,z)
row1_cubeLocation_X = float(0.0)                           # Width (x)
row1_cubeLocation_Y = float(batteryDepth)                  # Depth (y)
row1_cubeLocation_Z = float(0.0)                           # Height (z)

# Cube locations for the 2nd row (x,y,z)
row2_cubeLocation_X = float((-batteryWidth-
                      row_betweenBattery)  
                      )                                    # Width (x)
row2_cubeLocation_Y = float(batteryDepth)                  # Depth (y)
row2_cubeLocation_Z = float(0.0)                           # Height (z)
 

# Form of the cube of the 1st row (1)
boxShape = Part.makeBox(batteryWidth,
           batteryDepth, batteryHeight, 
           Base.Vector(0, 0, 0)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Form of the cube of the 1st row (2)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector
           (row1_cubeLocation_X, row1_cubeLocation_Y+
           row_betweenBattery, row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Form of the cube of the 1st row (3)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
           row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Form of the cube of the 1st row (4)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
           row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Form of the cube of the 1st row (5)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
           row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Cube shape of the 2nd row (1)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 0, 0)
           )
# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Cube shape of the 2nd row (2)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           row1_cubeLocation_Y+row_betweenBattery, 
           row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Cube shape of the 2nd row (3)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
           row1_cubeLocation_Z)
           )

# Object to display the form 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Cube shape of the 2nd row (4)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
           row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Cube shape of the 2nd row (5)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
           row1_cubeLocation_Z)
           )

# Object to display the form
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Switch to the most convenient view
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxonometric()

# Re-draw the document
document.recompute()