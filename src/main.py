import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.item import unique_router, runeword_router, set_item_router

LOG_LEVEL = logging.INFO

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# app = FastAPI(root_path="/api/v1", openapi_url="/api/v1/openapi.json", docs_url="/api/v1/docs", redoc_url="/api/v1/redoc")
app = FastAPI()

# CORS policies
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(unique_router, tags=["uniques"], prefix="/uniqueitems")
app.include_router(runeword_router, tags=["runewords"], prefix="/runeworditems")
app.include_router(set_item_router, tags=["sets"], prefix="/setitems")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

