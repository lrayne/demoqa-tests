from selene import have
from selene.core.entity import Element
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys


class DatePicker:
    def __init__(self, s: Element):
        self.s = s

    def set_by_click(
        self,
        day: str = '11',
        month: str = 'October',
        year: str = '1998',
    ):
        self.s.click()

        s('.react-datepicker').s('[class$=year-select]').ss(
            'option'
        ).element_by(have.value(year)).click()

        s('.react-datepicker').s('[class$=month-select]').ss(
            'option'
        ).element_by(have.exact_text(month)).click()

        s('.react-datepicker').s('[class$=month]').ss(
            '[class*=day]'
        ).element_by(have.exact_text(day)).click()

    def set_by_enter(
        self, day: str = '10', month: str = 'Jun', year: str = '1998'
    ):
        self.s.click()
        self.s.type(
            Keys.COMMAND + 'a' + Keys.NULL + f'{day} {month} {year}'
        ).press_enter()
