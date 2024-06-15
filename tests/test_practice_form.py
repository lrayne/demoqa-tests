from demoqa_tests.app import app
from demoqa_tests.model.data import student


def test_register_a_student():

    app.open()

    app.home_page.select_forms()
    app.forms_page.panel.select_student_registration_form()
    app.registration_page.register(student)

    app.registration_page.should_be_registered(student)


def test_register_a_student_using_simplified_form():

    app.open()

    app.home_page.select_elements()
    app.forms_page.panel.select_simple_registration_form()
    app.simple_registration_page.register(student)

    app.simple_registration_page.should_be_registered(student)
