from selene import command
from selene.support.shared.jquery_style import s


def set_by_tab(selector: str, *values: str):
    for value in values:
        s(selector).perform(command.js.scroll_into_view).type(
            value
        ).press_tab()
