from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.item import unique_router, runeword_router, set_item_router

app = FastAPI(openapi_url="/openapi.json")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(unique_router, tags=["uniques"], prefix="/uniqueitems")
app.include_router(runeword_router, tags=["runewords"], prefix="/runeworditems")
app.include_router(set_item_router, tags=["sets"], prefix="/setitems")
