from pathlib import Path
import json

from fastapi import FastAPI, HTTPException

from app.schemas import DatasetDocument

ROOT_DIR = Path(__file__).resolve().parents[1]
GROUND_TRUTH_PATH = ROOT_DIR / "data" / "ground_truth.jsonl"

app = FastAPI(
    title="Operations Document Extractor",
    description="Extract and validate structured data from invoices and contracts.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/documents", response_model=list[DatasetDocument], tags=["dataset"])
def list_documents() -> list[DatasetDocument]:
    if not GROUND_TRUTH_PATH.exists():
        raise HTTPException(status_code=503, detail="Ground-truth dataset is not available.")

    records = []
    for line in GROUND_TRUTH_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(DatasetDocument.model_validate(json.loads(line)))
    return records
