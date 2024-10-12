# app/models/user.py
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class GenderType(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class UserType(enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "tb_user"
    
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login_id = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    name = Column(String(10), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender_type = Column(Enum(GenderType), nullable=True)
    phone_number = Column(String(11), nullable=False)
    user_type = Column(Enum(UserType), nullable=True)
    
    # Relationships with other tables
    user_inquiries = relationship("Inquiry", back_populates="user", cascade="all, delete-orphan")
    
    # 사용자가 작성한 설문 목록
    created_surveys = relationship("Survey", back_populates="creator")

    # 사용자가 참여한 설문 목록 (Participation 모델과의 관계)
    participations = relationship("Participation", back_populates="user")
