from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI()

@app.get("/data")
def read_data():
    # Read processed data
    data_files = [f for f in os.listdir("data/processed_data") if f.endswith('.csv')]
    data_frames = [pd.read_csv(os.path.join("data/processed_data", file)) for file in data_files]
    df = pd.concat(data_frames)
    result = df.to_dict(orient="records")
    return JSONResponse(content=result)
