from fastapi import FastAPI, status, Response
from .fib import fibonacci


app = FastAPI()


@app.get("/fib", status_code=status.HTTP_200_OK)
async def read_item(n: int, response: Response):
    try:
        result = {"result": fibonacci(n)}
        response.status_code = status.HTTP_200_OK
        return result
    except ValueError as e:
        result = {"status": 400,
                  "message": "Bad Request",
                  "error": str(e)}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
