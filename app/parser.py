from app.models import Channel


def parse_m3u(file_path: str) -> list[Channel]:
    channels = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(len(lines)):
        line = lines[i]

        if line.startswith("#EXTINF"):
            name = line.split(",", 1)[1]

            if i + 1 < len(lines):
                url = lines[i + 1]
                if url.startswith("http"):
                    channels.append(Channel(name=name, url=url))

    return channels


# print(parse_m3u("D:\\Projects\\Python\\stream-checker\\tv.m3u"))
