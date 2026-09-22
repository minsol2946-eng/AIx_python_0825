
import requests

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
res = requests.get(url, headers)

res.raise_for_status() # 에러나면 프로그램 종료

with open("melon.html","w",encoding="utf8") as f:
    f.write(res.text)

print("저장완료")