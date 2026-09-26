from fastapi import FastAPI

from domain.entityoptimizer import EntityOptimizer

app = FastAPI(
    title="API Credit Optimizer",
    description="API para la Credit Optimizer",
    version="1.0.0"
)

# Gets

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get(
    "/consultoptimizerall",
    summary="Consult all Credit Optimizer",
    description="Consult all Credit Optimizer",
    tags=["CreditOptimizer"]
)

async def consult_optmizer_all():
    return "OK"


@app.get(
    "/consultoptimizer/{IdOptimizer}",
    summary="Consult by one Credit Optimizer",
    description="Consult Credit Optimizer one",
    tags=["CreditOptimizer"]
)
async def consultar_optimizer_by_one(IdOptimizer: int):
    return IdOptimizer

# entityOptimizer()
# return EntityOptimizer()