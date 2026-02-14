

import femm


def materials():

    oil=2.2
    Tiv=4.5
    weidmann=3.8
    Kraftsolid=3.2


    femm.ei_addmaterial('OilM', oil, oil, 0)
    femm.ei_addmaterial('TIV',  Tiv,  Tiv, 0)
    femm.ei_addmaterial('Weidmann',  weidmann,  weidmann, 0)
    femm.ei_addmaterial('kraftsolid',  Kraftsolid,  Kraftsolid, 0)


def asignmaterials(type,x,y,meshsize,group):

    femm.ei_addblocklabel(x, y)  # punto dentro
    femm.ei_selectlabel(x, y)
    femm.ei_setblockprop(type , 0, meshsize, group)
    femm.ei_clearselected()


def nomesh(x,y):
    GRUPO_FRONTERA=500
    femm.ei_addblocklabel(x, y)  # punto dentro
    femm.ei_selectlabel(x, y)
    femm.ei_setblockprop("<No Mesh>", 0, 0, GRUPO_FRONTERA)
    femm.ei_clearselected()
 #automesh = 0 y meshsize = 0 → FEMM interpreta que no quieres mallar esa región, y en la interfaz aparece como \<No Mesh\>, aunque hayas escrito 'OilM'.