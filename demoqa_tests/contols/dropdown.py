from selene import have
from selene.support.shared.jquery_style import s


def set_by_click(selector: str, value):
    s(selector).click()
    s(selector).s('[class$=menu]').ss('[class$=option]').element_by(
        have.exact_text(value)
    ).click()
