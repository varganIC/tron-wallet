import uvicorn
from fastapi import FastAPI

from api_routes import metadata, wallet
from settings.settings_loader import uvicorn_settings

app = FastAPI(title=metadata.title)

app.include_router(wallet.router)


if __name__ == "__main__":
    uvicorn.run(app, **uvicorn_settings)
