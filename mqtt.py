import json
import sys
import paho.mqtt.client
from datetime import datetime
import database
from json.decoder import JSONDecodeError

client = paho.mqtt.client.Client(client_id='Sebastian', clean_session=False)
client.username_pw_set(username="ECI", password="Equipos2023-+")

def on_connect(client, userdata, flags, rc):
    msg('connected (%s)' % client._client_id)
    client.subscribe(topic = '/5731076765449/ECIHWM', qos=2)


def on_message(client, userdata, message):
    try:
        msg('--------------------------------------------------------------------')
        
        # if(database.connection):
        #     msg('Se conecto a la base de datos')
        # else:
        #     msg('Error en la conexion a la base de datos')
        
        # print('Topic: %s' % message.topic) print('Qos: %d' % message.qos) print('Payload: %s' % message.payload)
        a = json.loads(message.payload)
        msg('msg: %s' % a)
            
        for dat in a:

            msg('Ingreso al for')

            columnas = ""
            values = ""
            keys = list(dat.keys())
            vals = list(dat.values())
            c= 0

            for i in vals:
                columnas += keys[c] + ","
                values += "'" +str(vals[c]) + "',"
                c= c +1
                msg('Ingreso al for 2')

            conexion = database.connection()
            con=conexion.cursor()
            
            sql = "INSERT INTO dbo.MQTTSensor(topic,"+ columnas[0:-1] +",datetimePub) values ('"+message.topic+"',"+values[0:-1]+",getdate())"
            msg(sql)
            con.execute(sql)

            if(con.rowcount > 0):
                msg("Se inserto el campo en la base de datos")
            else:
                msg("ERROR en la inserción")

            con.commit()
            con.close()

    except Exception as e:
        msg("error "+ str(e.__context__))
        

    

def con():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='192.168.0.11', port=8080)
    #client.loop_forever()
    client.loop_start()

def stop():
    client.disconnect()
    client.loop_stop()
    sys.exit()

def msg(message):
    f = open('log.txt','a')
    f.write('\n'+ message)
    f.close()