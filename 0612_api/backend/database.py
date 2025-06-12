from sqlalchemy import create_engine # DB 연결 엔진
from sqlalchemy.orm import sessionmaker, declarative_base # 세션 / 모델 베이스 생성

DATABASE_URL = 'sqlite:///./database.db'

# 현재 경로에 database.db 파일 생성, 쓰레드 제한을 우회
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread' : False})

# 세션을 생성하는 함수,, 요청할 때마다 세션을 만들어서 사용
SessionLocal = sessionmaker(bind=engine)

# 클래스를 정의할 때마다 사용하는 베이스 클래스
Base = declarative_base()

