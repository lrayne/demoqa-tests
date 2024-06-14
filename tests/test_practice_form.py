from datetime import date
from selene import have
from demoqa_tests.model.pages.home_page import HomePage
from demoqa_tests.model.pages.forms_page import FormsPage
from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.model.data import User, State, City, Hobby, Subject, Gender


def test_register_a_student():

    # GIVEN
    home_page = HomePage()
    forms_page = FormsPage()
    registration_page = RegistrationPage()
    student = User(
        first_name='Aleksei',
        last_name='Torsukov',
        email='torsukov@test.ru',
        gender=Gender.male,
        mobile='8999123440',
        date_of_birth=date(1998, 10, 11),
        subjects=[Subject.english, Subject.computer_science],
        hobbies=[Hobby.sports, Hobby.reading],
        avatar='photo.png',
        address='Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678',
        state=State.ncr,
        city=City.gurgaon,
    )

    # WHEN
    home_page.open()
    home_page.select_forms()
    forms_page.panel.select_student_registration_form()

    (
        registration_page.form
        .fill_first_name(student.first_name)
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
