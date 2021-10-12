

<br/><br/>


# Plataforma PYTHON que usa Machine Learning e Inteligencia Artificial para pillar a los malos

## 1. Descripción de la plataforma

Esta plataforma ha sido desarrollada por la brigada de ciberinteligencia de la policía siguiendo el patron MVC (Modelo-Vista-Controlador) con Flask y en el ODM para Python: MongoEngine. Sirve para conectarla a una base de datos de mensajes y la plataforma usando las técnicas más avanzadas de Machine Learning e Inteligencia Artificial podrá a partir de un nombre de usuario obtener su identidad real.

La **vista** es una interfaz web basada en HTML y CSS que permite realizar las acciones deseadas sobre los mensajes.

El **modelo** es la representación de la información de los mensajes. El modelo que usa esta plataforma está en el fichero model.py. Contiene solo algunos campos porque el esquema es dinámico y flexible.

```
class Mensajes(db.DynamicDocument):
    url = db.StringField()
    date = db.DateTimeField()
    content = db.StringField()
    renderedContent = db.StringField()
```

El **controlador** ejecuta acciones del servidor. Tiene dos rutas, "/" y "/process". Esta es la parte a personalizar para poder enganchar esta plataforma a cualquier base de datos de mensajes (Twitter, Telegram, Whatsapp, emails, ...). La ruta "/" debe llenar la variable "tweets" con los mensajes del username adecuado para que la plataforma los analice. Esta query a la base de datos debe hacerse específicamente para cada caso policial.


## 4. Descargar e instalar el código de la plataforma

Abra un terminal en su ordenador y siga los siguientes pasos.

El proyecto debe clonarse en el ordenador desde el que se está trabajando con:

```
$ git clone https://github.com/BBDD-ETSIT/atrapamalos
```

y entrar en el directorio de trabajo

```
$ cd atrapamalos
```

Una vez dentro de la carpeta, se instalan las dependencias con:

```
$ pip install requirements.txt
```

IMPORTANTE: En este momento lo ideal es abrir el código de la plataforma en un editor de código (Atom, Sublime Text, ...) y observar cómo se llama la base de datos y la colección. Habrá que restaurar el dump en JSON que tengamos con ese nombre de base de datos y esa colección para que la plataforma conecte a MongoDB adecuadamente.
También tendremos que implementar la query que está en la ruta "/" para que haga un find y filtre los mensajes con el username adecuado y los cargue en la variable "tweets".

Por último podemos arrancar la plataforma con:

```
$ python app.py
```

Abra un navegador y vaya a la url "http://localhost:8001" para ver la plataforma funcionando. Si la plataforma puede conectar a la base de datos y colección correcta y recibe filtrados los mensajes del username correcto, usará la Machine Learning e Inteligencia Artificial para devolver el nombre real del usuario buscado.

