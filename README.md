```
flask는
새로 고침이나 페이지를 열면 success = True가 남아이씀
단순히 렌더링한다고 생각 -> 이전 정보를 그대로 사용
```

# PRG 패턴
```
Post -> Redirect -> Get
Post 요청 처리 후 사용자를 리다이렉트 시켜서 GET 요청으로 바꿔줌
```

### PRG 설명
1. 초기에는 success가 False
    a. get 방식으로 화면을 보여줌
    b. 사용자가 폼을 입력해서 제출
2. POST방식으로 입력 제출
    a. success가 True로 변경
    b. 성공 메시지 출력
    c. get방식으로 화면 보여줌
3. 새로고침시 다시 contact 함수 실행
    a. 존재했던 success 정보를 지움
    b. 1번으로 이동