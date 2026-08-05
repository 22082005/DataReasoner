from fastapi import APIRouter, UploadFile, File
import pandas as pd
from io import BytesIO

router =APIRouter()
@router.post("/columns")

async def extract_coulmns(file:UploadFile=File(...)):
    contents=await file.read()
    df=pd.read_csv(BytesIO(contents))
    return ({"columns":df.columns.tolist()})


