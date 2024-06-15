import allure
from selene.support.shared.jquery_style import s
from selene import have, command


class Panel:

    @allure.step('В панели выбрать регистрацию студента')
    def select_student_registration_form(self):
        self._select('Forms', 'Practice Form')

    @allure.step('В панели выбрать упрощенную регистрацию студента')
    def select_simple_registration_form(self):
        self._select('Elements', 'Text Box')

    def select_buttons_form(self):
        self._select('Elements', 'Buttons')

    def _select(self, item: str, subitem: str):
        if (
            s('.left-pannel')
            .ss('.element-group')
            .element_by_its('.element-list', have.css_class('show'))
            .s('.header-text')
            .matching(have.exact_text(item))
        ):
            s('.element-list.show').ss('.text').element_by(
                have.exact_text(subitem)
            ).perform(command.js.click)
        else:
            s('.left-pannel').ss('.header-text').element_by(
                have.exact_text(item)
            ).click()
            s('.element-list.show').ss('.text').element_by(
                have.exact_text(subitem)
            ).perform(command.js.click)
