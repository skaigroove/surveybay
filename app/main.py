from fastapi import FastAPI
from app.api.routes import router

# FastAPI 인스턴스 생성
app = FastAPI(title="surveybay")

# 라우터를 FastAPI 앱에 등록
app.include_router(router)

# 기본 경로에 대한 엔드포인트 정의
@app.get("/")
def read_root():
    return {"message": "Welcome to surveybay"}
