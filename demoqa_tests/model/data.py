from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


@dataclass
class Gender(Enum):
    male = 'Male'
    female = 'Female'
    others = 'Others'


class Subject(Enum):
    computer_science = 'Computer Science'
    english = 'English'
    chemistry = 'Chemistry'


class Hobby(Enum):
    reading = 'Reading'
    music = 'Music'
    sports = 'Sports'


class State(Enum):
    ncr = 'NCR'
    uttar_pradesh = 'Uttar Pradesh'
    haryana = 'Haryana'
    rajasthan = 'Rajasthan'


class City(Enum):
    delhi = 'Delhi'
    gurgaon = 'Gurgaon'
    noida = 'Noida'

    agra = 'Agra'
    lucknow = 'Lucknow'
    merrut = 'Merrut'

    karnal = 'Karnal'
    panipat = 'Panipat'

    jaipur = 'Jaipur'
    jaiselmer = 'Jaiselmer'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    date_of_birth: date
    subjects: List[Subject]
    hobbies: List[Hobby]
    avatar: str
    address: str
    state: State
    city: City


user = User(
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
