from selene import browser, have, command
from selene.support.shared.jquery_style import s


class HomePage:
    def open(self):
        browser.open('/')
        return self

    def select_forms(self):
        self._select('Forms')
        return self

    def select_elements(self):
        self._select('Elements')
        return self

    def _select(self, card: str):
        s('.category-cards').ss('.card-body').element_by(
            have.exact_text(card)
        ).perform(command.js.scroll_into_view).click()
        return self
