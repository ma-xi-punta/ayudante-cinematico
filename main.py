from fastapi import FastAPI, Form, HTTPException, Depends
from pydantic import BaseModel
import math
import requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse


# Configuración de la aplicación FastAPI
app = FastAPI()

# Agregar middleware para CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir acceso desde cualquier dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Clave API de OpenWeatherMap (reemplázala con tu propia clave)
API_KEY = "e53258ad600a611d999628fec2e3ac90"
ciudad = "Córdoba,AR"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Modelo para datos en JSON
class Viento(BaseModel):
    intensidad: float
    direccion: float

# Función para calcular el viento relativo
def calcular_viento_relativo(viento_verdadero, propulsion_buque):
    try:
        direccion_verdadero_rad = math.radians(viento_verdadero["direccion"])
        direccion_propulsion_rad = math.radians(propulsion_buque["direccion"])

        vx_verdadero = viento_verdadero["intensidad"] * math.cos(direccion_verdadero_rad)
        vy_verdadero = viento_verdadero["intensidad"] * math.sin(direccion_verdadero_rad)
        
        vx_propulsion = propulsion_buque["intensidad"] * math.cos(direccion_propulsion_rad)
        vy_propulsion = propulsion_buque["intensidad"] * math.sin(direccion_propulsion_rad)

        vx_relativo = vx_verdadero - vx_propulsion
        vy_relativo = vy_verdadero - vy_propulsion

        intensidad_relativa = math.sqrt(vx_relativo**2 + vy_relativo**2)
        direccion_relativa_rad = math.atan2(vy_relativo, vx_relativo)
        direccion_relativa = math.degrees(direccion_relativa_rad)

        if direccion_relativa < 0:
            direccion_relativa += 360

        return {"intensidad": round(intensidad_relativa, 2), "direccion": round(direccion_relativa, 2)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error en el cálculo: {str(e)}")

# Endpoint para obtener el clima de una ciudad
@app.get("/clima/{ciudad}")
async def obtener_clima(ciudad: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "No se pudo obtener la información del clima"}

    data = response.json()
    
    if data.get("cod") != 200:
        return {"error": "Ciudad no encontrada"}

    clima = data.get("main", {})
    temperatura = clima.get("temp", "No disponible")
    descripcion = data["weather"][0]["description"] if "weather" in data else "No disponible"

    return {"temperatura": temperatura, "descripcion": descripcion}

# Endpoint para calcular el viento relativo (JSON)
@app.post("/calcular_viento_relativo/")
async def calcular_viento_relativo_endpoint(viento_verdadero: Viento, propulsion_buque: Viento):
    resultado = calcular_viento_relativo(viento_verdadero.dict(), propulsion_buque.dict())
    return {"viento_relativo": resultado}

# Endpoint alternativo para recibir datos desde un formulario
@app.post("/calcular_viento_relativo_form/")
async def calcular_viento_relativo_form(
    viento_verdadero_intensidad: float = Form(...),
    viento_verdadero_direccion: float = Form(...),
    propulsion_buque_intensidad: float = Form(...),
    propulsion_buque_direccion: float = Form(...)
):
    # Convertir datos del formulario en diccionarios similares al modelo Viento
    viento_verdadero = {"intensidad": viento_verdadero_intensidad, "direccion": viento_verdadero_direccion}
    propulsion_buque = {"intensidad": propulsion_buque_intensidad, "direccion": propulsion_buque_direccion}

    resultado = calcular_viento_relativo(viento_verdadero, propulsion_buque)
    
    return {"viento_relativo": resultado}
