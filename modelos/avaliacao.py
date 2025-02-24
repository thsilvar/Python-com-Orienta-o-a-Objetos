class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    def validar_nota(self):
        if self._nota < 0 or self._nota > 5:
            return False
        return True