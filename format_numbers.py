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
        num = self._value
        if num < 1000:
            return f"{num:.2f}"
        elif num < 1000000:
            return f"{num / 1000:.2f}K"
        elif num < 1000000000:
            return f"{num / 1000000:.2f}M"
        elif num < 1000000000000:
            return f"{num / 1000000000:.2f}B"
        elif num < 1000000000000000:
            return f"{num / 1000000000000:.2f}T"
        elif num < 1000000000000000000:
            return f"{num / 1000000000000000:.2f}Qa"
        elif num < 1000000000000000000000:
            return f"{num / 1000000000000000000:.2f}Qi"
        elif num < 1e+21:
            return f"{num / 1e+18:.2f}Sx"  # Sextillions
        elif num < 1e+24:
            return f"{num / 1e+21:.2f}Sp"  # Septillions
        elif num < 1e+27:
            return f"{num / 1e+24:.2f}Oc"  # Octillions
        elif num < 1e+30:
            return f"{num / 1e+27:.2f}No"  # Nonillions
        elif num < 1e+33:
            return f"{num / 1e+30:.2f}Dc"  # Decillions
        elif num < 1e+36:
            return f"{num / 1e+33:.2f}UDc"  # Undecillions
        elif num < 1e+39:
            return f"{num / 1e+36:.2f}DDc"  # Duodecillions
        elif num < 1e+42:
            return f"{num / 1e+39:.2f}TDc"  # Tredecillions
        elif num < 1e+45:
            return f"{num / 1e+42:.2f}QaDc"  # Quattuordecillions
        elif num < 1e+48:
            return f"{num / 1e+45:.2f}QiDc"  # Quindecillions
        elif num < 1e+51:
            return f"{num / 1e+48:.2f}SxDc"  # Sexdecillions
        elif num < 1e+54:
            return f"{num / 1e+51:.2f}SpDc"  # Septendecillions
        elif num < 1e+57:
            return f"{num / 1e+54:.2f}OcDc"  # Octodecillions
        elif num < 1e+60:
            return f"{num / 1e+57:.2f}NoDc"  # Novemdecillions
        elif num < 1e+63:
            return f"{num / 1e+60:.2f}Vg"  # Vigintillions
        elif num < 1e+66:
            return f"{num / 1e+63:.2f}UVg"  # Unvigintillion
        elif num < 1e+69:
            return f"{num / 1e+66:.2f}DVg"  # Duovigintillion
        elif num < 1e+72:
            return f"{num / 1e+69:.2f}TVg"  # Trevigintillion
        elif num < 1e+75:
            return f"{num / 1e+72:.2f}QaVg"  # Quattuorvigintillion
        elif num < 1e+78:
            return f"{num / 1e+75:.2f}QiVg"  # Quinvigintillion
        elif num < 1e+81:
            return f"{num / 1e+78:.2f}SxVg"  # Sexvigintillion
        elif num < 1e+84:
            return f"{num / 1e+81:.2f}SpVg"  # Septenvigintillion
        elif num < 1e+87:
            return f"{num / 1e+84:.2f}OcVg"  # Octovigintillion
        elif num < 1e+90:
            return f"{num / 1e+87:.2f}NoVg"  # Novemvigintillion
        elif num < 1e+93:
            return f"{num / 1e+90:.2f}Tg"  # Trigintillion
        elif num < 1e+96:
            return f"{num / 1e+93:.2f}UTg"  # Untrigintillion
        elif num < 1e+99:
            return f"{num / 1e+96:.2f}DTg"  # Duotrigintillion
        elif num < 1e+102:
            return f"{num / 1e+99:.2f}TTg"  # Tretrigintillion
        elif num < 1e+105:
            return f"{num / 1e+102:.2f}QaTg"  # Quattuortrigintillion
        elif num < 1e+108:
            return f"{num / 1e+105:.2f}QiTg"  # Quintrigintillion
        elif num < 1e+111:
            return f"{num / 1e+108:.2f}SxTg"  # Sextrigintillion
        elif num < 1e+114:
            return f"{num / 1e+111:.2f}SpTg"  # Septentrigintillion
        elif num < 1e+117:
            return f"{num / 1e+114:.2f}OcTg"  # Octotrigintillion
        elif num < 1e+120:
            return f"{num / 1e+117:.2f}NoTg"  # Novemtrigintillion
        elif num < 1e+123:
            return f"{num / 1e+120:.2f}Qd"  # Quadragintillion
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
