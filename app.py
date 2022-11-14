import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/healthz")
def get_status():
    return Response(status_code=200)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=True)