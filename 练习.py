# # 引入必要的库
# import requests
# import json
#
# # API地址
# url = 'https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json'
#
# # 发送GET请求到API
# response = requests.get(url)
#
# # 检查响应状态码
# if response.status_code == 200:
#     # 解析JSON响应
#     res = json.loads(response.text)
#
#     # 获取文案
#     text = res['anwei']
#
#     # 打印文案
#     print("每日一言示例：", text)
# else:
#     print("请求失败，状态码：", response.status_code)
