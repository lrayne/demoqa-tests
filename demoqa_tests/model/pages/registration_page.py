import allure
from selene import browser, have, command
from selene.support.shared.jquery_style import s, ss
from demoqa_tests.model.components.panel import Panel
from demoqa_tests.model.data import User
from demoqa_tests.utils.path import resource


class RegistrationPage:
    def __init__(self):
        self.panel = Panel()
        self.datepicker = s('[class$=datepicker]')
        self.subjects = s('#subjectsInput')
        self.state = s('#state')
        self.city = s('#city')

    @allure.step('Открыть страницу \'Регистрация студента\'')
    def open(self):
        browser.open('/automation-practice-form')
        return self

    @allure.step('Зарегистрировать студента')
    def register(self, user: User):
        s('#firstName').type(user.first_name)
        s('#lastName').type(user.last_name)
        s('#userEmail').type(user.email)

        s('#genterWrapper').all('label[for^=gender-radio]').element_by(
            have.text(user.gender.value)
        ).click()

        s('#userNumber').type(user.mobile)

        day, month, year = user.date_of_birth.strftime('%d %B %Y').split(' ')

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

        self.subjects.click()

        for subject in user.subjects:
            self.subjects.type(subject.value)
            s('[class*=auto-complete__menu]').ss('[id*=option]').element_by(
                have.exact_text(subject.value)
            ).click()

        for hobby in user.hobbies:
            ss('[for^=hobbies-checkbox]').element_by(
                have.exact_text(hobby.value)
            ).perform(command.js.scroll_into_view).click()

        s('#uploadPicture').type(resource(user.avatar))
        s('#currentAddress').type(user.address)

        self.state.perform(command.js.scroll_into_view).click()
        self.state.all('[id^=react-select-3-option]').element_by(
            have.text(user.state.value)
        ).click()

        self.city.click()
        self.city.all('[id^=react-select-4-option]').element_by(
            have.text(user.city.value)
        ).click()

        s('#submit').click()

    @allure.step('Студент должен быть зарегистрирован')
    def should_be_registered(self, user: User):
        s('.modal-content').s('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender.value,
                user.mobile,
                user.date_of_birth.strftime('%d %B,%Y'),
                ', '.join(subject.value for subject in user.subjects),
                ', '.join(hobby.value for hobby in user.hobbies),
                user.avatar,
                user.address,
                f'{user.state.value} {user.city.value}',
            )
        )
