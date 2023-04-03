from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
from utils import classes 


app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/generate",status_code=200)
def generate_random_name(response=Response,nationality:str="nepal",country:str="nepal",gender:str="male"):
    try:
        random_name_generator =classes.RandomNameGenerator(nationality,country,gender)
        random_name=random_name_generator.make_api_call()
        return {"random_name":random_name}
    except classes.APIException as err:
        response.status_code=err.status_code
        return {"err_message":str(err)}
    



    
