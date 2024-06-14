from selene import have
from demoqa_tests.model.pages.home_page import HomePage
from demoqa_tests.model.pages.forms_page import FormsPage
from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.model.data import user


def test_register_a_student():

    # GIVEN
    home_page = HomePage()
    forms_page = FormsPage()
    registration_page = RegistrationPage()
    student = user

    # WHEN
    home_page.open()
    home_page.select_forms()
    forms_page.panel.select_student_registration_form()

    (
        registration_page.form.fill_first_name(student.first_name)
        .fill_last_name(student.last_name)
        .fill_email(student.email)
        .fill_gender(student.gender.male)
        .fill_mobile(student.mobile)
        .fill_date_of_birth(student.date_of_birth)
        .fill_subjects(student.subjects)
        .set_hobbies(student.hobbies)
        .upload_avatar(student.avatar)
        .fill_current_address(student.address)
        .fill_state(student.state)
        .fill_city(student.city)
        .submit()
    )

    # THEN
    registration_page.user_data.should(
        have.exact_texts(
            f'{student.first_name} {student.last_name}',
            student.email,
            student.gender.value,
            student.mobile,
            student.date_of_birth.strftime('%d %B,%Y'),
            ', '.join(subject.value for subject in student.subjects),
            ', '.join(hobby.value for hobby in student.hobbies),
            student.avatar,
            student.address,
            f'{student.state.value} {student.city.value}',
        )
    )
