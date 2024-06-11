from selene import have
from selene.core.entity import Element


class Dropdown:
    def __init__(self, s: Element):
        self.s = s

    def set_by_click(self, value: str):
        self.s.click()
        self.s.s('[class$=menu]').ss('[class$=option]').element_by(
            have.exact_text(value)
        ).click()
