from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.router import router as test_router
from routers.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router)


@app.get("/")
@limiter.limit("100/second")
def read_root(request: Request):
    return {"Hello": "World"}


@app.post("/sql/")
@limiter.limit("1/second")
async def sql_response(request: Request):
    return
