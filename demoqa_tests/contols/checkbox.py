from selene import have, command
from selene.support.shared.jquery_style import ss


def set(selector: str, *values: str):
    for value in values:
        ss(selector).element_by(have.exact_text(value)).perform(
            command.js.scroll_into_view
        ).click()
