
# *******************SCRIPT PARA EL TEST DE GEOMETRIA ANTES DE IMPLEMENTARSE EN EL ARCHIVO DEL PROYECTO*******************

import femm


from  CoreGeo import drawcore
from  windingmaterials import materials
from AislamientosGeo import  drawsectoranillo_inf, drawsectoranillo_sup, drawsectorcapa_sup, drawsectorcapa_inf
from  DevanadosGeo import drawdevanado,drawdev_fullreg,drawanillo_eqinf,drawanillo_eqsup,drawanillo_eqsup_reginf,drawanillo_eqinf_regsup

femm.openfemm()
femm.newdocument(1)  # electrostatics
femm.ei_probdef("millimeters", "axi", 1e-8, 0, -30)
materials()



 # --------------------------------------|COMIENZO DIBUJO|-----------------------------------------

    #información general del dibujo para dibujar el núcleo
    #CabecerasDevSup = [185, 60, 140 + 80, 495]
    #CabecerasDevinf = [185, 60, 80+30, 495]
    #AlturasAxiDev = [2000, 2250, 2210, 1380]

AltVentanaNucleo = 2140
AnchVentanaNucleo = 545
DiametroNucleo = 640
CabSupAT=120 + 130
CabInfAT=120+30

#Para dibujar el nucleo se necesita tener toras las cabeceras y alturas en arreglos
dy=drawcore(DiametroNucleo, AnchVentanaNucleo, AltVentanaNucleo,  CabSupAT, CabInfAT)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------Dibujando dev LV-----------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
AltAxi=1770
Radial=58
DiamInt=974
axial_cond=16.486
Boundaryvoltage=0.0
cabsup=110
cabinf=110

kraft=2

NumTiras = 28
AnchoEspaciador = 30
EsptiraInt = 8
EsptiraExt = 6



drawdevanado("BoundLV",Boundaryvoltage,AltVentanaNucleo,AltAxi,Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,NumTiras,AnchoEspaciador, EsptiraInt,EsptiraExt,dy)



#------------------------------------------DIBUJAR ANILLO EQ Y SECTORES - SUPERIORES----------------------------
Radial=58
DiamInt=974
AltAxi=1770


h1=8 #distancia entre bobina y anillo eq
radiosint=[2,2,9,9]
hanillo_eq=22
offset=drawanillo_eqsup(AltAxi,AltVentanaNucleo,DiamInt,radiosint,Radial,0,h1,hanillo_eq,dy)

h1=9 #distancia de separación entre el elemento inferior(anillo, sector, arandela, etc)
rint=15
offset=drawsectoranillo_sup(DiamInt,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)

h1=8 #distancia de separación entre el elemento inferior
rint=20
offset=drawsectorcapa_sup(DiamInt,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)


#------------------------------------------DIBUJAR ANILLO EQ Y SECTORES - INFERIORES----------------------------
Radial=58
Diamint=974
AltAxi=1770



h1=8 #distancia entre bobina y anillo eq
radiosint=[2,2,5,5]
hanillo_eq=22
offset=drawanillo_eqinf(AltAxi,AltVentanaNucleo,Diamint,radiosint,Radial,0,h1,hanillo_eq,dy)

h1=9 #distancia de separación entre el elemento inferior(anillo, sector, arandela, etc)
rint=15
offset=drawsectoranillo_inf(Diamint,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)

h1=8 #distancia de separación entre el elemento inferior
rint=15
offset=drawsectorcapa_inf(Diamint,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)


#------------------------------------------REG AT----------------------------
AltAxi=1770
Radial=58
DiamInt=1200
axial_cond=16.486
BoundaryvoltageSup=0.0
BoundaryvoltageInf=0.0
cabsup=110
cabinf=110

kraft=2
NumTiras = 28
AnchoEspaciador = 30
EsptiraInt = 8
EsptiraExt = 6

separacion=500


drawdev_fullreg("BoundREGSup","BoundREGInf",BoundaryvoltageSup,BoundaryvoltageInf,AltVentanaNucleo,AltAxi, Radial,axial_cond, DiamInt,kraft,cabsup,cabinf,dy,separacion)

h1=8 #distancia entre bobina y anillo eq
radiosint=[2,2,9,9]
hanillo_eq=22
offset=drawanillo_eqsup(AltAxi,AltVentanaNucleo,DiamInt,radiosint,Radial,0,h1,hanillo_eq,dy)

h1=8 #distancia de separación entre el elemento inferior
rint=20
offset=drawsectoranillo_sup(DiamInt,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)

h1=8 #distancia de separación entre el elemento inferior
rint=15
offset=drawsectorcapa_sup(DiamInt,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)




h1=8 #distancia entre bobina y anillo eq
radiosint=[2,2,9,9]
hanillo_eq=22
offset=drawanillo_eqinf(AltAxi,AltVentanaNucleo,DiamInt,radiosint,Radial,0,h1,hanillo_eq,dy)

h1=8 #distancia de separación entre el elemento inferior
rint=20
offset=drawsectoranillo_inf(DiamInt,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)

h1=8 #distancia de separación entre el elemento inferior
rint=20
offset=drawsectorcapa_inf(DiamInt,AltAxi,AltVentanaNucleo,Radial,offset,h1,rint,dy)


h1=8 #distancia entre bobina y anillo eq
radiosint=[2,2,9,9]
hanillo_eq=22
drawanillo_eqsup_reginf(AltVentanaNucleo,AltAxi, DiamInt, radiosint, Radial, 0, h1, hanillo_eq,separacion, dy)

h1=8 #distancia entre bobina y anillo eq
radiosint=[2,2,9,9]
hanillo_eq=22
drawanillo_eqinf_regsup(AltVentanaNucleo,AltAxi, DiamInt, radiosint, Radial, 0, h1, hanillo_eq,separacion, dy)





femm.ei_zoomnatural()


input("Dibujo OK!. Presiona Enter para salir...")
