import femm
from DevanadosGeo import drawdevanado
from CoreGeo import drawcore
from windingmaterials import materials
from AislamientosGeo import drawcilindro


def ejecutar_simulacion(datos):
    """
    datos: Diccionario con todos los parametros de la interfaz
    """
    # 1. Configuración inicial
    femm.openfemm()
    femm.newdocument(1)
    materials()

    # Configuración del problema
    if datos['tipo_simulacion'] == 'Planar':
        femm.ei_probdef('millimeters', 'planar', 1e-8, 1e6, 30)
    else:
        femm.ei_probdef('millimeters', 'axi', 1e-8, 0, 30)

    # 2. Dibujando nucleo
    dy = drawcore(
        datos['nucleo_diametro'],
        datos['nucleo_ancho'],
        datos['nucleo_alto'],
        datos['nucleo_cab_sup'],
        datos['nucleo_cab_inf']
    )

    # 3. Dibujando Devanado Serie (si existe en los datos)
    if datos['serie_activo']:
        drawdevanado(
            "boundary1",
            datos['serie_voltage'],
            datos['nucleo_alto'],  # AltVentanaNucleo
            datos['serie_alt_axi'],
            datos['serie_radial'],
            datos['serie_axial_cond'],
            datos['serie_diam_int'],
            datos['serie_kraft'],
            dy
        )

    # 4. Dibujando Devanado Común
    if datos['comun_activo']:
        drawdevanado(
            "boundary2",
            datos['comun_voltage'],
            datos['nucleo_alto'],
            datos['comun_alt_axi'],
            datos['comun_radial'],
            datos['comun_axial_cond'],
            datos['comun_diam_int'],
            datos['comun_kraft'],
            dy
        )

    # 5. Dibujando Cilindros (Ejemplo iterativo)
    # Suponiendo que pasamos una lista de cilindros
    for cil in datos['cilindros']:
        # cil es un diccionario: {'dim_int': 300, 'alt_axi': 600, 'radial': 3}
        drawcilindro(cil['dim_int'], datos['nucleo_alto'], cil['alt_axi'], cil['radial'], dy)

    # 6. Finalizar
    femm.ei_zoomnatural()
    # femm.ei_saveas("estudio_auto.fee") # Opcional: guardar automáticamente
    print("Geometría generada con éxito.")