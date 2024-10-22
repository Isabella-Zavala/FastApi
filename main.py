from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/nombres") 
async def obtener_nombres(): 
  return ["Juan", "María", "Pedro"]
