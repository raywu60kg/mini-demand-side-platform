from typing import Optional
from fastapi import FastAPI
from datetime import datetime
app = FastAPI()

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	


@app.get("/train/")
def train_model():
    return {"Hello": "World"}


@app.get("/model_list/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
