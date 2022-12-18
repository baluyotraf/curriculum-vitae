from typing import (
    List,
    Union,
    Literal,
    Optional,
)
from datetime import date

from pydantic import BaseModel as PydanticModel


class BaseModel(PydanticModel):
    pass


class Theme(PydanticModel):
    primary_color: str
    primary_color_dark: str
    primary_color_light: str
    primary_color_text: str
    primary_font: str

    secondary_color: str
    secondary_color_dark: str
    secondary_color_light: str
    secondary_color_text: str
    secondary_font: str


class Metadata(BaseModel):
    github: Optional[str] = None
    website: Optional[str] = None
    printable: Optional[str] = None


class BasicInfo(BaseModel):
    name: str
    tagline: str

    linkedin: str
    github: str
    website: str
    phone: str
    email: str
    address: str

    summary: str


class Competence(BaseModel):
    area: str
    skills: List[str]


class ProfessionalAchievement(BaseModel):
    task: str
    result: str = ''


class ProfessionalExperience(BaseModel):
    title: str
    company: str
    consulting_company: Optional[str] = None
    country: str

    start_date: date
    end_date: Union[date, Literal['present']] = 'present'

    achievements: List[ProfessionalAchievement]

    skills: List[str]


class FreelanceProjects(BaseModel):
    title: str
    description: str

    start_date: date
    end_date: Union[date, Literal['present']] = 'present'

    skills: List[str]


class Education(BaseModel):
    degree: str
    program: str
    institution: str
    details: str

    start_date: date
    end_date: Union[date, Literal['present']] = 'present'


DEFAULT_THEME = Theme(
    primary_color = '#4e342e',
    primary_color_dark = '#260e04',
    primary_color_light = '#7b5e57',
    primary_color_text = '#ffffff',
    primary_font = 'Noto Sans JP',

    secondary_color = '#ffccbc',
    secondary_color_dark = '#e9ccc3',
    secondary_color_light = '#ffffee',
    secondary_color_text = '#000000',
    secondary_font = 'Maven Pro'
)


class CurriculumVitae(BaseModel):
    theme: Theme = DEFAULT_THEME
    metadata: Optional[Metadata] = None
    headline: BasicInfo
    competences: List[Competence]
    experiences: List[ProfessionalExperience]
    projects: List[FreelanceProjects]
    education: List[Education]
