import Part
from FreeCAD import Base;

# Содание документа с именем
document = App.newDocument('FreeCAD filler test')

batteryWidth = float(300.0)                             # Ширина куба (x)
batteryDepth = float(300.0)                             # Глубина куба (y)
batteryHeight = float(300.0)                            # Высота куба (z)
row_betweenBattery = float(50.0)                        # Расстояние между батареями
boxThickness = float(20.0)                              # Толщина стенки короба
additionalHeight = float(50.0)                          # + к высоте стенки короба от аккумулятора 

# Левая стенка короба (x, y, z)
wallLeftWidth = float(boxThickness)                     # Ширина (x)
wallLeftDepth = float((5*(batteryDepth)+
                row_betweenBattery*6)
                )                                       # Глубина (y)
wallLeftHeight = float(batteryHeight+additionalHeight)  # Высота (z)

# Координаты левой стенки короба  (x,y,z)
LeftWall_X = float((-batteryWidth - 
             2*row_betweenBattery-
             boxThickness)
             )
LeftWall_Y = float(-row_betweenBattery)
LeftWall_Z = float(0.0)

# Форма левой стенки короба
boxShape = Part.makeBox(wallLeftWidth, wallLeftDepth, 
           wallLeftHeight, Base.Vector(LeftWall_X, 
           LeftWall_Y, LeftWall_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# Правая стенка короба (x, y, z)
wallRightWidth = float(boxThickness)                    # Ширина (x)
wallRightDepth = float((5*(batteryDepth)+ 
                 row_betweenBattery*6)
                 )                                      # Глубина (y)
wallRightHeight = float((batteryHeight+
                  additionalHeight)
                  )                                     # Высота (z)

# Координаты правой стенки короба (x,y,z)
RightWall_X = float(batteryWidth+row_betweenBattery)
RightWall_Y = float(-row_betweenBattery)
RightWall_Z = float(0.0)

# Форма правой стенки короба
boxShape = Part.makeBox(wallRightWidth, wallRightDepth, 
           wallRightHeight, Base.Vector
           (RightWall_X, RightWall_Y, RightWall_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# Передняя сторона короба (x, y, z)
wallAnteriortWidth = float((2*batteryWidth+
                     row_betweenBattery*
                     3 + 2*boxThickness)
                     )                                  # Ширина (x)
wallAnteriortDepth = float(boxThickness)                # Глубина (y)
wallAnteriortHeight = float((batteryHeight+
                      additionalHeight)
                      )                                 # Высота (z)

# Координаты передней стенки короба  (x,y,z)
AnteriortWall_X = float((-batteryWidth - 
                  2*row_betweenBattery-
                  boxThickness)
                  )
AnteriortWall_Y = float((-row_betweenBattery-
                  boxThickness)
                  )
AnteriortWall_Z = float(0.0)

# Форма передней стенки короба
boxShape = Part.makeBox(wallAnteriortWidth, 
           wallAnteriortDepth, wallAnteriortHeight, 
           Base.Vector(AnteriortWall_X, 
           AnteriortWall_Y, 
           AnteriortWall_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# Задняя сторона короба (x, y, z)
wallPosteriorWidth = float((2*batteryWidth+
                     row_betweenBattery*3 +
                     2*boxThickness)
                     )                                   # Ширина (x)
wallPosteriorDepth = float(boxThickness)                 # Глубина (y)
wallPosteriorHeight = float((batteryHeight+
                      additionalHeight)
                      )                                  # Высота (z)

# Координаты задней стенки короба  (x,y,z)
PosteriorWall_X = float((-batteryWidth - 
                  2*row_betweenBattery-
                  boxThickness)
                  )
PosteriorWall_Y = float((5*row_betweenBattery + 
                  5*batteryDepth)
                  )
PosteriorWall_Z = float(0.0)

# Форма задней стенки короба
boxShape = Part.makeBox(wallPosteriorWidth, 
           wallPosteriorDepth, wallPosteriorHeight, 
           Base.Vector(PosteriorWall_X, 
           PosteriorWall_Y, PosteriorWall_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# Нижняя сторона короба (x, y, z)
wallLowerWidth = float((2*batteryWidth+
                 row_betweenBattery*3 +
                 2*boxThickness)
                 )                                         # Ширина (x)
wallLowerDepth = float(6*row_betweenBattery + 
                 + 5*batteryDepth + 2*boxThickness
                 )                                         # Глубина (y)
wallLowerHeight = float(boxThickness)                      # Высота (z)

# Координаты нижней стенки короба  (x,y,z)
LowerWall_X = float((-batteryWidth - 
              2*row_betweenBattery-
              boxThickness)
              )
LowerWall_Y = float((-row_betweenBattery-
              boxThickness)
              )
LowerWall_Z = float(-boxThickness) 

# Форма нижней стенки короба
boxShape = Part.makeBox(wallLowerWidth, 
           wallLowerDepth, wallLowerHeight, 
           Base.Vector(LowerWall_X, 
           LowerWall_Y, LowerWall_Z)
)
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Расположения куба для 1-го ряда  (x,y,z)
row1_cubeLocation_X = float(0.0)                           # Ширина (x)
row1_cubeLocation_Y = float(batteryDepth)                  # Глубина (y)
row1_cubeLocation_Z = float(0.0)                           # Высота (z)

# Расположения куба для 2-го ряда  (x,y,z)
row2_cubeLocation_X = float((-batteryWidth-
                      row_betweenBattery)  
                      )                                    # Ширина (x)
row2_cubeLocation_Y = float(batteryDepth)                  # Глубина (y)
row2_cubeLocation_Z = float(0.0)                           # Высота (z)
 

# Форма куба 1-го ряда (1)
boxShape = Part.makeBox(batteryWidth,
           batteryDepth, batteryHeight, 
           Base.Vector(0, 0, 0)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 1-го ряда (2)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector
           (row1_cubeLocation_X, row1_cubeLocation_Y+
           row_betweenBattery, row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 1-го ряда (3)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 1-го ряда (4)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 1-го ряда (5)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 2-го ряда (1)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 0, 0)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 2-го ряда (2)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           row1_cubeLocation_Y+row_betweenBattery, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 2-го ряда (3)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 2-го ряда (4)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Форма куба 2-го ряда (5)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
           row1_cubeLocation_Z)
           )
# Объект для отображения формы 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# Переключить на наиболее удобный вид
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxonometric()

# Повторно нарисовать документ
document.recompute()