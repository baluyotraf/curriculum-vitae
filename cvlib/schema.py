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


class Metadata(BaseModel):
    github_repo: Optional[str] = None
    website: Optional[str] = None


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
    result: str = ""


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


class CurriculumVitae(BaseModel):
    metadata: Optional[Metadata] = None
    headline: BasicInfo
    competences: List[Competence]
    experiences: List[ProfessionalExperience]
    projects: List[FreelanceProjects]
    education: List[Education]
