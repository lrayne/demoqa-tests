from selene.core.entity import Element


class Table:
    def __init__(self, s: Element):
        self._table = s

    @property
    def cells(self):
        return self._table.ss('td')

    @property
    def rows(self):
        return self._table.ss('tr')
