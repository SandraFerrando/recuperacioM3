from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.characters import HPCharacterService
from app.services.spells import HPSpellService

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def inici(request: Request):
    servei = HPCharacterService()
    personatges = servei.get_characters()
    return templates.TemplateResponse("personatges.html", {
        "request": request,
        "personatges": personatges
    })

@router.get("/encanteris", response_class=HTMLResponse)
async def mostrar_encanteris(request: Request):
    servei = HPSpellService()
    encanteris = servei.get_spells()
    return templates.TemplateResponse("encanteris.html", {
        "request": request,
        "encanteris": encanteris
    })

@router.get("/personatge/{nom}", response_class=HTMLResponse)
async def mostrar_personatge(request: Request, nom: str):
    servei = HPCharacterService()
    personatges = servei.get_characters(limit=1000)
    personatge = next((p for p in personatges if p["name"] == nom), None)

    if personatge:
        return templates.TemplateResponse("personatge.html", {
            "request": request,
            "personatge": personatge
        })
    else:
        return HTMLResponse(content=f"<h1>No s'ha trobat cap personatge amb el nom: {nom}</h1>", status_code=404)
