# MongoDB CRUD Operations with Python

Este repositorio contiene un conjunto de scripts en Python que demuestran operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MongoDB utilizando la biblioteca `pymongo`.

## Requisitos

Asegúrate de tener Python y la biblioteca `pymongo` instalados en tu entorno antes de ejecutar los scripts.

```bash
pip install pymongo
```

## Configuración de la Base de Datos

1. Crea una cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) si aún no tienes una.
2. Configura un clúster en MongoDB Atlas.
3. Obtén la cadena de conexión de tu clúster y reemplaza `<tu usuario aquí>` y `<tu contraseña aquí>` en la función `conectar_a_base_de_datos` en el archivo `main.py`.

## Uso

Ejecuta `main.py` y sigue las instrucciones en el menú para realizar operaciones en la base de datos MongoDB.

```bash
python main.py
```

## Operaciones Disponibles

1. **Agregar**: Agrega un nuevo documento a la colección "people".
2. **Editar**: Modifica la información de un documento existente en la colección "people".
3. **Eliminar**: Elimina un documento de la colección "people" según el nombre.
4. **Consultar**: Muestra todos los documentos en la colección "people".

## Contribuir

Siéntete libre de contribuir al proyecto abriendo problemas o enviando solicitudes de extracción. ¡Toda contribución es bienvenida!

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

**¡Gracias por usar este script! Si encuentras algún problema o tienes sugerencias, no dudes en abrir un problema.**
