import pymongo #Importamos pymongo para poder conectarnos a MongoDB
import datetime #Importamos datetime para poder usar la fecha de creación y modificación de los artículos
from os import system

my_client = pymongo.MongoClient("mongodb://localhost:27017/") #Creamos una conexión a MongoDB

print("=====Bases de datos existentes=====")
#Imprimimos con un for la lista de la base de datos
for db in my_client.list_database_names():
    print("-",db)
select_database = input("Ingresa el nombre de la base de datos: ")#Pedimos seleccionar la base de datos y la asignamos a su respectiva variable
system("cls")


print("=====Colecciones existentes=====")
#Imprimimos con un for la lista de las colecciones de la base de datos
for collection in my_client[select_database].list_collection_names():
    print("-",collection)
mydb = my_client[select_database] #Le asignamos a la variable mydb la base de datos que seleccionamos
select_collection = input("Ingresa el nombre de la colección: ") #Pedimos seleccionar la coleccion y la asignamos a su respectiva variable	
system("cls")
mytb = mydb[select_collection] #Le asignamos a la variable mytb la coleccion que seleccionamos


#Declaramos una funcion para agregar un artículo donde asignaremos los valores que el usuario ingrese a cada variable
def agregar_articulo(): 
    id_articulo = int(input("Ingresa el ID del articulo\n"))
    nombre = input("Ingresa un nombre para el artículo\n")
    descripcion = input("Ingresa la descripciono del artículo\n")
    precio = input("Ingresa el precio del artículo\n")
    nombre_proveedor= input("Ingresa el nombre del proveedor\n")
    telefono_proveedor = input("Ingresa el telefono del proveedor\n")
    email_cliente = input("Ingresa el email del cliente\n")
    stars = int(input("Ingresa la cantidad de estrellas\n"))
    post = {"_id": id_articulo,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "fecha": datetime.datetime.now(), #Decidí poner la fecha de creación del artículo como dato extra
            "modificacion": datetime.datetime.now(), #Y su fecha de modificación para llevar un control de los cambios
            "Proveedor": {"nombre": nombre_proveedor, "telefono": telefono_proveedor},
            "Reseña": [{"cliente": { "email": email_cliente}, "stars": stars }],
            }
    x = mytb.insert_one(post)
    print("El ID del producto agregado es: ", x.inserted_id)
    #Imprimimos el resultado de la inserción
    
#Declaramos una funcion para borrar un articulo
def borrar_articulo():
    id_del = int(input("Escribe el ID del post a eliminar\n"))
    mytb.delete_one({"_id": id_del})

#Declaramos una funcion para editar un articulo
def editar_articulo():
    id_edit = int(input("Copia y pega el ID del post a modificar\n"))
    nombre = input("Ingresa el nuevo nombre del artículo\n")
    descripcion = input("Ingresa la nueva descripción del artículo\n")
    precio = input("Ingresa el nuevo precio del artículo\n")
    post_updated = mydb.articulo.update_one(
        {"_id": id_edit},
        {
            "$set": {

                "nombre": nombre,
                "descripcion": descripcion,
                "precio": precio,
                "modificacion": datetime.datetime.now() #Le asignamos la fecha de modificación para saber cuando fue editado
            }
        }
    )
    print("Artículos modificados: %s" % str(post_updated.matched_count))

#Declaramos una funcion para buscar un articulo
def imprimir_articulos(mytb):
        cursor = mytb.find()
        for document in cursor:
            print("id: %s\t NOMBRE: %s\t" % (str(document['_id']), document['nombre']))

#Declaramos una funcion para llamar al menú de opciones
def main():
    
    while True: #Con un while true, repetimos el menú hasta que el usuario decida salir
        print("=====Menú de opciones=====")
        print ("""
        1.- Agregar artículo
        2.- Borrar artículo
        3.- Editar un artículo
        4.- Buscar artículo
        5.- Salir
        """)
        
        opcion = input("Escribe la opcion\n") #Pedimos la opción que el usuario desee realizar y mediante if, elif y else mandamos llamar a la funcion correspondiente
        system("cls")
        if opcion == "1":
            agregar_articulo()
            system("pause")
            system("cls")
            
        elif opcion == "2":
            print("--Artículos--")
            for document in mytb.find():
                print("id: %s\t NOMBRE: %s\t PRECIO: %s\t" % (str(document['_id']), document['nombre'], document['precio']))
            borrar_articulo()
            system("pause")
            system("cls")
        elif opcion == "3":
            editar_articulo()
        elif opcion == "4":
            
            print("<<<<-ids y nombre de productos->>>>")
            
            for document in mytb.find():
                print("id: %s\t NOMBRE: %s\t PRECIO: %s\t" % (str(document['_id']), document['nombre'], document['precio']))
            system("pause")
            system("cls")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")
            system("pause")
            system("cls")
         #Limpiamos la pantalla para que no se acumulen las opciones

if __name__ == "__main__":
    main()#Llamamos a la funcion main para que se ejecute el menú