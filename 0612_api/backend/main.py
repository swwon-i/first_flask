from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model import Base, User
from database import SessionLocal, engine

# fastapi 생성
app = FastAPI()

# 앱 실행 시 DB에 정의된 모든 테이블 생성
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() 
    try:
        yield db # 종속된 함수에 세션 주입

    finally:
        db.close()

# 회원 가입용 데이타타입 pydantic
class RegisterRequest(BaseModel):
    username : str
    email : str
    password : str

# 라우터 ( 요청에 응답하는 )
@app.post('/api/register')
def register_user(user : RegisterRequest, db : Session=Depends(get_db)):
    # 같은 사용자가 존재하는지 조회
    existing_user = db.query(User).filter(User.username == user.username).first()

    # 같은 사용자가 있으면 400에러
    if existing_user:
        raise HTTPException(status_code=400, detail='이미 존재하는 사용자입니다.')
    
    # 새 유저에 대한 객체(인스턴스) 생성
    new_user = User(
        username = user.username,
        email = user.email,
        password = user.password
    )
    # db commit하는 과정과 동일
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # db에서 자동 생성된 id를 유저에 할당

    return {"success" : True, 'message' : '회원가입 성공!', 'user_id' : new_user.id}

