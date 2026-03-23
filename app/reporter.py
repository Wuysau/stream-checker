import csv, json
from dataclasses import asdict

from app.models import CheckStatus


def export_csv(results: list[CheckStatus], file_path: str) -> None:
    with open(file_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "name",
                "url",
                "status",
                "status_code",
                "response_time",
                "error",
            ],
        )
        writer.writeheader()
        for result in results:
            writer.writerow(asdict(result))


def export_json(results: list[CheckStatus], file_path: str) -> None:
    data = [asdict(result) for result in results]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
