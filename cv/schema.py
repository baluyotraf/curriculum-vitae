from typing import (
    List,
    Union,
    Literal,
)
from datetime import date

from pydantic import BaseModel as PydanticModel


class BaseModel(PydanticModel):
    pass


class SocialInfo(BaseModel):
    linkedin: str
    github: str
    phone: str
    email: str
    address: str


class BasicInfo(BaseModel):
    name: str
    tagline: str
    social_info: SocialInfo
    summary: str


class Competence(BaseModel):
    area: str
    skills: List[str]


class ProfessionalAchivement(BaseModel):
    task: str
    results: List[str]


class ProfessionalExperience(BaseModel):
    title: str
    company: str
    country: str

    start_date: date
    end_date: Union[date, Literal['present']]

    achievements: List[ProfessionalAchivement]

    skills: List[str]


class FreelanceProjects(BaseModel):
    title: str
    description: str

    start_date: date
    end_date: date

    skills: List[str]


class Education(BaseModel):
    degree: str
    program: str
    institution: str

    start_date: date
    end_date: Union[date, Literal['present']]


class CurriculumVitae(BaseModel):
    headline: BasicInfo
    competences: List[Competence]
    experiences: List[ProfessionalExperience]
    projects: List[FreelanceProjects]
    education: List[Education]
