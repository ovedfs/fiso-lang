
# Fiso

Fiso es un pequeño lenguaje de programación para manejo de archivos de texto (escritos en lenguaje natural) desde la terminal/shell.

## Funcionalidades

**count**

Permite contar el número de palabras o letras de un archivo de texto.
```
# Obtener el total de palabras del archivo file.txt
fiso count -w file.txt

# Obtener el total de caracteres del archivo file.txt
fiso count -c file.txt
```

**summary**

Genera un resumen del contenido de un archivo de texto que puede guardarse en 
otro archivo o en memoria.
```
fiso summary fileInt.txt fileOut.txt
```

**translate**

Traduce el contenido de un archivo de texto de un lenguaje dado a otro.
```
fiso translate from=sp to=en fileIn.txt fileOut.txt
```

**speech**

Genera un archivo de audio en mp3 a partir del contenido de un archivo de texto.
```
fiso speech fileInt.txt fileOut.mp3
```

## Pruebas
Para simular el uso del lenguaje realiza lo siguiente:
* Descarga o clona el repositorio
* Puedes usar el archivo prueba.txt o agregar tu propio archivo de texto
* Desde la terminal ejecuta el archivo fiso.py de la siguiente forma:
    1) Para contar el número de palabras de un archivo
    ```
    py fiso.py count -w prueba.txt
    ```
    
    2) Para contar el número de caracteres de un archivo
    ```
    py fiso.py count -c prueba.txt
    ```
    
    3) Para traducir al inglés el contenido del archivo prueba.txt y guardar la traducción en el archivo prueba2.txt
    ```
    py fiso.py translate from=sp to=en prueba.txt prueba2.txt
    ```
    _Puedes traducir a otros idiomas y guardar las traducciones en otros archivos_
    ```
    py fiso.py translate from=en to=de prueba2.txt prueba3.txt
    ```
    
    4) Para generar un audio del archivo prueba.txt
    ```
    py fiso.py speech prueba.txt audio.mp3
    ```
    _Puedes usar tu propio archivo de texto solo ponlo en la carpeta del archivo fiso.py_

    
