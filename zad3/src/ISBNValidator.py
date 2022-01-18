class ISBNValidator:
    def validate(self, isbn_number):
        if not isinstance(isbn_number, str):
            return False
        try:
            number = list(map(lambda x: int(x), list(
                isbn_number.replace("-", ""))))
        except ValueError:
            return False
        if len(number) != 13:
            return False

        for i, j in enumerate(number):
            if i % 2 != 0:
                number[i] = j * 3

        return number[12] == (10 - sum(number[:12]) % 10) % 10
