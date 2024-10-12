from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum as PyEnum

# 질문 유형 열거형 정의
class QuestionType(PyEnum):
    SINGLE_CHOICE = "SINGLE_CHOICE"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    TEXT = "TEXT"

class Question(Base):
    __tablename__ = "tb_question"

    # 질문 ID
    question_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # 설문 ID (Survey와의 관계)
    survey_id = Column(Integer, ForeignKey("tb_survey.survey_id"), nullable=False)
    survey = relationship("Survey", back_populates="questions")

    # 질문 내용
    context = Column(String, nullable=False)

    # 질문 유형 (열거형으로 지정)
    question_type = Column(Enum(QuestionType), nullable=False)

    # 답변 (Answer와의 1:N 관계)
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

    # 선택지 (QuestionOption과의 1:N 관계)
    question_options = relationship("QuestionOption", back_populates="question", cascade="all, delete-orphan")
