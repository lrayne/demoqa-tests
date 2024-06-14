from selene import browser
from selene.support.shared.jquery_style import s
from demoqa_tests.model.components.panel import Panel
from demoqa_tests.model.components.registration_form import RegistrationForm
from demoqa_tests.model.components.modal_content import Table


class RegistrationPage:
    def __init__(self):
        self.form = RegistrationForm()
        self.panel = Panel()
        self._user_data = Table(s('.modal-content').s('.table'))

    def open(self):
        browser.open('/automation-practice-form')
        return self

    @property
    def user_data(self):
        return self._user_data.cells.even
