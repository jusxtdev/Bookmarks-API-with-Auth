from fastapi import FastAPI

from app.database import init_db
from app.routers import resource, user

app = FastAPI()

@app.on_event('startup')
def on_startup():
    init_db()

app.include_router(resource.router)        ## Include routers
app.include_router(user.router)        ## Include routers