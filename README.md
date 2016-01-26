# mongoapi
Prueba de código para utilizar Pyton + Tornado + Motor + Mongodb.
</br></br>

<b>Servicio RESTFul</b>
</br>
Expone 2 servicios:

- /users</br>
Retorna una lista de los correos de los usuarios.

- /usercount</br>
Retorna el conteo de usuarios en la base de datos.

<b>Formato de Respuesta:</b> </br></br>
{
  "data": {
  },
  "responseheader": {
    "message": "",
    "code": "" 
  }
}

<b>Base de Datos Mongo</b></br>
Se conecta a una BD de Mongo y asume tiene una colección "users" con documentos que llevan un campo "email".
