class Error(Exception):
    """Klasa bazowa dla wyjątków w tym module"""
    pass

class zły_wymiar(Error):
    def __init__(self):
        pass

class zla_liczba_min(Error):
    def __init__(self):
        pass