
import datetime;
import Draft;
import os;
import Drawing;
import Part;
from FreeCAD import Base;

# Sodaniye of the document with a name (Sodaniye dokumenta s imenem)
document = App.newDocument('FreeCAD NG300 case')

shelveGroup = document.addObject("App::DocumentObjectGroup", "Shelve");

class TenBatteriesCase:

    """ My box with batteries"""
    def __init__(self, batteryWidth, batteryDepth, 
                batteryHeight, row_betweenBattery, 
                boxThickness, additionalHeight, 
                rotation, x, y, z, scale_by_x, 
                scale_by_y, scale_by_z):
        self.batteryWidth = batteryWidth
        self.batteryDepth = batteryDepth
        self.batteryHeight = batteryHeight
        self.row_betweenBattery = row_betweenBattery
        self.boxThickness = boxThickness
        self.additionalHeight = additionalHeight
        self.rotation = rotation
        self.x = x
        self.y = y
        self.z = z
        self.scale_by_x = scale_by_x
        self.scale_by_y = scale_by_y
        self.scale_by_z = scale_by_z

        # Scaling a shape (Masshtabirovaniye formy)
        myMat = Base.Matrix()
        myMat.scale(scale_by_x,scale_by_y,scale_by_z)

        wallLeftWidth = float(boxThickness)                     # Width (Shirina) (x)
        wallLeftDepth = float((5*(batteryDepth)+
                        row_betweenBattery*6)
                        )                                       # Depth (glubina) (y)
        wallLeftHeight = float(batteryHeight+additionalHeight
                         -150)                                  # Height (Vysota) (z)

        # Coordinates of the left wall of a box (Koordinaty levoy stenki yashchika)(x, y, z)
        LeftWall_X = float((-batteryWidth - 
                     2*row_betweenBattery-
                     boxThickness)
                     )
        LeftWall_Y = float(-row_betweenBattery)
        LeftWall_Z = float(0.0)

        # Form of the left wall of a box (Forma levoy stenki korobki)
        boxShapeLTh = Part.makeBox(wallLeftWidth, wallLeftDepth, 
                      wallLeftHeight, Base.Vector(LeftWall_X, 
                      LeftWall_Y, LeftWall_Z)
                      )

        # Turn of the left wall of a box (Povorot levoy steny korobki)
        boxShapeLTh.rotate(Base.Vector ((-batteryWidth - 
                          2*row_betweenBattery-
                          boxThickness),(-row_betweenBattery),0),
                          Base.Vector(x, y, z), rotation)
        
        # Scaling a shape (Masshtabirovaniye formy)
        boxShapeLTh = boxShapeLTh.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box1 = document.addObject('Part::Feature', 'Box')
        box1.Shape = boxShapeLTh


        # Right wall of a box (Pravaya stenka korobki) (x, y, z)
        wallRightWidth = float(boxThickness)                    # Width (Shirina) (x)
        wallRightDepth = float((5*(batteryDepth)+ 
                         row_betweenBattery*6)
                         )                                      # Depth (glubina) (y)
        wallRightHeight = float((batteryHeight+
                          additionalHeight-150)
                          )                                     # Height (Vysota) (z)

        # Coordinates of the right wall of a box (Koordinaty pravoy stenki yashchika) (x, y, z)
        RightWall_X = float(batteryWidth+row_betweenBattery)
        RightWall_Y = float(-row_betweenBattery)
        RightWall_Z = float(0.0)


        # Form of the right wall of a box (Forma pravoy stenki yashchika)
        boxShapeRTh = Part.makeBox(wallRightWidth, wallRightDepth, 
                      wallRightHeight, Base.Vector
                      (RightWall_X, RightWall_Y, RightWall_Z)
                      )

        # Turn of the right wall of a box (Povorot pravoy stenki yashchika)
        boxShapeRTh.rotate(Base.Vector ((-batteryWidth - 
                          2*row_betweenBattery-
                          boxThickness),(-row_betweenBattery),0),
                          Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShapeRTh = boxShapeRTh.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box2 = document.addObject('Part::Feature', 'Box')
        box2.Shape = boxShapeRTh


        # Front face of a box (Perednyaya storona korobki) (x, y, z)
        wallAnteriortWidth = float((2*batteryWidth+
                            row_betweenBattery*
                            3 + 2*boxThickness)
                            )                                   # Width (Shirina) (x)
        wallAnteriortDepth = float(boxThickness)                # Depth (glubina) (y)
        wallAnteriortHeight = float((batteryHeight+
                              additionalHeight-150)
                              )                                 # Height (Vysota) (z)

        # Coordinates of a front wall of a box (Koordinaty peredney stenki korobki) (x, y, z)
        AnteriortWall_X = float((-batteryWidth - 
                          2*row_betweenBattery-
                          boxThickness)
                          )
        AnteriortWall_Y = float((-row_betweenBattery-
                          boxThickness)
                          )
        AnteriortWall_Z = float(0.0)

        # Form of a front wall of a box (Forma peredney stenki korobki)
        boxShapeATh = Part.makeBox(wallAnteriortWidth, 
                      wallAnteriortDepth, wallAnteriortHeight, 
                      Base.Vector(AnteriortWall_X, 
                      AnteriortWall_Y, 
                      AnteriortWall_Z)
                      )

        # Turn of a front wall of a box (Povorot peredney stenki korobki)
        boxShapeATh.rotate(Base.Vector ((-batteryWidth - 
                          2*row_betweenBattery-
                          boxThickness),(-row_betweenBattery),0),
                          Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShapeATh = boxShapeATh.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box3 = document.addObject('Part::Feature', 'Box')
        box3.Shape = boxShapeATh


        # Back face of a box (Zadnyaya storona korobki) (x, y, z)
        wallPosteriorWidth = float((2*batteryWidth+
                             row_betweenBattery*3 +
                             2*boxThickness)
                             )                                   # Width (Shirina) (x)
        wallPosteriorDepth = float(boxThickness)                 # Depth (glubina) (y)
        wallPosteriorHeight = float((batteryHeight+
                              additionalHeight-150)
                              )                                  # Height (Vysota) (z)

        # Coordinates of a back wall of a box (Koordinaty zadney stenki yashchika) (x, y, z)
        PosteriorWall_X = float((-batteryWidth - 
                          2*row_betweenBattery-
                          boxThickness)
                          )
        PosteriorWall_Y = float((5*row_betweenBattery + 
                          5*batteryDepth)
                          )
        PosteriorWall_Z = float(0.0)

        # Form of a back wall of a box (Forma zadney stenki korobki)
        boxShapePTh = Part.makeBox(wallPosteriorWidth, 
                      wallPosteriorDepth, wallPosteriorHeight, 
                      Base.Vector(PosteriorWall_X, 
                      PosteriorWall_Y, PosteriorWall_Z)
                      )

        # Turn of a back wall of a box (Povorot zadney stenki yashchika)
        boxShapePTh.rotate(Base.Vector ((-batteryWidth - 
                          2*row_betweenBattery-
                          boxThickness),(-row_betweenBattery),0),
                          Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShapePTh = boxShapePTh.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box4 = document.addObject('Part::Feature', 'Box')
        box4.Shape = boxShapePTh


        # Lower side of a box (Nizhnyaya storona korobki) (x, y, z)
        wallLowerWidth = float((2*batteryWidth+
                         row_betweenBattery*3 +
                         2*boxThickness)
                         )                                         # Width (Shirina) (x)
        wallLowerDepth = float(6*row_betweenBattery + 
                         + 5*batteryDepth + 2*boxThickness
                         )                                         # Depth (glubina) (y)
        wallLowerHeight = float(boxThickness)                      # Height (Vysota) (z)

        # Coordinates of the lower wall of a box (Koordinaty nizhney stenki yashchika) (x, y, z)
        LowerWall_X = float((-batteryWidth - 
                      2*row_betweenBattery-
                      boxThickness)
                      )
        LowerWall_Y = float((-row_betweenBattery-
                      boxThickness)
                      )
        LowerWall_Z = float(-boxThickness) 

        # Form of the lower wall of a box (Forma nizhney stenki yashchika)
        boxShapeLoTh = Part.makeBox(wallLowerWidth, 
                       wallLowerDepth, wallLowerHeight, 
                       Base.Vector(LowerWall_X, 
                       LowerWall_Y, LowerWall_Z)
                       )

        # Turn of the lower wall of a box (Povorot nizhney stenki yashchika)
        boxShapeLoTh.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShapeLoTh = boxShapeLoTh.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box5 = document.addObject('Part::Feature', 'Box')
        box5.Shape = boxShapeLoTh

        # Layouts of a cube for the 1st row (Makety kuba dlya 1-y stroki) (x,y,z)
        row1_cubeLocation_X = float(0.0)                           # Width (Shirina) (x)
        row1_cubeLocation_Y = float(batteryDepth)                  # Depth (glubina) (y)
        row1_cubeLocation_Z = float(0.0)                           # Height (Vysota) (z)

        # Layouts of a cube for the 2nd row (Makety kuba dlya vtoroy stroki) (x, y, z)
        row2_cubeLocation_X = float((-batteryWidth-
                              row_betweenBattery)  
                              )                                    # Width (Shirina) (x)
        row2_cubeLocation_Y = float(batteryDepth)                  # Depth (glubina) (y)
        row2_cubeLocation_Z = float(0.0)                           # Height (Vysota) (z)                           
 

        # Form of a cube of the 1st row (1) (Forma kuba 1-go ryada (1))
        boxShape_1_1 = Part.makeBox(batteryWidth,
                       batteryDepth, batteryHeight, 
                       Base.Vector(0, 0, 0)
                       )

        # Turn of a cube of the 1st row, the 2nd cube (Povorot kuba 1-go ryada, 2-y kub)
        boxShape_1_1.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_1_1 = boxShape_1_1.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_1_1


        # Form of a cube of the 1st row (2) (Forma kuba 1-go ryada (2))
        boxShape_1_2 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector
                       (row1_cubeLocation_X, row1_cubeLocation_Y+
                       row_betweenBattery, row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 1st row, the 2nd cube (Povorot kuba 1-go ryada, 2-y kub)
        boxShape_1_2.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_1_2 = boxShape_1_2.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_1_2

        # Form of a cube of the 1st row (3) (Forma kuba 1-go ryada (3))
        boxShape_1_3 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector(row1_cubeLocation_X, 
                       2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
                       row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 1st row, the 3rd cube (Povorot kuba 1-go ryada, 3-go kuba)
        boxShape_1_3.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_1_3 = boxShape_1_3.transformGeometry(myMat) 

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_1_3

        # Form of a cube of the 1st row (4) (Forma kuba 1-go ryada (4))
        boxShape_1_4 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector(row1_cubeLocation_X, 
                       3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
                       row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 1st row, the 4th cube (Povorot kuba 1-go ryada, 4-y kub)
        boxShape_1_4.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_1_4 = boxShape_1_4.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_1_4

        # Form of a cube of the 1st row (5) (Forma kuba 1-go ryada (5))
        boxShape_1_5 = Part.makeBox(batteryWidth, batteryDepth, 
                   batteryHeight, Base.Vector(row1_cubeLocation_X, 
                   4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
                   row1_cubeLocation_Z)
                   )

        # Turn of a cube of the 1st row, the 5th cube (Povorot kuba 1-go ryada, 5-y kub)
        boxShape_1_5.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_1_5 = boxShape_1_5.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_1_5

        # Form of a cube of the 2nd row (1) (Forma kuba vtorogo ryada (1))
        boxShape_2_1 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector
                       (row2_cubeLocation_X, 0, 0)
                       )

        # Turn of a cube of the 2nd row, the 1st cube (Povorot kuba 2-go ryada, 1-y kub)
        boxShape_2_1.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_2_1 = boxShape_2_1.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_2_1

        # Form of a cube of the 2nd row (2) (Forma kuba vtorogo ryada (2))
        boxShape_2_2 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector(row2_cubeLocation_X, 
                       row1_cubeLocation_Y+row_betweenBattery, 
                       row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 2nd row, the 2nd cube (Povorot kuba 2-go ryada, 2-y kub)
        boxShape_2_2.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_2_2 = boxShape_2_2.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_2_2

        # Form of a cube of the 2nd row (3) (Forma kuba vtorogo ryada (3))
        boxShape_2_3 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector(row2_cubeLocation_X, 
                       2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
                       row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 2nd row, the 3rd cube (Povorot kuba 2-go ryada, 3-go kuba)
        boxShape_2_3.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_2_3 = boxShape_2_3.transformGeometry(myMat)

        # Object for display of the form  (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_2_3

        # Form of a cube of the 2nd row (4) (Forma kuba vtorogo ryada (4))
        boxShape_2_4 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector(row2_cubeLocation_X, 
                       3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
                       row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 2nd row, the 4th cube (Povorot kuba 2-go ryada, 4-y kub)
        boxShape_2_4.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_2_4 = boxShape_2_4.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_2_4

        # Form of a cube of the 2nd row (5) (Forma kuba 2-go ryada (5))
        boxShape_2_5 = Part.makeBox(batteryWidth, batteryDepth, 
                       batteryHeight, Base.Vector(row2_cubeLocation_X, 
                       4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
                       row1_cubeLocation_Z)
                       )

        # Turn of a cube of the 2nd row, the 5th cube (Povorot kuba 2-go ryada, 5-y kub)
        boxShape_2_5.rotate(Base.Vector ((-batteryWidth - 
                           2*row_betweenBattery-
                           boxThickness),(-row_betweenBattery),0),
                           Base.Vector(x, y, z), rotation)

        # Scaling a shape (Masshtabirovaniye formy)
        boxShape_2_5 = boxShape_2_5.transformGeometry(myMat)

        # Object for display of the form (Ob"yekt dlya otobrazheniya formy)
        box = document.addObject('Part::Feature', 'Box')
        box.Shape = boxShape_2_5

##############################################################################################

        ###
        self.partVersion = "1.0";
        ###
        self.box1Clone = Draft.clone(box1);
        self.box2Clone = Draft.clone(box2);
        self.box3Clone = Draft.clone(box3);
        self.box4Clone = Draft.clone(box4);
        self.box5Clone = Draft.clone(box5);
        self.box6Clone = Draft.clone(box5);
        ###
        boxShapeLTh.rotate(Base.Vector((-batteryWidth - 
                          2*row_betweenBattery-boxThickness),
                          (-row_betweenBattery),0), 
                          Base.Vector(1, 0, 0), -90);
        boxShapeRTh.rotate(Base.Vector((-batteryWidth - 
                          2*row_betweenBattery-boxThickness),
                          (-row_betweenBattery),0), 
                          Base.Vector(1, 0, 0), -90);
        boxShapeATh.rotate(Base.Vector((-batteryWidth - 
                          2*row_betweenBattery-boxThickness),
                          (-row_betweenBattery),0), 
                          Base.Vector(1, 0, 0), -90);
        boxShapePTh.rotate(Base.Vector((-batteryWidth - 
                          2*row_betweenBattery-boxThickness),
                          (-row_betweenBattery),0), 
                          Base.Vector(1, 0, 0), -90);
        boxShapeLoTh.rotate(Base.Vector((-batteryWidth - 
                          2*row_betweenBattery-boxThickness),
                          (-row_betweenBattery),0), 
                          Base.Vector(1, 0, 0), -90);
        ###
        self.box1Clone.Shape = boxShapeLTh;
        self.box2Clone.Shape = boxShapeRTh;
        self.box3Clone.Shape = boxShapeATh;
        self.box4Clone.Shape = boxShapePTh;
        self.box5Clone.Shape = boxShapeLoTh;
        self.box6Clone.Shape = boxShapeLoTh;
        ###
        self.box1Clone.ViewObject.Visibility = 0;
        self.box2Clone.ViewObject.Visibility = 0;
        self.box3Clone.ViewObject.Visibility = 0;
        self.box4Clone.ViewObject.Visibility = 0;
        self.box5Clone.ViewObject.Visibility = 0;
        self.box6Clone.ViewObject.Visibility = 0;
        ###
        shelveGroup.addObject(self.box1Clone);
        shelveGroup.addObject(self.box2Clone);
        shelveGroup.addObject(self.box3Clone);
        shelveGroup.addObject(self.box4Clone);
        shelveGroup.addObject(self.box5Clone);
        shelveGroup.addObject(self.box6Clone);
        ###

    def display3D(self):

        # Side part page (Stranitsa chasti storony)
        box1ClonePage = box2ClonePage = box3ClonePage =\
        box4ClonePage = box5ClonePage = document.addObject\
        ('Drawing::FeaturePage', 'Display 3D');
        box1ClonePage.Template = box2ClonePage.Template =\
        box3ClonePage.Template = box4ClonePage.Template =\
        box5ClonePage.Template = os.path.dirname(__file__)\
        + '/A4-Portrait-ISO7200.svg';
        ###
        box1CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display 3D view');
        box2CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display 3D view');
        box3CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display 3D view');
        box4CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display 3D view');
        box5CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display 3D view');
        ###
        box1CloneView.Source = self.box1Clone;
        box2CloneView.Source = self.box2Clone;
        box3CloneView.Source = self.box3Clone;
        box4CloneView.Source = self.box4Clone;
        box5CloneView.Source = self.box5Clone;
        ###
        box1CloneView.Direction = box2CloneView.Direction =\
        box3CloneView.Direction = box4CloneView.Direction =\
        box5CloneView.Direction = (1, 1, 1);
        ###
        box1CloneView.X = box2CloneView.X = box3CloneView.X =\
        box4CloneView.X = box5CloneView.X = 80.0;
        ###
        box1CloneView.Y = box2CloneView.Y = box3CloneView.Y =\
        box4CloneView.Y = box5CloneView.Y = 160.0;
        ###
        box1CloneView.Scale = box2CloneView.Scale =\
        box3CloneView.Scale = box4CloneView.Scale =\
        box5CloneView.Scale = 0.12; # drawingScale;
        ###
        box1ClonePage.addObject(box1CloneView);
        box2ClonePage.addObject(box2CloneView);
        box3ClonePage.addObject(box3CloneView);
        box4ClonePage.addObject(box4CloneView);
        box5ClonePage.addObject(box5CloneView);
        # Change page texts (Izmenit' tekst stranitsy)
        box1CloneTexts = box1ClonePage.EditableTexts;
        box2CloneTexts = box2ClonePage.EditableTexts;
        box3CloneTexts = box3ClonePage.EditableTexts;
        box4CloneTexts = box4ClonePage.EditableTexts;
        box5CloneTexts = box5ClonePage.EditableTexts;
        # Author (avtor)
        box1CloneTexts[0] = "FreeCAD NG300 case";
        box2CloneTexts[0] = "FreeCAD NG300 case";
        box3CloneTexts[0] = "FreeCAD NG300 case";
        box4CloneTexts[0] = "FreeCAD NG300 case";
        box5CloneTexts[0] = "FreeCAD NG300 case";
        # Drawing name (Nazvaniye chertezha)
        box1CloneTexts[1] = "Display 3D";
        box2CloneTexts[1] = "Display 3D";
        box3CloneTexts[1] = "Display 3D";
        box4CloneTexts[1] = "Display 3D";
        box5CloneTexts[1] = "Display 3D";
        # Scale (Masshtab)
        box1CloneTexts[10] = str(box1CloneView.Scale); # str(drawingScale);
        box2CloneTexts[10] = str(box2CloneView.Scale); # str(drawingScale);
        box3CloneTexts[10] = str(box3CloneView.Scale); # str(drawingScale);
        box4CloneTexts[10] = str(box4CloneView.Scale); # str(drawingScale);
        box5CloneTexts[10] = str(box5CloneView.Scale); # str(drawingScale);
        # Drawing (Risovaniye)
        box1CloneTexts[12] = "1";
        box2CloneTexts[12] = "1";
        box3CloneTexts[12] = "1";
        box4CloneTexts[12] = "1";
        box5CloneTexts[12] = "1";
        # Date (Data)
        box1CloneTexts[13] = datetime.datetime.now().strftime("%Y-%m-%d");
        box2CloneTexts[13] = datetime.datetime.now().strftime("%Y-%m-%d");
        box3CloneTexts[13] = datetime.datetime.now().strftime("%Y-%m-%d");
        box4CloneTexts[13] = datetime.datetime.now().strftime("%Y-%m-%d");
        box5CloneTexts[13] = datetime.datetime.now().strftime("%Y-%m-%d");
        # Version (Versiya)
        box1CloneTexts[14] = self.partVersion;
        box2CloneTexts[14] = self.partVersion;
        box3CloneTexts[14] = self.partVersion;
        box4CloneTexts[14] = self.partVersion;
        box5CloneTexts[14] = self.partVersion;
        ###
        box1ClonePage.EditableTexts = box1CloneTexts;
        box2ClonePage.EditableTexts = box2CloneTexts;
        box3ClonePage.EditableTexts = box3CloneTexts;
        box4ClonePage.EditableTexts = box4CloneTexts;
        box5ClonePage.EditableTexts = box5CloneTexts;
        ###

    def displayBottomSide(self):

        # Side part page (Stranitsa chasti storony)
        box5ClonePage = box6ClonePage = document.addObject\
        ('Drawing::FeaturePage', 'Display bottom side');
        box5ClonePage.Template = os.path.dirname\
        (__file__) + '/A4-Portrait-ISO7200.svg';
        box6ClonePage.Template = os.path.dirname\
        (__file__) + '/A4-Portrait-ISO7200.svg';
        ###
        box5CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display bottom side view');
        box6CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display bottom side view');
        ###
        box5CloneView.Source = self.box5Clone;
        box6CloneView.Source = self.box6Clone;
        ###
        box5CloneView.Direction =  (0, 1, 0);
        box5CloneView.X = 160.0;
        box5CloneView.Y = 150.0;
        box6CloneView.Direction =  (1, 0, 0);
        box6CloneView.X = 160.0;
        box6CloneView.Y = 80.0;
        ###
        box5CloneView.Scale = box6CloneView.Scale = 0.1; # drawingScale;
        ###
        box5ClonePage.addObject(box5CloneView);
        box6ClonePage.addObject(box6CloneView);
        # Change page texts (Izmenit' tekst stranitsy)
        box5CloneTexts = box5ClonePage.EditableTexts;
        box6CloneTexts = box6ClonePage.EditableTexts;
        # Author (avtor)
        box5CloneTexts[0] = "FreeCAD NG300 case";
        box6CloneTexts[0] = "FreeCAD NG300 case";
        # Drawing name (Nazvaniye chertezha)
        box5CloneTexts[1] = "Display bottom side";
        box6CloneTexts[1] = "Display bottom side";
        # Scale (Masshtab)
        box5CloneTexts[10] = str(box5CloneView.Scale); # str(drawingScale);
        box6CloneTexts[10] = str(box6CloneView.Scale); # str(drawingScale);
        # Drawing (Risovaniye)
        box5CloneTexts[12] = "2";
        box6CloneTexts[12] = "2";
        # Date (Data)
        box5CloneTexts[13] = datetime.datetime.now().\
        strftime("%Y-%m-%d");
        box6CloneTexts[13] = datetime.datetime.now().\
        strftime("%Y-%m-%d")
        # Version (Versiya)
        box5CloneTexts[14] = self.partVersion;
        box6CloneTexts[14] = self.partVersion;
        ###
        box5ClonePage.EditableTexts = box5CloneTexts;
        box6ClonePage.EditableTexts = box6CloneTexts;
        ###

    def displayRightSide(self):

        # Side part page (Stranitsa chasti storony)
        box1ClonePage = box2ClonePage = document.addObject\
        ('Drawing::FeaturePage', 'Display right side');
        box1ClonePage.Template = box2ClonePage.Template =\
        os.path.dirname(__file__) + '/A4-Portrait-ISO7200.svg';
        ###
        box1CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display right side view');
        box2CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display right side view');
        ###
        box1CloneView.Source = self.box1Clone;
        box2CloneView.Source = self.box2Clone;
        ###
        box1CloneView.Direction = (1, 0, 0);
        box1CloneView.X = 160.0;
        box1CloneView.Y = 130.0;
        box2CloneView.Direction = (0, 1, 0);
        box2CloneView.X = 160.0;
        box2CloneView.Y = 80.0;
        ###
        box1CloneView.Scale = box2CloneView.Scale = 0.1; # drawingScale;
        ###
        box1ClonePage.addObject(box1CloneView);
        box2ClonePage.addObject(box2CloneView);
        # Change page texts (Izmenit' tekst stranitsy)
        box1CloneTexts = box1ClonePage.EditableTexts;
        box2CloneTexts = box2ClonePage.EditableTexts;
        # Author (avtor)
        box1CloneTexts[0] = "FreeCAD NG300 case";
        box2CloneTexts[0] = "FreeCAD NG300 case";
        # Drawing name (Nazvaniye chertezha)
        box1CloneTexts[1] = "Display right side";
        box2CloneTexts[1] = "Display right side";
        # Scale (Masshtab)
        box1CloneTexts[10] = str(box1CloneView.Scale); # str(drawingScale);
        box2CloneTexts[10] = str(box2CloneView.Scale); # str(drawingScale);
        # Drawing (Risovaniye)
        box1CloneTexts[12] = "3";
        box2CloneTexts[12] = "3";
        # Date (Data)
        box1CloneTexts[13] = datetime.datetime.now().\
        strftime("%Y-%m-%d");
        box2CloneTexts[13] = datetime.datetime.now().\
        strftime("%Y-%m-%d");
        # Version (Versiya)
        box1CloneTexts[14] = self.partVersion;
        box2CloneTexts[14] = self.partVersion;
        ###
        box1ClonePage.EditableTexts = box1CloneTexts;
        box2ClonePage.EditableTexts = box2CloneTexts;
        ###

    def displayBackSide(self):

        box3ClonePage = box4ClonePage = document.addObject\
        ('Drawing::FeaturePage', 'Display back side');
        box3ClonePage.Template = box4ClonePage.Template =\
        os.path.dirname(__file__) + '/A4-Portrait-ISO7200.svg';
        ###
        box3CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display back side');
        box4CloneView = document.addObject\
        ('Drawing::FeatureViewPart', 'Display back side');
        ###
        box3CloneView.Source = self.box3Clone;
        box4CloneView.Source = self.box4Clone;
        ###
        box3CloneView.Direction = (1, 0, 0);
        box3CloneView.X = 50;
        box3CloneView.Y = 94;
        box4CloneView.Direction = (0, 0, 1);
        box4CloneView.X = 140.0;
        box4CloneView.Y = 150.0;
        ###
        box3CloneView.Scale = box4CloneView.Scale = 0.2; # drawingScale;
        ###
        box3ClonePage.addObject(box3CloneView);
        box4ClonePage.addObject(box4CloneView);
        # Change page texts (Izmenit' tekst stranitsy)
        box3CloneTexts = box3ClonePage.EditableTexts;
        box4CloneTexts = box4ClonePage.EditableTexts;
        # Author (avtor)
        box3CloneTexts[0] = "FreeCAD NG300 case";
        box4CloneTexts[0] = "FreeCAD NG300 case";
        # Drawing name (Nazvaniye chertezha)
        box3CloneTexts[1] = "Display back side";
        box4CloneTexts[1] = "Display back side";
        # Scale (Masshtab)
        box3CloneTexts[10] = str(box3CloneView.Scale); # str(drawingScale);
        box4CloneTexts[10] = str(box4CloneView.Scale); # str(drawingScale);
        # Drawing (Risovaniye)
        box3CloneTexts[12] = "4";
        box4CloneTexts[12] = "4";
        # Date (Data)
        box3CloneTexts[13] = datetime.datetime.now().\
        strftime("%Y-%m-%d");
        box4CloneTexts[13] = datetime.datetime.now().\
        strftime("%Y-%m-%d");
        # Version (Versiya)
        box3CloneTexts[14] = self.partVersion;
        box4CloneTexts[14] = self.partVersion;
        ###
        box3ClonePage.EditableTexts = box3CloneTexts;
        box4ClonePage.EditableTexts = box4CloneTexts;     

##############################################################################################

class NG300BatteryCase(TenBatteriesCase):
    """NG-300 Battery Case0"""
    def __init__(self, row_betweenBattery, boxThickness, 
                 additionalHeight, rotation, x, y, z,
                 scale_by_x, scale_by_y, scale_by_z):
        TenBatteriesCase.__init__(self, 170, 135, 470, row_betweenBattery, 
                                 boxThickness, additionalHeight, rotation, 
                                 x, y, z, scale_by_x, scale_by_y, scale_by_z)

battery = NG300BatteryCase(20, 18, 0, 0, 0, 0, 1, 1, 1, 1)
battery.display3D()
battery.displayBottomSide()
battery.displayBackSide()
battery.displayRightSide()

# To switch to the most convenient look (Chtoby pereklyuchit'sya na samyy udobnyy vid)
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxonometric()

# It is repeted to draw the document (Povtorno narisovat' dokument)
document.recompute()