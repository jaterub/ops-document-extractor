import json

from app.main import GROUND_TRUTH_PATH
from scripts.generate_documents import DOCUMENTS


def test_ground_truth_has_unique_ids_and_expected_document_types():
    records = [json.loads(line) for line in GROUND_TRUTH_PATH.read_text(encoding="utf-8").splitlines()]
    assert len(records) == 6
    assert len({record["document_id"] for record in records}) == len(records)
    assert {record["document_type"] for record in records} == {"invoice", "contract"}
    assert all(record["source"] == "synthetic" for record in records)


def test_invoice_ground_truth_includes_injected_mismatch():
    records = [json.loads(line) for line in GROUND_TRUTH_PATH.read_text(encoding="utf-8").splitlines()]
    mismatch = next(record for record in records if record["document_id"] == "INV-1004")
    assert mismatch["expected_issues"] == ["tax_amount_mismatch", "total_amount_mismatch"]


def test_pdf_generator_creates_all_documents(tmp_path, monkeypatch):
    import scripts.generate_documents as generator

    monkeypatch.setattr(generator, "OUTPUT_DIR", tmp_path)
    paths = generator.generate_documents()
    assert len(paths) == len(DOCUMENTS)
    assert all(path.exists() and path.read_bytes().startswith(b"%PDF") for path in paths)
