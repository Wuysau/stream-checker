from app.parser import parse_m3u
from app.checker import check_channels
from app.reporter import export_csv, export_json
from utils import ensure_parent_dir

from pathlib import Path


def main():
    output_csv = Path("/data/output/report.csv")
    output_json = Path("/data/output/report.json")
    # print(type(output_csv))
    # print(type(output_josn))
    ensure_parent_dir(str(output_csv))
    ensure_parent_dir(str(output_json))

    print("start check（main）")
    channels = parse_m3u("D:\\Projects\\Python\\stream-checker\\tv.m3u")
    results = []
    for channel in channels:
        results.append(check_channels(channel))

    export_csv(results, str(output_csv))
    export_json(results, str(output_json))
    print(results)
    print("check done")


if __name__ == "__main__":
    main()
