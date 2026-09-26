from fastapi import FastAPI

# from

app = FastAPI(
    title="API Credit Optimizer",
    description="API para la Credit Optimizer",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

app.api.get()

# entityOptimizer()
# return EntityOptimizer()