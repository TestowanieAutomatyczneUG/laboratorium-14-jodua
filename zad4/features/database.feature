Feature: Database

    @mock
    Scenario: Get all books
        Given there is an book database
        And api_call method mock, returning {1:{title:"Jądro ciemności",ISBN:"9780312159016",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}}}
        When function get_books is called
        Then we get {1:{title:"Jądro ciemności",ISBN:"9780312159016",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}}} as result

    @mock
    Scenario: Get all books - empty
        Given there is an book database
        And api_call method mock, returning {}
        When function get_books is called
        Then we get {} as result

    @mock
    Scenario: Get book by id
        Given there is an book database
        And api_call method mock, returning {title:"Jądro ciemności",ISBN:"9780312159016",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}}
        When function get_book is called with argument 1
        Then we get {title:"Jądro ciemności",ISBN:"9780312159016",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}} as result

    @mock
    Scenario: Get book by id - empty
        Given there is an book database
        And api_call method mock, returning null
        When function get_book is called with argument 23
        Then we get null as result

    @mock
    Scenario: Add book
        Given there is an book database
        And api_call method mock, returning {title:"Nostromo",ISBN:"9780192801548",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}}
        And there is an writer with first_name Joseph, second_name Conrad, email jc@gmail.com
        And there is a book Nostromo with ISBN 9780192801548
        When we add new book to database
        Then we get {title:"Nostromo",ISBN:"9780192801548",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}} as result

    @mock
    Scenario: Add invalid book
        Given there is an book database
        And api_call method mock, raising database error
        When function add_book is called with argument 23
        Then DatabaseError is raised

    @mock
    Scenario: Delete book
        Given there is an book database
        And api_call method mock, returning DELETED
        When function delete_book is called with argument 1
        Then we get DELETED as result

    @mock
    Scenario: Edit book
        Given there is an book database
        And api_call method mock, returning {title:"Nostromo2",ISBN:"9780192801548",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}}
        And there is an writer with first_name Joseph, second_name Conrad, email jc@gmail.com
        And there is a book Nostromo2 with ISBN 9780192801548
        When we update book in database
        Then we get {title:"Nostromo2",ISBN:"9780192801548",author:{first_name:"Joseph",last_name:"Conrad",email:"jc@gmail.com"}} as result