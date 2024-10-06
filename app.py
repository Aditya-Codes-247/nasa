from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI()

# Mount the static files correctly
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Home route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route for Game Selection page
@app.get("/game-selection", response_class=HTMLResponse)
async def game_selection(request: Request):
    return templates.TemplateResponse("game_selection.html", {"request": request})

# Routes for each game
@app.get("/game1", response_class=HTMLResponse)
async def game1(request: Request):
    return templates.TemplateResponse("game1.html", {"request": request})

@app.get("/game2", response_class=HTMLResponse)
async def game2(request: Request):
    return templates.TemplateResponse("game2.html", {"request": request})

@app.get("/game3", response_class=HTMLResponse)
async def game3(request: Request):
    return templates.TemplateResponse("game3.html", {"request": request})

# Run the app using: uvicorn app:app --reload
