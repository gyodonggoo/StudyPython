from urllib.request import urlopen
from bs4 import BeautifulSoup

target = urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, "html.parser")
# print(soup)

for location in soup.select("location"):
    # print(location)
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()