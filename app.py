from models.modelo import Modelos, ListaModelos

try:
    # Creamos la lista 
    lista = ListaModelos()

    # Creo el modelo SEAT
    modelo = Modelos('SEAT', 'SEAT MATORELL')
     # Lo añado a la lista
    lista.add(modelo)
    # Destruyo el objeto
    del modelo 

    # Creo el modelo RENAULT
    modelo = Modelos('RENAULT', 'RENAULT')
    # Lo añado a la lista
    lista.add(modelo)
    # Destruyo el objeto
    del modelo 

    try:
        # Me devuelve el modelo SEAT (en caso que esté inactivo, me devolverá un None)
        modelo = lista.getItem('SEAT')
        if (modelo is not None):
            print(modelo.descripcion)
        else:
            print('El modelo está inactivo')
    except:
        print('fallo')
finally:
    # Libero la lista
    del lista   
	

