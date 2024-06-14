from datetime import date

from selene import have, command
from selene.support.shared.jquery_style import s, ss

from demoqa_tests.model.data import Subject, Gender, Hobby, State, City
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

    def fill_gender(self, gender: Gender):
        s('#genterWrapper').all('label[for^=gender-radio]').element_by(
            have.text(gender.value)
        ).click()
        return self

    def fill_mobile(self, value: str):
        s('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, value: date):
        day, month, year = value.strftime('%d %B %Y').split(' ')
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

    def fill_subjects(self, subjects: list[Subject]):
        self.subjects.click()
        for subject in subjects:
            self.subjects.type(subject.value)
            s('[class*=auto-complete__menu]').ss('[id*=option]').element_by(
                have.exact_text(subject.value)
            ).click()
        return self

    def set_hobbies(self, hobbies: list[Hobby]):
        for hobby in hobbies:
            ss('[for^=hobbies-checkbox]').element_by(
                have.exact_text(hobby.value)
            ).perform(command.js.scroll_into_view).click()
        return self

    def upload_avatar(self, file: str):
        s('#uploadPicture').type(resource(file))
        return self

    def fill_current_address(self, value: str):
        s('#currentAddress').type(value)
        return self

    def fill_state(self, state: State):
        self.state.perform(command.js.scroll_into_view).click()
        self.state.all('[id^=react-select-3-option]').element_by(
            have.text(state.value)
        ).click()
        return self

    def fill_city(self, city: City):
        self.city.click()
        self.city.all('[id^=react-select-4-option]').element_by(
            have.text(city.value)
        ).click()
        return self

    def submit(self):
        s('#submit').click()
        return self
