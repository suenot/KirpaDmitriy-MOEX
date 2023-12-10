from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from ml import algos

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/all_algos")
async def algos_list():
    return algos.get_all_algos_names()