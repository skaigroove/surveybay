from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class Survey(Base):
    __tablename__ = "tb_survey"

    # 설문 ID
    survey_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # 설문 작성자 (User와의 관계)
    creator_id = Column(Integer, ForeignKey("tb_user.user_id"), nullable=False)
    creator = relationship("User", back_populates="created_surveys")

    # 설문 제목
    title = Column(String, nullable=False)

    # 설문 설명
    description = Column(String, nullable=True)

    # 설문 시작일
    start_date = Column(Date, nullable=False)

    # 설문 종료일
    end_date = Column(Date, nullable=True)

    # 질문 목록 (Survey와 Question 간의 일대다 관계)
    questions = relationship("Question", back_populates="survey", cascade="all, delete-orphan")

    # 설문 참여 (Participation과의 관계)
    participations = relationship("Participation", back_populates="survey", cascade="all, delete-orphan")