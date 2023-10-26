import requests

# 指定要请求的网址
url = "https://www.cloudflare.com/cdn-cgi/trace"  # 替换为您要请求的实际网址

try:
    # 发送GET请求
    response = requests.get(url)

    # 检查响应状态码，200表示请求成功
    if response.status_code == 200:
        # 打印网址的内容
        print(response.text)
    else:
        print(f"请求失败，状态码：{response.status_code}")

except requests.exceptions.RequestException as e:
    # 处理请求异常
    print(f"发生请求异常：{e}")