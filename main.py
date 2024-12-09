from fastapi import FastAPI
import debugpy
from controllers.api import router

debugpy.listen(("0.0.0.0", 5678))
app = FastAPI()
app.include_router(router)

