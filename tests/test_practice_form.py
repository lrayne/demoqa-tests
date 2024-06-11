from selene import browser, have, command
from selene.support.shared.jquery_style import s, ss
from demoqa_tests.utils.path import resource
from demoqa_tests.contols import (
    datepicker,
    dropdown,
    checkbox,
    tags_input,
)


def test_register_a_student():
    # GIVEN
    browser.open('https://demoqa.com')

    s('.category-cards').ss('.card-body').element_by(
        have.exact_text('Forms')
    ).perform(command.js.scroll_into_view).click()

    s('.left-pannel').ss('.menu-list').element_by(
        have.exact_text('Practice Form')
    ).click()

    # WHEN
    s('#firstName').type('Aleksei')
    s('#lastName').type('Torsukov')
    s('#userEmail').type('torsukov@test.ru')
    ss('[for^=gender-radio]').element_by(have.exact_text('Male')).click()
    s('#userNumber').type('89991234407')
    datepicker.set_by_click('#dateOfBirthInput', '11', 'October', '1998')
    tags_input.set_by_click(
        '#subjectsInput', 'Computer Science', 'Maths', 'Commerce'
    )
    checkbox.set('[for^=hobbies-checkbox]', 'Reading', 'Music')
    s('#uploadPicture').type(resource('avatar.png'))
    s('#currentAddress').type('27302 Ardelia Spurs, Kunzetown, GA 83306-2195')
    dropdown.set_by_click('#state', 'Haryana')
    dropdown.set_by_click('#city', 'Panipat')
    s('#submit').click()

    # THEN
    s('.modal-content').s('.table').all('td').even.should(
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
