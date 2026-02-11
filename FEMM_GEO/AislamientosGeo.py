import femm
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def drawminiangulo(AltVentanaNucleo,AltAxi, Radial, DiamInt, axial_cond,kraft,dy):
    l_recomp = Radial - 19 * 2 - 4
    ax = round(axial_cond - 1)

    if kraft==0:

        # --------MINI ANGULOS SUPERIORES-------
        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        # corners
        # crea corner sup izq

        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax + dy)
        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 + dy, 0.5 + 1)

        # --------MINI ANGULOS INFERIORES-------
        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 + dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)

        # corners
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax + dy)

        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + dy, 0.5 + 1)

    else:
        l_recomp = Radial - 19 * 2 - 4

        # --------MINI ANGULOS SUPERIORES-------
        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo + AltAxi) / 2+ dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        # corners
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy, 0.5 + 1 + kraft / 2)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+ dy)
        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+ dy, 0.5 + 1 + kraft / 2)

        # --------MINI ANGULOS INFERIORES-------

        # relleno compensador
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2, (AltVentanaNucleo - AltAxi) / 2+ dy)

        # miniangulo anillo
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy,
                         DiamInt / 2 + Radial / 2 - l_recomp / 2 - 2 - 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)

        # corners
        # crea corner sup izq
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy, 0.5 + 1 + kraft / 2)

        # miniangulo capa
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)
        femm.ei_drawline(DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 20, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy,
                         DiamInt / 2 + Radial / 2 + l_recomp / 2 + 2 + 19, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+ dy)

        # corners
        # crea corner sup derc
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+ dy, 0.5 + 1 + kraft / 2)

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
def drawanilloangular(AltVentanaNucleo,AltAxi, Radial, DiamInt, axial_cond,kraft,dy):
    ax = round(axial_cond - 1)
    if kraft== 0:
        #--------ANILLO ANGULAR SUPERIOR-----------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5  + 1)
        # --------ANILLO ANGULAR INFERIOR-----------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 ,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5 + 1)

    else:

        # --------ANILLO ANGULAR SUPERIOR--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo + AltAxi) / 2 + 1 - ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5+ kraft/2+1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo + AltAxi) / 2 + 1+dy, 0.5+ kraft/2+1)
        # --------ANILLO ANGULAR INFERIOR--------
        femm.ei_drawline(DiamInt / 2, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 - 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, DiamInt / 2 + Radial + 1,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_drawline(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy, DiamInt / 2 + Radial,(AltVentanaNucleo - AltAxi) / 2 - 1 + ax+dy)
        femm.ei_createradius(DiamInt / 2 - 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5+ kraft/2+1)
        femm.ei_createradius(DiamInt / 2 + Radial + 1, (AltVentanaNucleo - AltAxi) / 2 - 1+dy, 0.5+ kraft/2+1)

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------