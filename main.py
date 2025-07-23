from fastapi import FastAPI,HTTPException,File,UploadFile
from pydantic import BaseModel,Field
import json
from typing import List,Optional,Literal
import shutil
import os
import uvicorn

app=FastAPI()

class verify_patient(BaseModel):
    id: int = Field(..., ge=0, description="Unique patient ID, must be non-negative")
    name: str = Field(..., description="Full name of the patient")
    age: int = Field(..., ge=0, le=120, description="Age must be between 0 and 120")
    gender: Literal['male','female']
    diagnosis: Optional[str] = Field(None, description="Diagnosis or medical condition")

@app.get('/patients/{patient_id}')
def item_by_path(patient_id:int):
    if patient_id>=0 and patient_id<=10:
        try:
            with open('patients.json','r') as f:
                file=json.load(f)
                print(file[patient_id])
                return {'status':'success','patient':file[patient_id]}
        except :
            raise HTTPException(status_code=503,detail='Unable to open file from DB')
    else:
        raise HTTPException(status_code=404,detail="Patient Not found")
@app.get('/patient_detail')
def pateint_info_by_query(patient_id:int,detail:List[str]):
    if patient_id>=0 and patient_id<=10:
        try:
            with open('patients.json','r') as f:
                file=json.load(f)
                patient=file[patient_id]
                #print(file[patient_id].get(detail))
                data={}
                for details in detail:
                    data[details]=patient.get(details,'Not available')
                return {'status':'success','data':data}
        except :
            raise HTTPException(status_code=503,detail='Unable to open file from DB')
    else:
        raise HTTPException(status_code=404,detail="Patient Not found")
    
@app.post("/new_patient")
def add_patient(addpatient:verify_patient):
    try:
        with open('patients.json', 'r') as f:
                patients = json.load(f)

        patients.append(addpatient.model_dump())
        with open('patients.json', 'w') as f:
            json.dump(patients, f, indent=4)

        return {"status": "success", "data": addpatient}
    
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Unable to update patient DB: {str(e)}")
    
UPLOAD_FOLDER = "uploads"


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {
            "status": "success",
            "filename": file.filename,
            "saved_to": file_location
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

if __name__=="__main__":
    uvicorn.run('main:app',host="127.0.0.1",port=8000,reload=True)