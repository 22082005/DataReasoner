from fastapi import APIRouter, UploadFile, File, Form
import pandas as pd
from io import BytesIO

from scchema_inference.infer_schema import infer_schema
from preprocessing.missing_values  import analyze_missing_values
from preprocessing.duplicates import analyze_duplicates
from statstics.descriptive.summary import descriptive_summary
from statstics.correlation.corr import analyze_correlation
from preprocessing.outliers.outlier import analyze_outliers
from statstics.hypothesis_testing.hypothesis import analyze_hypothesis_testing
from statstics.information_theory.information import analyze_information
from eda.eda import analyze_eda
from visualization.visualize import analyze_visualization

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

    descriptive_results = []

    for column in df.select_dtypes(include="number").columns:

        result = descriptive_summary(df[column])

        result["column_name"] = column

        descriptive_results.append(result)

    correlation = analyze_correlation(df,schema)

    outliers = analyze_outliers(df,schema)
    hypothesis = analyze_hypothesis_testing(
    df,
    schema,
    target
    )
    information = analyze_information(

    df,schema,target)
    eda = analyze_eda(
    df,
    target
   )
    visualization = analyze_visualization(
        df,
        schema
    )
    


    return {
    "rows"  :len(df),
    "columns":len(df.columns),
    "target":target,
    "schema": schema,
    "missing":missing,
    "duplicates":duplicates,
    "descriptive_summary":descriptive_results,
    "correlation":correlation,
    "outliers":outliers,
    "hypothesis_testing":hypothesis,
    "information_theory":information,
    "eda":eda,
    "visualization": visualization
    }

   