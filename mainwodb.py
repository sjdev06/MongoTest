from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []  # list of lists here each list contains [username, password, email]


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str


@app.post("/login")
def login(request: LoginRequest):
    for user in users:
        if user[0] == request.username and user[1] == request.password:
            return "Login successful"
    return "Login failed"


@app.post("/register")
def register(request: RegisterRequest):
    # username, password, email
    users.append([request.username, request.password, request.email])
    return "User registered successfully at index " + str(len(users) - 1)

@app.get("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    print("running...")
