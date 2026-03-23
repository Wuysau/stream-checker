from app.parser import parse_m3u
from app.checker import check_channels
from app.reporter import export_csv, export_json


def main():
    print("start check（main）")
    channels = parse_m3u("D:\\Projects\\Python\\stream-checker\\tv.m3u")
    results = []
    for channel in channels:
        results.append(check_channels(channel))

    export_csv(results, "./data/output/report.csv")
    export_json(results, "./data/output/report.json")
    print(results)
    print("check done")


if __name__ == "__main__":
    main()
