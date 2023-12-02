from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.member import MemberCreate, ShowMemberDetails
from db.session import get_db
from db.repository.member import create_new_member

router = APIRouter()


@router.post("/", response_model=ShowMemberDetails, status_code=status.HTTP_201_CREATED)
async def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    member = create_new_member(member=member, db=db)
    return member
