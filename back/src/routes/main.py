from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def main():
    return {"response": "Funcionando!"}