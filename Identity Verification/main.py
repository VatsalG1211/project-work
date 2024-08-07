import cv2
import numpy as np
import pytesseract
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
import io
from Processing_Model import process_image
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.post("/verify")
async def verify(
    first_name: str = Form(...),
    last_name: str = Form(...),
    surname: str = Form(...),
    pan_number: str = Form(...),
    image: UploadFile = File(...)
):
    image_bytes = await image.read()
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    if image.shape[1] != 880 or image.shape[0] != 495:
        return JSONResponse(content={"message": "Image size must be 880 x 495."}, status_code=400)

    data = process_image(image)

    if not data:
        return JSONResponse(content={"message": "Failed to extract data from the image."}, status_code=400)

    extracted_first_name, extracted_last_name, extracted_surname, extracted_pan_number = data

    if (first_name.upper() == extracted_first_name and
        last_name.upper() == extracted_last_name and
        surname.upper() == extracted_surname and
        pan_number.upper() == extracted_pan_number):
        return {"message": "The information matches."}
    else:
        return {"message": "The information does not match."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
