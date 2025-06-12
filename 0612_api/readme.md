## API 엔드포인트 목록

| 기능           | 메서드 | 엔드포인트                   | 설명                          |
|----------------|--------|------------------------------|-------------------------------|
| 회원가입 폼    | GET    | /api/products                | 회원가입 폼 요청 (예시 목적) |
| 회원가입       | POST   | /api/registert               | 사용자 정보 DB 저장           |
| 로그인         | POST   | /api/login                   | 사용자 인증 및 세션 관리      |
| 상품 목록 조회 | GET    | /api/products                | 전체 상품 조회                |
| 상품 등록      | POST   | /api/products                | 관리자용 상품 등록            |
| 장바구니 담기  | POST   | /api/cart                    | 사용자별 장바구니 추가        |
| 장바구니 조회  | GET    | /api/cart?user_id=           | 특정 사용자의 장바구니 조회   |
| 주문 요청      | POST   | /api/order                   | 장바구니 상품 주문 처리       |
| 주문 목록 조회 | GET    | /api/order?user_id=          | 사용자 주문 내역 조회         |


## FAST API 설치
```
pip install fastapi uvicorn sqlalchemy
```

## 통신 규칙
```
통신    json 포맷
인증    쿠키, 세션 대신 단순 로그인 응답으로 user_id 유지 ( js 변수에 저장 )
응답    {success : True, data : ,,} 형식
에러    {success : False, error : ',,'} 형식

```