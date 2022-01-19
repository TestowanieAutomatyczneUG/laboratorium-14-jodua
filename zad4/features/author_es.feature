            # language: es
            Característica: Autor

            Esquema del escenario: Crear autor, verificar el nombre
            Dado hay un nombre <first_name>
            Y hay un apellido <last_name>
            Y hay un correo jc@gmail.com
            Cuando Se crea el autor
            Entonces el nombre completo del autor es igual a <full_name>

            Ejemplos:
            | first_name | last_name | full_name         |
            | Joseph     | Conrad    | Joseph Conrad     |
            | Joseph2    | Conrad2   | Joseph2 Conrad2   |
            | Adam       | Pilarski  | Adam Pilarski     |
            | Szymon     | Merski    | Szymon Merski     |
            | Sebastian  | Rychert   | Sebastian Rychert |

Escenario: Crear autor, verificar apellido
Dado hay un nombre Joseph
Y hay un apellido Conrad
Y hay un correo jc@gmail.com
Cuando Se crea el autor
Entonces author last_name is equal to Conrad

Escenario: Crear autor, verificar el correo electrónico
Dado hay un nombre Joseph
Y hay un apellido Conrad
Y hay un correo jc@gmail.com
Cuando Se crea el autor
Entonces author email is equal to jc@gmail.com

Escenario: Crear autor, inválido
Dado hay un nombre Joseph
Y hay un apellido Conrad
Y !hay un correo inválido
Cuando Se crea el autor
Entonces Se genera TypeError
