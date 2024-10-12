from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum as PyEnum

# 답변 유형에 대한 열거형 정의
class AnswerType(PyEnum):
    OBJECTIVE = "OBJECTIVE"  # 객관식
    SUBJECTIVE = "SUBJECTIVE"  # 주관식

class Answer(Base):
    __tablename__ = "tb_answer"

    # 답변 ID
    answer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # 답변 유형 (AnswerType 열거형 사용)
    answer_type = Column(Enum(AnswerType), nullable=False)

    # 답변 작성자 (User와의 관계)
    user_id = Column(Integer, ForeignKey("tb_user.user_id"), nullable=False)
    user = relationship("User", back_populates="answers")

    # 답변이 속한 질문 (Question과의 관계)
    question_id = Column(Integer, ForeignKey("tb_question.question_id"), nullable=False)
    question = relationship("Question", back_populates="answers")

    # 답변이 속한 설문 참여 (Participation과의 관계)
    participation_id = Column(Integer, ForeignKey("participations.participation_id"), nullable=False)
    participation = relationship("Participation", back_populates="answers")

    # 객관식 답변일 경우 선택된 옵션 (QuestionOption과의 관계)
    objective_answer_id = Column(Integer, ForeignKey("tb_question_option.option_id"))
    objective_answer = relationship("QuestionOption")

    # 주관식 답변 내용
    subjective_answer = Column(String, nullable=True)
