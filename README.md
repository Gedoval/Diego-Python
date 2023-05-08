# Puto el que lee

## Instalar 

### Anaconda
Anaconda es un creador de entornos virtuales para Python. Un entorno virtual es como una "caja" donde corres Python y sirve para separar (abstraer) distintos proyectos para que
no tengas problemas con dependencias. Por ejemplo, en un entorno podes tener instalado Python 2 y en otro Python 3, y podes correr tus scrips en uno u otro segun quieras.
[Leete la guia y lo instalas](https://docs.anaconda.com/free/anaconda/install/)

Cuando lo instalas tenes que crear el entorno que hice yo para este proyecto. Corres ``conda env create -f environment.yml`` y lo activas con ``conda activate Python-Diego``. En la consola
deberias ver algo asi ``(Python-Diego) gdoval@ARG-60142-N:~$ ``


### Docker
Docker es un contenedor de aplicacions. Parecido a los entornos virtuales pero mucho mas extenso. Aca podes replicar sistemas operativos desde cero sin importar el OS donde corras los containers.
Te arme un docker para MySql asi no tenes que andar creando nada para probar esto. Instalate **Docker** y **Docker Compose**. Si estas en Windows tenes el **Docker Desktop** si te miedo la consola.
Para levantar el contenedor anda a la carpeta **docker** y corres ``docker-compose -f mysql-compose.yml up --force-recreate`` . Esto te crea un contenedor con una base MySql lista para usar, y te carga
unos datos falopa para probar, usando el script **init.sql**. Tambien tiene una UI en **localhost:8080**. El password sacalo del yml del composer. 

### Python
Cuando tengas todo lo de arriba instalado, te abris esto con el PyCharm y en la carpeta de test tenes dos para correr que a mi me funcionaron asi que a vos tambien... o agarrate.
Cuando importes esto en el PyCharm elegile como compilador **Conda** y busca el entorno que creaste.


## Y ahora

Esto lo arme asi rapido para que vayas viendo de a poco un par de conceptos que se usan en Python y en todos lados:
* Programacion orientada a Objetos (Object Oriented Programming)
* Modelado de datos
  * Basicamente cómo representar las tablas en una base de datos en una Clase
* Buenas practicas para codear
  * Patron de diseño Repository
  * Uso de constantes (las variables que estan en MAYUSCULA)
  * No repetir codigo
  * Validaciones con excepciones propias
  * Tests para cada caso posible

Anda viendo de a poco todo eso, y cuando mas o menos lo entiendas completa los archivos que dicen **Factura** para que queden similares a Usuario pero:
* Quiero saber cuántas facturas hizo cada usuario
* Monto total facturado por usuario
* Cargar una factura para un usuario
* Cargar muchas facturas para un usuario
* Cargar muchas facturas para muchos usuarios

Hacelo de a poco, siempre armando uno o mas tests para cada uno de esos puntos. Trata de pensar todos los casos posibles, no solo los casos en los que todo sale bien.
Subi cosas al repo asi lo voy viendo y te digo que onda. Y si no logeas se te descuentan puntos asi que fijate.
