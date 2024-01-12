class FormattedNumber:
    def __init__(self, value=0):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __format__(self, format_spec):
        return format(self._value, format_spec)

    def formatted(self):
        num = self._value #if isinstance(self._value, (int, float)) else self._value.value
        if num < 1000:
            return f"{num:.2f}"  # Numbers less than 1000 with two decimal places
        elif num < 1000000:
            # print(num)
            return f"{num/1000:.2f}K"  # Thousands with two decimal places
        elif num < 1000000000:
            return f"{num/1000000:.2f}M"  # Millions
        elif num < 1000000000000:
            return f"{num/1000000000:.2f}B"  # Billions
        elif num < 1000000000000000:
            return f"{num/1000000000000:.2f}T"  # Trillions
        elif num < 1000000000000000000:
            return f"{num/1000000000000000:.2f}Qa"  # Quadrillions
        elif num < 1000000000000000000000:
            return f"{num/1000000000000000000:.2f}Qi"  # Quintillions
        else:
            return f"{num:.2f}"

        # Arithmetic operations
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return FormattedNumber(self._value + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, FormattedNumber):
            self._value += other.value
        elif isinstance(other, (int, float)):
            self._value += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other):
        if isinstance(other, FormattedNumber):
            self._value -= other.value
        elif isinstance(other, (int, float)):
            self._value -= other
        else:
            return NotImplemented
        return self


# Comparison methods
    def __lt__(self, other):
        if isinstance(other, FormattedNumber):
            return self._value < other.value
        if isinstance(other, (int, float)):
            return self._value < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, FormattedNumber):
            return self._value <= other.value
        if isinstance(other, (int, float)):
            return self._value <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, FormattedNumber):
            return self._value > other.value
        if isinstance(other, (int, float)):
            return self._value > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, FormattedNumber):
            return self._value >= other.value
        if isinstance(other, (int, float)):
            return self._value >= other
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, FormattedNumber):
            return self._value == other.value
        if isinstance(other, (int, float)):
            return self._value == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, FormattedNumber):
            return self._value != other.value
        if isinstance(other, (int, float)):
            return self._value != other
        return NotImplemented
