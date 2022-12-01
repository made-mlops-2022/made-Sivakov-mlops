from pydantic import BaseModel


class HealthChecker(BaseModel):
    health: str

    class Config:
        orm_mode = True
