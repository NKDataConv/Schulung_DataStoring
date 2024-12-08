import fastapi
import uvicorn


app = fastapi.FastAPI()

# route ohne parameter
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# route mit einem parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

# route mit einem query parameter
@app.get("/hello")
def say_hello(name: str = fastapi.Query(..., description="The name to say hello to")):
    return {"message": f"Hello {name}"}

# route mit einem path parameter und einem query parameter
@app.get("/hello_with_greeting/{name}")
def say_hello(name: str, greeting: str = fastapi.Query("Welcome", description="The greeting to say hello to")):
    return {"message": f"{greeting} {name}"}

# route mit body parameter
@app.post("/hello_with_body")
def say_hello_with_body(body: dict = fastapi.Body(..., description="The body to say hello to")):
    # insert oder update in die datenbank
    # ...
    return {"message": f"Hello {body['name']}"}

# erstellen der swagger documentation
@app.get("/docs")
def docs():
    return fastapi.docs(app)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
