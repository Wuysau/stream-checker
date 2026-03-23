from dataclasses import dataclass


@dataclass
class Channel:
    name: str
    url: str


@dataclass
class CheckStatus:
    name:str
    url:str
    status:str
    status_code:int
    response_time:int
    error:str


c1 = Channel(name="cctv1", url="fdajfa")
c2 = Channel(name="cctv2", url="fafda")
print(c1)
print(c2)
