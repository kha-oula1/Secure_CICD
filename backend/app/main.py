from fastapi import FastAPI

app = FastAPI(title="DentalFlow")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "DentalFlow API is running"}