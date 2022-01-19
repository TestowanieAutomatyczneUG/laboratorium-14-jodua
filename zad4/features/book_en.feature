Feature: Book

    Scenario Outline: Create book, check data
        Given there is an title <title>
        And there is an author Joseph, Conrad, jc@gmail.com
        And there is an ISBN <isbn>
        When the book is created
        Then book data is equal to <data>

        Examples:
            | title             | isbn          | data                            |
            | Heart of darkness | 9780312159016 | Heart of darkness 9780312159016 |
            | Lord jim          | 9780195813845 | Lord jim 9780195813845          |
            | Nostromo          | 9780192801548 | Nostromo 9780192801548          |
            | The secret agent  | 9780192801692 | The secret agent 9780192801692  |

    Scenario Outline: Create book, error
        Given there is an title <title>
        And there is an author Joseph, Conrad, jc@gmail.com
        And there is an ISBN <isbn>
        When the book is created
        Then TypeError is raised

        Examples:
            | title             | isbn          |
            | Heart of darkness | 123           |
            | Lord jim          | []            |
            | Nostromo          | {}            |
            | Heart of darkness | DDDDDDDDDDDD  |
            | Heart of darkness | 1231231231231 |
            | The secret agent  | testing       |