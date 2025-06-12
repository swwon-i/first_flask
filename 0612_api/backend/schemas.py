# 요청 / 응답 모델 정의
from pydantic import BaseModel

class UserCreate(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    id : int
    username : str

    # ORM 객체를 직렬화 할 수 있도록 --> DB에서 가져온 객체를 API 응답으로 사용하기 위함
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name : str
    price : int

class ProductOut(BaseModel):
    id : int
    name : str
    price : int

    class Config:
        from_attributes = True

class CartItem(BaseModel):
    user_id : int
    product_id : int
    quantity : int

class OrderOut(BaseModel):
    id : int
    user_id : int
    product_id : int 
    quantity : int

    class Config:
        from_attributes = True