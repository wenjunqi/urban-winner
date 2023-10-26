import requests  # 导入requests库，用于发送HTTP请求

# API的地址
url = "https://v.api.aa1.cn/api/phone/guishu-api.php"

# 输入要查询的手机号
phone_number = input("请输入要查询的手机号：")

# 构建请求参数
params = {
    "phone": phone_number  # 将输入的手机号作为参数传递给API
}

try:
    # 发送GET请求
    response = requests.get(url, params=params)  # 发送GET请求到API

    # 检查响应状态码
    if response.status_code == 200:  # 如果响应状态码是200，表示请求成功
        # 解析JSON响应
        data = response.json()  # 将API响应解析为JSON格式的数据

        # 检查API返回的code字段，0表示成功，非0表示出错
        if data["code"] == 0:
            province = data["data"]["province"]  # 提取JSON响应中的省份信息
            city = data["data"]["city"]  # 提取JSON响应中的城市信息
            sp = data["data"]["sp"]  # 提取JSON响应中的运营商信息
            print(f"手机号 {phone_number} 所属省份: {province}")  # 打印手机号的省份信息
            print(f"手机号 {phone_number} 所属城市: {city}")  # 打印手机号的城市信息
            print(f"手机号 {phone_number} 运营商: {sp}")  # 打印手机号的运营商信息
        else:
            print(f"API返回错误码: {data['code']}")  # 打印API返回的错误码
    else:
        print(f"请求失败，状态码: {response.status_code}")  # 打印请求失败的状态码
except Exception as e:
    print(f"发生异常: {str(e)}")  # 打印发生的异常信息
