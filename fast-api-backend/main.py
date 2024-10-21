from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from utils import classes  # Asegúrate de que esta importación sea correcta

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate", status_code=200)
def generate_random_name(response: Response, nationality: str = "nepal", country: str = "nepal", gender: str = "male", count: int = 5):
    try:
        random_name_generator = classes.RandomNameGenerator(nationality, country, gender)
        
        # Generar múltiples nombres
        random_names = random_name_generator.make_api_call(count)  # Ajustar según tu método
        return {"random_names": random_names}  # Cambia aquí para devolver múltiples nombres
    except classes.APIException as err:
        response.status_code = err.status_code
        return {"err_message": str(err)}
