from selene import browser, have
from selene.support.shared.jquery_style import s, ss
from demoqa_tests.utils.path import resource
from demoqa_tests.contols import (
    TagsInput,
    Dropdown,
    DatePicker,
    Checkbox,
    Menu,
    Table,
)


def test_register_a_student():
    # GIVEN
    browser.open('https://demoqa.com')

    cards = Menu(s('.category-cards').ss('.card-body'))
    cards.select('Forms')

    panel = Menu(s('.left-pannel').ss('.menu-list'))
    panel.select('Practice Form')

    # WHEN
    s('#firstName').type('Aleksei')
    s('#lastName').type('Torsukov')
    s('#userEmail').type('torsukov@test.ru')
    ss('[for^=gender-radio]').element_by(have.exact_text('Male')).click()
    s('#userNumber').type('89991234407')

    date_of_birth = DatePicker(s('#dateOfBirthInput'))
    date_of_birth.set_by_click('11', 'October', '1998')

    subjects = TagsInput(s('#subjectsInput'))
    subjects.set_by_click('Computer Science', 'Maths', 'Commerce')

    hobbies = Checkbox(ss('[for^=hobbies-checkbox]'))
    hobbies.set('Reading', 'Music')

    s('#uploadPicture').type(resource('avatar.png'))
    s('#currentAddress').type('27302 Ardelia Spurs, Kunzetown, GA 83306-2195')

    state = Dropdown(s('#state'))
    state.set_by_click('Haryana')

    city = Dropdown(s('#city'))
    city.set_by_click('Panipat')

    s('#submit').click()

    # THEN
    modal = Table(s('.modal-content').s('.table'))
    modal.cells.even.should(
        have.exact_texts(
            'Aleksei Torsukov',
            'torsukov@test.ru',
            'Male',
            '8999123440',
            '11 October,1998',
            'Computer Science, Maths, Commerce',
            'Reading, Music',
            'avatar.png',
            '27302 Ardelia Spurs, Kunzetown, GA 83306-2195',
            'Haryana Panipat',
        )
    )
