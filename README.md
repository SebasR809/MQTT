# PROTOCOLO MQTT
### ¿qué es MQTT?:
MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero y de bajo consumo de energía diseñado para la comunicación entre dispositivos conectados a Internet de las Cosas (IoT). Permite que los dispositivos envíen y reciban mensajes de forma eficiente y confiable, incluso en redes con ancho de banda limitado.

El agente MQTT es el sistema de back-end que coordina los mensajes entre los diferentes clientes. Las responsabilidades del agente incluyen recibir y filtrar mensajes, identificar a los clientes suscritos y presentarles todos los mensajes publicados.

Su funcionamiento se resumen mejor en la siguiente imagen:

![mqtt](https://www.smartnet.com.co/wp-content/uploads/2021/03/protpubsus.jpg "mqtt")

### Código Adjunto:
El codigo adjunto se divide en tres archivos con una funcionalidad distinta, y para poder hacer la conexión son explicitamente necesarios los tres recursos:

**- database.py:**

  En este archivo se encuentra toda la conexión con la base de datos, se usa la libreria pyodbc debido a que se almacena la información en una base de datos SQL server; la función recibe 4 parametros fundamentales:
  - Server: el nombre de nuestro server, puede ser local o público
  - Database: El nombre de la base de datos que estamos usando
  - Username: El usuario con el cual nos podemos logear al servidor
  - Password: Y por último contamos con la contraseña del anterior usuario
>  Tambien se debe tener el cuenta el controlador que se este usando o sea necesario para evitar errores de conexión; Está definido como "ODBC Driver 17 for SQL Server"por defecto

 **- mqtt.py:**
 
 En este archivo se encuentra todo lo necesario para poder realizar la conexión con el broker MQTT, se usan las siguientes librerias (json, sys, paho.mqtt.client, etc); 
 

- Cliente: En las primeras líneas se define el cliente que se va a usar para realizar la comunicación con el mqtt, este por predeterminado está en Sebastian como un identificador fijo; el identificador puede ser fijo o generado aleatoriamente pero es necesario que sea único.

- Broker: el cliente debe de estar fijo en la conexión, para la conexión al broker usamos el metodo *con()* donde solamente tendremos que proporcionar el host y el puerto por el cual se está lanzando, si para la conexión se requiere un login se usara la linea de codigo de la linea 9, aca se proporciona user y pass,  si es exitoso llamara a las siguientes funciones:

- Tema / Topic: el cliente se va a suscribir al tema que este definido en la función *on_connect()* ; solo definimos el topic si son varios solamente copiar y pegar la linea de codigo y definir el qos(Quality of Service) de acuerdo a la necesidad.

- Mensaje: si todo lo anterior sale de manera correcta, obtendremos cada vez que se publique, un mensaje el cual lo recibimos en un formato de tipo JSON en la función *on_message()* , este mensaje es tratado y convertido en un diccionario de python donde se crea el script sql para la inserción en base de datos
> Es de suma importancia que los campos se publiquen de acuerdo a como está creada cada columna de la tabla en la bd, de lo contrario no se guardara información y saldra un error

Si no hubo ningun problema, se ejecutara el script guardando en la base de datos la información recibida.

**- Interface.pyw:**
En este archivo se encuentra la interfaz gráfica para usar la aplicación,  este es el archivo principal del programa donde se encuentra el metodo Main, posee dos metodos:
- main(): se uso la libreria tkinter para desarrollar la interfaz gráfica, usa dos variables determinadas root y frame la mayoría de lo que se encuentra en este metodo son estilos para actualizarlos, ver más de la libreria.
Realice un metodo llamado *hide()* que lo único que hace es detectar si el boton principal es oprimido,si la condición se cumple, se detiene la conexión con el broker (se usa el metodo *stop()* importado de la mqtt.py) y se cambia el color del botón y texto.

- rutas(): este metodo se usa para detectar donde esta el icono que se usa para la interfaz 


### Creación de ejecutable
Para crear un ejecutable en python se usa la libreria pyinstaller, debido a que son 3 archivos distintos lo que necesitamos para que el codigo funcione los pasos para crear un .exe son los siguientes:
En consola agregamos el siguiente codigo:

pyinstaller --name=MQTTECI --onefile Interface.pyw

> - name: definir el nombre con el cual queremos llamar a nuestro .exe

> - onefile: empaquetar todos los archivos y carpetas para que solo se muestre un unico archivo

Se habra creado una rchivo llamado MQTTECI.spec, lo abrimos y en la linea datas(linea 11) agregamos los otros dos archivos que necesitamos, que quede de la siguiente manera:

datas=[('database.py','.'),('mqtt.py','.')],

Por último ejecutamos en consola la siguiente linea de codigo:

pyinstaller MQTTECI.spec

Ya tendriamos en la carpeta dist nuestro ejecutable


