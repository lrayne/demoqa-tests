from selene import have
from selene.support.shared.jquery_style import s


def set_by_click(selector: str, *values: str):
    for value in values:
        s(selector).click().type(value)
        s('[class*=auto-complete__menu]').ss('[id*=option]').element_by(
            have.exact_text(value)
        ).click()
