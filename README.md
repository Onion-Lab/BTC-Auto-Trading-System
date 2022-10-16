# BTC-Auto-Trading-System

< 개발 환경 >
- Window
- Python 3.8
- Package
  (1) Seleinum
  (2) PyQt
  (3) KakaoTalk chat bot
  (4) Flask

< 동작 시나리오 >
- 카카오톡으로 비트코인 구매 시그널을 받는다
- 구매 시그널을 웹서버(Flask)로 전달한다
- 웹서버는 전달받은 카카오톡 시그널을 기반해 크롬 웹 브라우저를 제어한다.
