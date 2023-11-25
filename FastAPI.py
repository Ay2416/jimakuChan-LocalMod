from googletrans import Translator
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
translator = Translator()

origins = [
    "http://localhost",
    "http://localhost:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=PlainTextResponse)
async def trancelate_text(text: str, source: str, target:str):    
    return translator.translate(text, src=source, dest=target).text

if __name__ == "__main__":
    uvicorn.run(app)