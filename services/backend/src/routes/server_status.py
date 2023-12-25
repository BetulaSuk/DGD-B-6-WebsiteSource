from fastapi import APIRouter, HTTPException
import psutil

router = APIRouter()

@router.get(
    "/server"
)
async def get_server_status():
    disk = psutil.disk_usage('/').percent
    mem = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1)
    return {
        "disk_usage": disk,
        "mem_usage": mem,
        "cpu_usage": cpu
    }

