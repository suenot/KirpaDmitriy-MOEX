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


@app.get("/get_algo_params")
async def get_algo_params(algo: str):
    return algos.get_algo_params(algo)


@app.get("/execute_algo")
async def execute_algo(algo: str, **kwargs):
    kwargs = {k: v for k, v in kwargs.items() if k in algos.get_algo_params(algo)}
    return await algos.execute_algo(algo, **kwargs)