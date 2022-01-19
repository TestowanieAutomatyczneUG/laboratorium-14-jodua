Feature: ISBNValidator

  Scenario Outline: ISBN Validator
    Given there is an ISBNValidator
    When we pass <string> to validate method
    Then we get <result> as result

    Examples:
      | string                           | result |
      | 978-3-16-148410-0                | true   |
      | 978-83-87347-42-0                | true   |
      | 978-83-87347-42-1                | false  |
      | 978-3-16-148410-2                | false  |
      | 123123123123                     | false  |
      | asdasdasd                        | false  |
      | ******                           | false  |
      | []                               | false  |
      | 12312312312.3123123              | false  |
      | -123123123                       | false  |
      | -123123123.123123123             | false  |
      | {}                               | false  |
      | ""                               | false  |
      | ---------------------------      | false  |
      | 978-3-16-148------410----------0 | true   |
