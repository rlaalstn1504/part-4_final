from fastapi import FastAPI

app = FastAPI()

# 데코레이터: "이 함수는 GET /hello 요청을 처리해"
@app.get("/hello")
def hello():
    return {"message": "안녕하세요"}