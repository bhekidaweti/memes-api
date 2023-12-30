import fastapi as _fastapi
import fastapi.responses as _responses


app = _fastapi.FastAPI()

import services as _services

@app.get("/")
def root():
    return {"message": "Welcome to memes API"}

@app.get("/general-memes")
def get_general_memes():
    image_path = _services.select_random_image("memes")
    return _responses.FileResponse(image_path)

@app.post("/memes")
def create_meme(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("memes", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="incorrect file type")
    return _responses.FileResponse(file_path)