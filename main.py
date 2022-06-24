from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"hello":5}

@app.get("/about")
def about():
    return [{"data":"about page"}]    