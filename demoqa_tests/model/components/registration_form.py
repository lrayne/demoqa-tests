from selene import have, command
from selene.support.shared.jquery_style import s, ss
from demoqa_tests.utils.path import resource


class RegistrationForm:
    def __init__(self):
        self.datepicker = s('[class$=datepicker]')
        self.subjects = s('#subjectsInput')
        self.state = s('#state')
        self.city = s('#city')

    def fill_first_name(self, value: str):
        s('#firstName').type(value)
        return self

    def fill_last_name(self, value: str):
        s('#lastName').type(value)
        return self

    def fill_email(self, value: str):
        s('#userEmail').type(value)
        return self

    def fill_gender(self, value: str):
        s('#genterWrapper').all('label[for^=gender-radio]').element_by(
            have.text(value)
        ).click()
        return self

    def fill_mobile(self, value: str):
        s('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, value: str):
        day, month, year = value.split(' ')
        s('#dateOfBirthInput').click()
        self.datepicker.element('[class$=year-select]').all(
            'option'
        ).element_by(have.text(f'{year}')).click()
        self.datepicker.element('[class$=month-select]').all(
            'option'
        ).element_by(have.text(f'{month}')).click()
        self.datepicker.element('[class$=_month]').all(
            '[role=option][class*=day]'
        ).element_by(have.text(f'{day}')).click()
        return self

    def fill_subjects(self, values: list[str]):
        self.subjects.click()
        for value in values:
            self.subjects.type(value)
            s('[class*=auto-complete__menu]').ss('[id*=option]').element_by(
                have.exact_text(value)
            ).click()
        return self

    def set_hobbies(self, values: list[str]):
        for value in values:
            ss('[for^=hobbies-checkbox]').element_by(
                have.exact_text(value)
            ).perform(command.js.scroll_into_view).click()
        return self

    def upload_avatar(self, file: str):
        s('#uploadPicture').type(resource(file))
        return self

    def fill_current_address(self, value: str):
        s('#currentAddress').type(value)
        return self

    def fill_state(self, value: str):
        self.state.perform(command.js.scroll_into_view).click()
        self.state.all('[id^=react-select-3-option]').element_by(
            have.text(value)
        ).click()
        return self

    def fill_city(self, value: str):
        self.city.click()
        self.city.all('[id^=react-select-4-option]').element_by(
            have.text(value)
        ).click()
        return self

    def submit(self):
        s('#submit').click()
        return self
