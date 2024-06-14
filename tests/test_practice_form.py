from selene import have
from demoqa_tests.model.pages.home_page import HomePage
from demoqa_tests.model.pages.forms_page import FormsPage
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_register_a_student():

    # GIVEN
    home_page = HomePage()
    forms_page = FormsPage()
    registration_page = RegistrationPage()

    # WHEN
    home_page.open()
    home_page.select_forms()
    forms_page.panel.select_student_registration_form()

    (
        registration_page.form.fill_first_name('Aleksei')
        .fill_last_name('Torsukov')
        .fill_email('torsukov@test.ru')
        .fill_gender('Male')
        .fill_mobile('8999123440')
        .fill_date_of_birth('11 October 1998')
        .fill_subjects(['Computer Science', 'English'])
        .set_hobbies(['Reading', 'Music'])
        .upload_avatar('photo.png')
        .fill_current_address(
            'Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678'
        )
        .fill_state('NCR')
        .fill_city('Delhi')
        .submit()
    )

    # THEN
    registration_page.user_data.should(
        have.exact_texts(
            'Aleksei Torsukov',
            'torsukov@test.ru',
            'Male',
            '8999123440',
            '11 October,1998',
            'Computer Science, English',
            'Reading, Music',
            'photo.png',
            'Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678',
            'NCR Delhi',
        )
    )
