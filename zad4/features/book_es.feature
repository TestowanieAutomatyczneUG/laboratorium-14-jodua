            # language: es
            Característica: Libro

            Esquema del escenario: Crear libro, consultar datos
            Dado hay un titulo <title>
            Y Hay un autor Joseph, Conrad, jc@gmail.com
            Y hay un ISBN <isbn>
            Cuando se crea el libro
            Entonces los datos del libro son iguales a <data>

            Ejemplos:
            | title             | isbn          | data                            |
            | Heart of darkness | 9780312159016 | Heart of darkness 9780312159016 |
            | Lord jim          | 9780195813845 | Lord jim 9780195813845          |
            | Nostromo          | 9780192801548 | Nostromo 9780192801548          |
            | The secret agent  | 9780192801692 | The secret agent 9780192801692  |

            Esquema del escenario: Crear libro, error
            Dado hay un titulo <title>
            Y Hay un autor Joseph, Conrad, jc@gmail.com
            Y hay un ISBN <isbn>
            Cuando se crea el libro
            Entonces Se genera TypeError

            Ejemplos:
            | title             | isbn          |
            | Heart of darkness | 123           |
            | Lord jim          | []            |
            | Nostromo          | {}            |
            | Heart of darkness | DDDDDDDDDDDD  |
            | Heart of darkness | 1231231231231 |
            | The secret agent  | testing       |