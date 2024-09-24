
class vendedores():
    id_vendedor=0
    numero=0
    nombre=""
    apellidos=""
    ventas=0
    sueldo=0
    Email=""
    
    def vend_listas(self):
        print("listas--------------")
        nombres=["Susana", "emilia", "josefa", "jacinto", "yamileth"]
        for w in nombres:
            print(w)

    def vend_tuplas(self):
        print("tuplas--------------")
        vent=(14, 13, 3, 5, 10)
        for i in vent:
            print(i)
    
    def vend_conjuntos(self):
        print("conjuntos--------------")
        sueldos={2000, 1500, 200, 500, 1000 }
        for u in sueldos:
            print(u)
    
    def vend_diccionarios(self):
        print("diccionarios--------------")
        dict_venta = {
            " susana:": "susiiroz2@gmail.com",
            "josefa: ": "josefarrez28@gmail.com",
            "emilia: ": "emiluevano224@gmail.com",
            " jacinto:": "jacissvegy101@gmail.com",
            "yamileth: ": "yamiramirez1311@gmail.com" 
        }
        for x,y in dict_venta.items():
            print(x, y)
mostrar_datos=vendedores()
susana=vendedores()
susana.id_vendedor=1139
susana.numero=6568997430
susana.nombre="Susana lili"
susana.apellidos="Quiroz"
susana.sueldo=2000
susana.Email="susiiroz2@gmail.com"
print("resultado para susana-------")
print(f"ID: {susana.id_vendedor}")
print(f"Numero telefonico: {susana.numero}")
print(f"Nombre(s): {susana.nombre}")
print(f"Apellidos(s): {susana.apellidos}")
print(f"sueldo: {susana.sueldo}")
print(f"sueldo: {susana.Email}")

emilia=vendedores()
emilia.id_vendedor=1140
emilia.numero=6569977230
emilia.nombre="Emilia Jasmin"
emilia.apellidos="luevano Zuñiga"
emilia.sueldo=1500
emilia.Email="emiluevano224@gmail.com"
print("resultado para Emilia-------")
print(f"ID: {emilia.id_vendedor}")
print(f"Numero telefonico: {emilia.numero}")
print(f"Nombre(s): {emilia.nombre}")
print(f"Apellidos(s): {emilia.apellidos}")
print(f"sueldo: {emilia.sueldo}")
print(f"sueldo: {emilia.Email}")
        
yamileth=vendedores()
yamileth.id_vendedor=1140
yamileth.numero=6569977230
yamileth.nombre="yamileth cristal"
yamileth.apellidos="zuñiga coronel"
yamileth.sueldo=500
yamileth.Email="yamiramirez1311@gmail.com"
print("resultado para Emilia-------")
print(f"ID: {yamileth.id_vendedor}")
print(f"Numero telefonico: {yamileth.numero}")
print(f"Nombre(s): {yamileth.nombre}")
print(f"Apellidos(s): {yamileth.apellidos}")
print(f"sueldo: {yamileth.sueldo}")
print(f"sueldo: {yamileth.Email}")

mostrar_datos.vend_listas()
mostrar_datos.vend_tuplas()
mostrar_datos.vend_diccionarios()
mostrar_datos.vend_conjuntos()
    
    