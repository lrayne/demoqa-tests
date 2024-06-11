from selene import have, command
from selene.core.entity import Collection


class Checkbox:
    def __init__(self, ss: Collection):
        self.ss = ss

    def set(self, *values: str):
        for value in values:
            self.ss.element_by(have.exact_text(value)).perform(
                command.js.scroll_into_view
            ).click()
