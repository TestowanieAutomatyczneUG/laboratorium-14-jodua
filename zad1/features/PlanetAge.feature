Feature: PlanetAge

  Scenario Outline: Planet age calculator, different planets
    Given there is an PlanetAge
    When we pass number <number> and planet <planet> to calculate method
    Then we get <result> as result

    Examples:
      | number     | planet  | result |
      | 1123123123 | Merkury | 147.77 |
      | 9999999999 | Wenus   | 515.09 |
      | 1123123123 | Ziemia  | 35.59  |
      | 111111111  | Mars    | 1.87   |
      | 99887766   | Jowisz  | 0.27   |


  Scenario Outline: Planet age calculator, exceptions
    Given there is an PlanetAge
    When we pass <what>
    Then <error> is raised

    Examples:
      | what                                   | error      |
      | not a number as first argument         | TypeError  |
      | invalid planet type as second argument | TypeError  |
      | negative number to calculate method    | ValueError |
      | invalid planet to calculate method     | ValueError |
