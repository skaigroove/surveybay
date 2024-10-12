from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class QuestionOption(Base):
    __tablename__ = 'tb_question_option'

    # 선지 Id
    question_option_id = Column(Integer, primary_key=True, autoincrement=True)

    # 선택지 순서
    option_index = Column(Integer, nullable=False)

    # 선지 내용
    question_option_text = Column(String, nullable=False)

    # 질문과의 관계 (ManyToOne)
    question_id = Column(Integer, ForeignKey('tb_question.question_id'), nullable=False)
    question = relationship("Question", back_populates="question_options")

    # 객관식 답변들과의 관계 (OneToMany)
    objective_answers = relationship("Answer", back_populates="objective_answer")
