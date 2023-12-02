from sqlalchemy.orm import Session
from schemas.member import MemberCreate
from db.models.member import Member
from core.hashing import Hasher


def create_new_member(member: MemberCreate, db: Session):
    member = Member(
        email=member.email,
        password_hash=Hasher.get_password_hash(member.password_hash),
        is_active=True
    )
    db.add(member)
    db.commit()
    db.refresh(member)
    return member
