class PlanetAge:
    def calculate(self, seconds, planet):
        self.planets = {
            "Merkury": 0.2408467,
            "Wenus": 0.61519726,
            "Ziemia": 1,
            "Mars": 1.8808158,
            "Jowisz": 11.862615,
            "Saturn": 29.447498,
            "Uran": 84.016846,
            "Neptun": 164.79132
        }

        if type(seconds) == int or type(seconds) == float:
            if type(planet) == str:
                if seconds > 0:
                    if planet in self.planets:
                        result = round(seconds/31557600 /
                                       self.planets[planet], 2)
                        return result
                    else:
                        raise ValueError(
                            f'Planet /"{planet}/" is not a valid planet')
                else:
                    raise ValueError("Number must be positive")
            else:
                raise TypeError("Planet have to be a string")
        else:
            raise TypeError("Seconds parameter must be a integer or float")
