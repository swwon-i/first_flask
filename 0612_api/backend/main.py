from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model import *
from database import SessionLocal, engine
from schemas import *
from typing import List
from fastapi import Query

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
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='이미 존재하는 사용자입니다.')
    
    new_user = User(
        username = user.username,
        email = user.email,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"success" : True, 'message' : '회원가입 성공!', 'user_id' : new_user.id}

# 로그인
@app.post('/api/login')
def login(user:UserCreate, db:Session=Depends(get_db)):
    found = db.query(User).filter(User.username == user.username, User.password == user.password).first()
    if not found:
        raise HTTPException(status_code=400, detail='로그인 실패.')
    
    return {"success" : True, 'message' : '로그인 성공!'}

# 사용자 조회
@app.get('/api/users/{user_id}', response_model=UserResponse)
def get_user(user_id:int, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='사용자를 조회할 수 없습니다.')
    
    return user

# 전체 상품 조회
@app.get('/api/products', response_model=List[ProductOut])
def get_product(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

# 전체 상품 등록
@app.post('/api/products')
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product = Product(name=product.name, price=product.price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"success" : True, 'message' : '상품 등록 성공!', 'product_id' : product.id}

# 장바구니 담기
@app.post('/api/cart')
def add_to_cart(item: CartItem, db: Session = Depends(get_db)):
    cart = Cart(user_id=item.user_id, product_id=item.product_id, quantity=item.quantity)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return {"success" : True, 'message' : '장바구니!', 'cart_id' : cart.id}

# 장바구니 조회
@app.get('/api/cart?user_id={user_id}')
def show_cart(db: Session=Depends(get_db), user_id: int = Query(...)):
    cart = db.query(Cart).filter(Cart.user_id == user_id).all()

    if not cart:
        raise HTTPException(status_code=404, detail='사용자를 조회할 수 없습니다.')
    
    return [
        {
            'product_id' : item.product_id, 'quantity' : item.quantity
        } for item in cart
    ]

# 주문 요청( 장바구니 상품 주문 )
## 장바구니에서 빼서 주문테이블에 삽입
### 트랜잭션으로 구현해야 하긴 함
@app.post('/api/order')
def order_item(order: OrderRequest, db:Session=Depends(get_db)):
    cart_items = db.query(Cart).filter(Cart.user_id == order.user_id).all()
    
    if not cart_items:
        raise HTTPException(status_code=404, detail='사용자를 조회할 수 없습니다.')
    
    for item in cart_items:
        new_order = Order(
            user_id = item.user_id,
            product_id = item.product_id,
            quantity = item.quantity
        )
        db.add(new_order) # 주문 테이블
        db.delete(item) # 카트 테이블
        db.refresh(new_order) # db에서 생성된 primary key값을 new_order에 갱신

    db.commit()
    return {"success" : True, 'message' : '주문 완!'}

# 주문 목록 조회
@app.get('/api/order', response_model=List[OrderOut])
def get_orders(user_id: int = Query(...), db:Session=Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    
    return orders