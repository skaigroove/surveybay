from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class Participation(Base):
    __tablename__ = "tb_participation"

    # 참여 ID
    participation_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # 설문 참여자 (User와의 관계)
    user_id = Column(Integer, ForeignKey("tb_user.user_id"), nullable=False)
    user = relationship("User", back_populates="participations")

    # 설문 ID (Survey와의 관계)
    survey_id = Column(Integer, ForeignKey("tb_survey.survey_id"), nullable=False)
    survey = relationship("Survey", back_populates="participations")

    # 참여 일자 (기본값: 참여 일시를 저장)
    participation_date = Column(Date, nullable=False, default=date.today)

    # 참여자가 남긴 답변 목록
    answers = relationship("Answer", back_populates="participation", cascade="all, delete-orphan")
