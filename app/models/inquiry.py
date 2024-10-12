from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
from enum import Enum as PyEnum

# 문의 상태에 대한 열거형 정의
class InquiryState(PyEnum):
    UNCOMPLETE = "UNCOMPLETE"
    COMPLETE = "COMPLETE"

class Inquiry(Base):
    __tablename__ = "tb_inquiry"

    # 문의 글 번호
    inquiry_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # 문의 글 작성자 (User와의 관계)
    user_id = Column(Integer, ForeignKey("tb_user.user_id"), nullable=False)
    user = relationship("User", back_populates="inquiry")

    # 문의 게시 글 제목
    title = Column(String, nullable=False)

    # 문의 작성 일자 (기본값으로 현재 시간)
    write_date = Column(DateTime, nullable=False, default=datetime.now)

    # 문의 내용
    content = Column(String, nullable=False)

    # 답변 작성 일자
    answer_date = Column(DateTime, nullable=True)

    # 답변 내용
    reply = Column(String, nullable=True)

    # 문의 상태 (InquiryState 열거형 사용)
    status = Column(Enum(InquiryState), nullable=False, default=InquiryState.UNCOMPLETE)

    # 답변 완료 여부 확인
    @property
    def is_complete(self):
        return self.status == InquiryState.COMPLETE

    # 답변 완료 처리 메서드
    def complete_inquiry(self):
        self.status = InquiryState.COMPLETE
