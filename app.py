from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from s3_manager import S3Manager
import os
import tempfile

app = FastAPI(title="S3 File Manager")

try:
    s3_manager = S3Manager()
except ValueError as e:
    print(f"Error initializing S3Manager: {e}")
    s3_manager = None

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/files")
async def list_files():
    if not s3_manager:
        raise HTTPException(status_code=500, detail="S3 Manager not initialized. Check your .env file.")
    
    try:
        files = s3_manager.list_files()
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    if not s3_manager:
        raise HTTPException(status_code=500, detail="S3 Manager not initialized. Check your .env file.")
    
    try:
        s3_manager.upload_fileobj(file.file, file.filename)
        return {"message": f"File '{file.filename}' uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/download/{file_key:path}")
async def download_file(file_key: str):
    if not s3_manager:
        raise HTTPException(status_code=500, detail="S3 Manager not initialized. Check your .env file.")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        s3_manager.download_file(file_key, tmp_path)
        
        filename = os.path.basename(file_key)
        
        return FileResponse(
            tmp_path,
            media_type='application/octet-stream',
            filename=filename,
            background=None
        )
    except Exception as e:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/delete/{file_key:path}")
async def delete_file(file_key: str):
    if not s3_manager:
        raise HTTPException(status_code=500, detail="S3 Manager not initialized. Check your .env file.")
    
    try:
        s3_manager.delete_file(file_key)
        return {"message": f"File '{file_key}' deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/temp-link/{file_key:path}")
async def get_temp_link(file_key: str, expiration: int = 3600):
    if not s3_manager:
        raise HTTPException(status_code=500, detail="S3 Manager not initialized. Check your .env file.")
    
    try:
        url = s3_manager.generate_presigned_url(file_key, expiration)
        return {"url": url, "expiration": expiration}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/perm-link/{file_key:path}")
async def get_perm_link(file_key: str):
    if not s3_manager:
        raise HTTPException(status_code=500, detail="S3 Manager not initialized. Check your .env file.")
    
    try:
        url = s3_manager.get_permanent_url(file_key)
        return {"url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "s3_configured": s3_manager is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)