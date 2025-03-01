from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
from PIL import Image

from utils import get_image_embedding

# HTML
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#CSS
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# mount css to api
app.mount("/static", StaticFiles(directory="static"), name="static")

# on load
@app.get('/')
async def ok():
    return {'status code':'200'}


@app.get("/lookalike")
async def lookalike(request: Request):
    return templates.TemplateResponse("index.html", {'request':request})

@app.post("/lookalike")
async def lookalike(request: Request, file: UploadFile = File(...)):
    # Read
    embedding = get_image_embedding(file.file)

    return templates.TemplateResponse("index.html", {'request':request, 'embedding':embedding})



# run app
if __name__ == "__main__":
    uvicorn.run(app)

# http://127.0.0.1:8000
