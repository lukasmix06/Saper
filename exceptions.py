class Error(Exception):
    """Klasa bazowa dla wyjątków w tym module"""

class ZłyWymiar(Error):
    def __init__(self):
        pass

class ZłaLiczbaMin(Error):
    def __init__(self):
        pass
