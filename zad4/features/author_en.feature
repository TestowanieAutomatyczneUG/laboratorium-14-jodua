Feature: Author

    Scenario Outline: Create author, check full_name
        Given there is an first_name <first_name>
        And there is an last_name <last_name>
        And there is an email jc@gmail.com
        When the author is created
        Then author full name is equal to <full_name>

        Examples:
            | first_name | last_name | full_name         |
            | Joseph     | Conrad    | Joseph Conrad     |
            | Joseph2    | Conrad2   | Joseph2 Conrad2   |
            | Adam       | Pilarski  | Adam Pilarski     |
            | Szymon     | Merski    | Szymon Merski     |
            | Sebastian  | Rychert   | Sebastian Rychert |

    Scenario: Create author, check last_name
        Given there is an first_name Joseph
        And there is an last_name Conrad
        And there is an email jc@gmail.com
        When the author is created
        Then author last_name is equal to Conrad

    Scenario: Create author, check email
        Given there is an first_name Joseph
        And there is an last_name Conrad
        And there is an email jc@gmail.com
        When the author is created
        Then author email is equal to jc@gmail.com

    Scenario: Create author, invalid
        Given there is an first_name Joseph
        And there is an last_name Conrad
        And there is an invalid email
        When the author is created
        Then TypeError is raised