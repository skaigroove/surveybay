from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 URL 설정
# PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://skaigroove:skaigroovedb@localhost/surveybay"
# SQLALCHEMY_DATABASE_URL = "postgresql://skaigroove:skaigroovedb@221.164.153.134/surveybay"

# 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 설정
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 베이스 클래스 정의
Base = declarative_base()

# 데이터베이스 세션을 가져오는 종속성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# 연결 테스트를 위한 함수
def test_connection():
    try:
        # 엔진을 사용해 데이터베이스와 연결
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()
            print(f"Connected to: {version[0]}")
    except Exception as e:
        print(f"Error occurred: {e}")
        
# 메인 함수 호출
if __name__ == "__main__": 
    # 연결 테스트 실행
    test_connection()
