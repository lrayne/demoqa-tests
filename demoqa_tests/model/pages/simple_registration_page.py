import allure
from selene import browser, have, command
from selene.support.shared.jquery_style import s
from demoqa_tests.model.components.panel import Panel
from demoqa_tests.model.data import User


class SimpleRegistrationPage:
    def __init__(self):
        self.panel = Panel()

    @allure.step('Открыть страницу \'Упрощенная регистрация студента\'')
    def open(self):
        browser.open('/text-box')
        return self

    @allure.step('Зарегистрировать студента')
    def register(self, user: User):
        s('#userName').type(f'{user.first_name} {user.last_name}')
        s('#userEmail').type(user.email)
        s('#currentAddress').type(user.address)
        s('#permanentAddress').type(user.permanent_address)

        s('#submit').perform(command.js.scroll_into_view).click()

    @allure.step('Студент должен быть зарегистрирован')
    def should_be_registered(self, user: User):
        s('#output').s('#name').should(
            have.exact_text(f'Name:{user.first_name} {user.last_name}')
        )
        s('#output').s('#email').should(have.exact_text(f'Email:{user.email}'))

        s('#output').s('#currentAddress').should(
            have.exact_text(f'Current Address :{user.address}')
        )

        s('#output').s('#permanentAddress').should(
            have.exact_text(f'Permananet Address :{user.permanent_address}')
        )
