
# **Proyecto Django**

Proyecto trimestral para módulo Desarrollo Web en Entorno Servidor (DWES)

***
## **Título**
 Librería musical para que mi padre pueda ir registrando su colección de música.   

 Consta de varias partes: Álbums, Artistas, Canciones y Discográficas.   

 Haciendo click en cada una de las partes, veremos que hay varias opciones:   
 a) Listar: muestra todos los registros sin posibilidad de mayor acción.   
 b) Crear: pide los datos necesarios para incluir un nuevo registro.   
 c) Modificar: permite acceder al registro que queramos y modificar su información.   
 d) Eliminar: elimina el registro.   

 Para poder acceder a todas las opciones, hay que tener permisos. Si no, sólo podrás listar.   

 Para testeo:   
 _user:_ root   
 _password:_ root

***  

## **Instalación**

1) Clona el repositorio o descárgalo directamente:  
   
  ```bash 
  https://github.com/mariaestmag/libreria-musical.git  
  ```

2) Una vez desargado, ábrelo, crea tu propio entorno virtual y actívalo:

```bash 
python3 -m venv venv

source venv/bin/activate
  ```

3) Instala los requisitos:

```bash
pip install -r requirements.txt
```

4) Despliega el servidor:
   
```bash
python3 manage.py runserver
```  


***

### Autores  
* [@mariaestmag](https://www.github.com/mariaestmag) 👋

