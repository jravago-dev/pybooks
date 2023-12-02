from pydantic import BaseModel, EmailStr, Field


class MemberCreate(BaseModel):
    email: EmailStr
    password_hash: str = Field(..., min_length=4)

class ShowMemberDetails(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
