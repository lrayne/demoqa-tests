import allure
from selene import browser
from demoqa_tests.model.pages.forms_page import FormsPage
from demoqa_tests.model.pages.home_page import HomePage
from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.model.pages.simple_registration_page import (
    SimpleRegistrationPage,
)


class Application:
    home_page = HomePage()
    forms_page = FormsPage()
    registration_page = RegistrationPage()
    simple_registration_page = SimpleRegistrationPage()

    @allure.step('Открыть стартовую страницу сайта')
    def open(self):
        browser.open('/')
        return self


app = Application()
