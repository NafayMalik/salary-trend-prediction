from fastapi import FastAPI, Response
import json
from fastapi.staticfiles import StaticFiles
from Prediction_and_Difference_for_Specific_Title import generate_salary_plot

app = FastAPI()

@app.get("/predict_salary_plot/")
def get_salary_plot(job_title: str):
    buffer, printed_output, salary_data = generate_salary_plot(job_title)
    return Response(content=buffer.getvalue(), media_type="image/png", headers={"X-Printed-Output": json.dumps(printed_output), "X-Salary-Data": json.dumps(salary_data)})
