from pydantic import BaseModel

class EmpTerm(BaseModel):
    EmpSatisfaction: int
    SpecialProjectsCount: int
    Absences: int