Para ejecutar el script poblar_estados.py se debe estar posicionado en la carpeta addons/saim/ y ejecutar:

    > python poblar_estados.py

Se deben modificar las primeras lineas del script:

    username = 'admin' #the user
    pwd = '123321...'      #the password of the user
    dbname = 'SAIM'    #the database

Para que correspondan con el usuario, contraseña y nombre de la base de datos a la que se quieren poblar los estados.

El script se alimentará del script geo.py que ya contiene todos los paises, estados, parroquias y municipios en formato diccionario, facilmente leible por el script.
