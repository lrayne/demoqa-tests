from selene.core.entity import Element
from selene.support.shared.jquery_style import ss


class Table:
    def __init__(self, s: Element):
        self.s = s
        self.cells = ss('td')
