from selene import have, command
from selene.core.entity import Collection


class Menu:
    def __init__(self, items: Collection):
        self.items = items

    def select(self, item: str):
        self.items.element_by(have.exact_text(item)).perform(
            command.js.scroll_into_view
        ).click()
