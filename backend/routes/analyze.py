from fastapi import APIRouter, UploadFile, File, Form
import pandas as pd
from io import BytesIO

from scchema_inference.infer_schema import infer_schema
from preprocessing.missing_values  import analyze_missing_values
from preprocessing.duplicates import analyze_duplicates
router =APIRouter()

@router.post("/analyze")

async def analyze_file(file:UploadFile=File(...),target:str=Form()):
    contents=await file.read()
    df=pd.read_csv(BytesIO(contents))
  
    schema = infer_schema(
    df
         )
    missing = analyze_missing_values(
    df
   
    )
    duplicates = analyze_duplicates(df)


    return {
    "rows"  :len(df),
    "columns":len(df.columns),
    "target":target,
    "schema": schema,
    "missing":missing,
    "duplicates":duplicates

   }