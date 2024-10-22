from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
async def obtener_nombres(): 
  return ["Juan", "María", "Pedro"]
