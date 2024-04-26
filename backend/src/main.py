from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from src.db.session import init_db
from fastapi.staticfiles import StaticFiles
from src.api.tutorials import router as tutorial_router
import os


def app() -> FastAPI:
    init_db()
    app = FastAPI(
        title="Challenge-Accepted",
        version="1.0.0",
        swagger_ui_parameters={"tryItOutEnabled": True},
        root_path="/api",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.add_1vent_handler("startup", tasks.create_start_app_handler(app))
    # app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))

    if not os.path.exists("../backend/resources"):
        os.makedirs("../backend/resources")

    app.include_router(tutorial_router)

    app.mount(
        "/resources",
        StaticFiles(directory="../backend/resources"),
        name="resources",
    )

    @app.get("/", include_in_schema=False)
    async def docs_redirect():
        return RedirectResponse(url="/api/docs")

    return app


if __name__ == "__main__":
    app()
