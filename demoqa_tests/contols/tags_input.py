from selene import have
from selene.core.entity import Element
from selene.support.shared.jquery_style import s


class TagsInput:
    def __init__(self, s: Element):
        self.s = s

    def set_by_click(self, *values: str):
        for value in values:
            self.s.click().type(value)
            s('[class*=auto-complete__menu]').ss('[id*=option]').element_by(
                have.exact_text(value)
            ).click()
