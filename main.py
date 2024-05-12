from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app = FastAPI()

template = Jinja2Templates(directory="./")

@app.get("/home")
def home(request: Request):
  return template.TemplateResponse("index.html",context={"request":"request"})

