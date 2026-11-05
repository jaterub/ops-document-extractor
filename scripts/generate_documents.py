from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "documents" / "generated"

DOCUMENTS = {
    "INV-1001.pdf": ["INVOICE", "Northstar Freight Supplies Ltd", "Invoice number: NFS-2026-1001", "Invoice date: 2026-10-02", "Due date: 2026-11-01", "Purchase order: PO-7781", "Currency: EUR", "Subtotal: 1200.00", "Tax rate: 21%", "Tax amount: 252.00", "TOTAL: 1452.00"],
    "INV-1002.pdf": ["INVOICE", "Iberia Office Systems SL", "Invoice number: IOS-2026-1002", "Invoice date: 2026-10-05", "Due date: 2026-11-04", "Purchase order: PO-7782", "Currency: EUR", "Subtotal: 500.00", "Tax rate: 21%", "Tax amount: 105.00", "TOTAL: 605.00"],
    "INV-1003.pdf": ["INVOICE", "Blue Harbor Packaging GmbH", "Invoice number: BHP-2026-1003", "Invoice date: 2026-10-08", "Due date: 2026-11-07", "Purchase order: PO-7783", "Currency: EUR", "Subtotal: 800.00", "Tax rate: 10%", "Tax amount: 80.00", "TOTAL: 880.00"],
    "INV-1004.pdf": ["INVOICE", "Northstar Freight Supplies Ltd", "Invoice number: NFS-2026-1004", "Invoice date: 2026-10-12", "Due date: 2026-11-11", "Purchase order: PO-7784", "Currency: EUR", "Subtotal: 1000.00", "Tax rate: 21%", "Tax amount: 200.00", "TOTAL: 1250.00", "SYNTHETIC TEST CASE: totals intentionally do not reconcile."],
    "CTR-2001.pdf": ["SERVICE AGREEMENT", "Contract ID: NFS-SERVICE-2026-01", "Party A: Northstar Freight Supplies Ltd", "Party B: Fictional Logistics Operations SL", "Effective date: 2026-10-01", "Expiry date: 2027-09-30", "Currency: EUR", "Annual value: 24000.00", "Payment terms: 30 days", "Automatic renewal: Yes"],
    "CTR-2002.pdf": ["SUPPLY AGREEMENT", "Contract ID: BHP-SUPPLY-2026-02", "Party A: Blue Harbor Packaging GmbH", "Party B: Fictional Logistics Operations SL", "Effective date: 2026-10-15", "Expiry date: 2027-10-14", "Currency: EUR", "Annual value: 18000.00", "Payment terms: 45 days", "Automatic renewal: No"],
}


def generate_documents() -> list[Path]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    generated = []
    for file_name, lines in DOCUMENTS.items():
        path = OUTPUT_DIR / file_name
        pdf = canvas.Canvas(str(path), pagesize=A4)
        text = pdf.beginText(50, 790)
        text.setFont("Helvetica", 11)
        for line in lines:
            text.textLine(line)
        pdf.drawText(text)
        pdf.save()
        generated.append(path)
    return generated


if __name__ == "__main__":
    paths = generate_documents()
    print(f"Generated {len(paths)} synthetic PDFs in {OUTPUT_DIR}")
