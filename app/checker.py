import time, requests

# from app.parser import parse_m3u

from app.models import Channel, CheckStatus


def check_channels(channel: Channel, timeout: int = 5) -> CheckStatus:
    print("start check")
    start_time = time.time()

    try:
        response = requests.get(channel.url, stream=True, timeout=timeout)
        elapsed_ms = int((time.time() - start_time) * 1000)

        return CheckStatus(
            name=channel.name,
            url=channel.url,
            status="ok",
            status_code=response.status_code,
            response_time=elapsed_ms,
            error="",
        )
    except requests.exceptions.Timeout:
        return CheckStatus(
            name=channel.name,
            url=channel.url,
            status="failed",
            status_code=None,
            response_time=None,
            error="timeout",
        )
    except requests.exceptions.RequestException as e:
        return CheckStatus(
            name=channel.name,
            url=channel.url,
            status="failed",
            status_code=None,
            response_time=None,
            error=str(e),
        )
