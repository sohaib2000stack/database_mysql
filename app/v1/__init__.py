from fastapi import FastAPI
from app.v1.endpoints import router as v1_router
# from app.v1.signup import router as signup_router
router = FastAPI()


router = FastAPI()
router.include_router(v1_router, prefix="/api/v1")
# router.include_router(signup_router, prefix="/api/v1")