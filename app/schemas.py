from typing import Literal

from pydantic import BaseModel, ConfigDict


class DatasetDocument(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document_id: str
    document_type: Literal["invoice", "contract"]
    file_name: str
    source: Literal["synthetic", "public"]
    expected_fields: dict[str, str | int | float | bool | None]
    expected_issues: list[str]
