Para ejecutar el script importar_madres se debe estar posicionado en la carpeta addons/saim/ y ejecutar:

    > python importar_madres.py

Se deben modificar las primeras lineas del script:

    username = 'admin' #the user
    pwd = '123321...'      #the password of the user
    dbname = 'SAIM'    #the database

Para que correspondan con el usuario, contraseña y nombre de la base de datos a la que se quieren importar los datos.

El script se alimentará de el archivo "madres.csv" que se encuentra en la misma carpeta saim/
