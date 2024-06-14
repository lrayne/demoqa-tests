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
