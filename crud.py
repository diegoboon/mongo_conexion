import pymongo


def conectar_a_base_de_datos():
    client = pymongo.MongoClient("mongodb+srv://,tu usuario aquí>:<tu contraseña aquí>@cluster0.dzjexhg.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
    db = client.test
    return db


def crear_documento(nombre, edad, ciudad):
    document = {
        "name": nombre,
        "age": edad,
        "city": ciudad
    }
    return document


def insertar_documento(db, document):
    """Inserta un documento en una colección MongoDB."""

    db["people"].insert_one(document)


def actualizar_documento(db, collection, criterio, document):
    """Actualiza un documento en una colección MongoDB."""

    db[collection].update_one(criterio, {"$set": document})


def eliminar_documento(db, collection, criterio):
    """Elimina un documento en una colección MongoDB."""

    db[collection].delete_one(criterio)


def consultar_documentos(db):
    """Consulta los documentos de una colección MongoDB."""

    cursor = db.people.find()
    for document in cursor:
        print(document)


if __name__ == "__main__":
    # Conecta a la base de datos
    db = conectar_a_base_de_datos()

    # Opciones
    opciones = ["Agregar", "Editar", "Eliminar", "Consultar"]

    # Elige una opción
    while True:
        print("\n")
        for opcion in opciones:
            print(opcion)
        opcion = input("Elige una opción: ")

        # Agrega un documento
        if opcion == "Agregar":
            nombre = input("Ingresa tu nombre: ")
            edad = int(input("Ingresa tu edad: "))
            ciudad = input("Ingresa tu ciudad: ")
            document = crear_documento(nombre, edad, ciudad)
            insertar_documento(db, document)

        # Edita un documento
        elif opcion == "Editar":
            nombre = input("Ingresa el nombre del documento que deseas editar: ")
            edad = input("Ingresa la nueva edad: ")
            ciudad = input("Ingresa la nueva ciudad: ")
            criterio = {"name": nombre}
            document = {
                "age": edad,
                "city": ciudad
            }
            actualizar_documento(db, "people", criterio, document)

        # Elimina un documento
        elif opcion == "Eliminar":
            nombre = input("Ingresa el nombre del documento que deseas eliminar: ")
            criterio = {"name": nombre}
            eliminar_documento(db, "people", criterio)

        # Consulta los datos
        elif opcion == "Consultar":
            consultar_documentos(db)

        # Salir
        else:
            print("Saliendo...")
            break
