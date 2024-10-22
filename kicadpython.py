from skip import Schematic
sch = Schematic("/Users/Desktop//Untitled/Untitled.kicad_sch")
a = sch.symbol.R2.clone()#add a elements
a.move(50,100)
sch.symbol.R1.move(100,100)
sch.symbol.R1.Value.value = '100k' 
sch.write("/Users/Desktop//Untitled/Untitled.kicad_sch")


                                                                                                                                          
