# [![Django](https://skillicons.dev/icons?i=django&perline=3)](https://skillicons.dev) API REST con Django y DRF

> ℹ️ Aplicación basada en el [tutorial](https://www.youtube.com/watch?v=Gr_QsOifaro) impartido por Fazt Code

API REST sencilla con operaciones de registrar, login y obtener profile utilizando Tokens a través del módulo 'authtoken' de la librería Django REST Framework.

Para acceder a la información del profile del usuario se debe pasar primero por un proceso de Registro y Login.

### Estructura del código
> *Dentro del código se puede encontrar comentarios para cada línea o proceso que es importante mencionar su utilidad.*

La API consta de dos aplicaciones, 'func' y 'class', correspondiente a vista de funciones y a vista de clases. Los endpoints de ejemplo son los siguientes para las distintas aplicaciones:

* Aplicación func:
  * Registro de usuarios [POST]: http://127.0.0.1:8000/func/register
  * Login de usuarios [POST]: http://127.0.0.1:8000/func/login
  * Profile de usuarios [GET]: http://127.0.0.1:8000/func/profile

* Aplicación class:
  * Registro de usuarios [POST]: http://127.0.0.1:8000/class/register
  * Login de usuarios [POST]: http://127.0.0.1:8000/class/login
  * Profile de usuarios [GET]: http://127.0.0.1:8000/class/profile

Para los endpoints de Login y Registro se puede acceder sin necesidad de Token. Para la consulta del Profile se debe enviar en los Headers la 'Authorization: Token ...' para poder obtener los datos.

Se ha utilizado un sistema de gestión de bases de datos SQLite.

Los posibles JSON se ubican en el JSON_example.txt