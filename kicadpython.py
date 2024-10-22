from skip import Schematic
sch = Schematic("/Users/Desktop//Untitled/Untitled.kicad_sch")#set up the path of the program 


a = sch.symbol.R2.clone()#add a elements(You can only clone a excited elements)

a.move(50,100)# move the symbol(x,y)

sch.symbol.R1.Value.value = '100k' # change the value of R1


sch.write("/Users/Desktop//Untitled/Untitled.kicad_sch")#you have to rewrite the program in order to save the changes you made



                                                                                                                                          