from fastapi import APIRouter
import importlib
import os

def register_routes(app):
    routes_dir = os.path.dirname(__file__)
    for filename in os.listdir(routes_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            route_module = importlib.import_module(f"app.routes.{filename[:-3]}")
            app.include_router(route_module.router)
