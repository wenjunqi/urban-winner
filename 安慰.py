import requests

# API地址
api_url = "https://v.api.aa1.cn/api/api-wenan-anwei/index.php"

# 请求参数
params = {
    "type": "json"
}

# 发送GET请求
response = requests.get(api_url, params=params)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()

    # 获取文案
    anwei = data.get("anwei")

    # 打印文案
    print("文案：", anwei)
else:
    print("请求失败，状态码：", response.status_code)
