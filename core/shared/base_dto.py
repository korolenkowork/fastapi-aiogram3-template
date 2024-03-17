from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        from_attributes = True


class StatusDTO(BaseDTO):
    status: str
