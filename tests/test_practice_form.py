from selene import browser, have, command
from selene.support.shared.jquery_style import s, ss


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

    s('#dateOfBirthInput').click()

    s('.react-datepicker').s('[class$=year-select]').ss('option').element_by(
        have.value('1998')
    ).click()

    s('.react-datepicker').s('[class$=month-select]').ss('option').element_by(
        have.exact_text('October')
    ).click()

    s('.react-datepicker').s('[class$=month]').ss('[class*=day]').element_by(
        have.exact_text('31')
    ).click()

    s('#subjectsInput').perform(command.js.scroll_into_view)
    s('#subjectsInput').type('Computer Science')
    s('.subjects-auto-complete__menu-list').ss('[class$=option]').element_by(
        have.exact_text('Computer Science')
    ).click()

    ss('[for^=hobbies-checkbox]').element_by(
        have.exact_text('Reading')
    ).click()

    s('#currentAddress').type('27302 Ardelia Spurs, Kunzetown, GA 83306-2195')

    s('#state').click()
    s('#state').s('[class$=menu]').ss('[class$=option]').element_by(
        have.exact_text('Haryana')
    ).click()

    s('#city').click()
    s('#city').s('[class$=menu]').ss('[class$=option]').element_by(
        have.exact_text('Panipat')
    ).click()

    s('#submit').click()

    # THEN
    s('.modal-content').s('.table').all('td').even.should(
        have.exact_texts(
            'Aleksei Torsukov',
            'torsukov@test.ru',
            'Male',
            '8999123440',
            '31 October,1998',
            'Computer Science',
            'Reading',
            '',
            '27302 Ardelia Spurs, Kunzetown, GA 83306-2195',
            'Haryana Panipat',
        )
    )
