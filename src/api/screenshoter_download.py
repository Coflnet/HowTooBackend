from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse


router = APIRouter(tags=["ScreenShoter"])


@router.get("/screenshoter/")
async def download_screenshoter_exe():
    file_path = "./src/how_too.exe"
    return FileResponse(
        path=file_path, filename="how_too.exe", media_type="application/octet-stream"
    )
