from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/model:predict")
async def get_model_predict(data: ModelInput):
    try:

        prediction = train_light_gbm_model.predict(
            model=model, data=data.dict())
    except Exception as e:
        logging.error("Error in makeing prediction: {}".format(e))
        prediction = 0.5

    return {"prediction": prediction}
