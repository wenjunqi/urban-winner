import requests

# 定义API地址
api_url = "https://api.vvhan.com/api/rand.music"

# 设置请求参数
params = {
    "type": "all",  # 输出全部类型
    "sort": "排行榜"  # 歌单名称，你可以根据需要更改
}

try:
    # 发送GET请求
    response = requests.get(api_url, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析JSON响应
        data = response.json()

        # 遍历歌曲信息
        for song_info in data:
            # 提取返回的参数
            song_name = song_info.get('name')
            artist = song_info.get('auther')
            mp3_url = song_info.get('mp3url')
            img_url = song_info.get('imgurl')

            # 输出结果
            print("歌曲名:", song_name)
            print("艺术家:", artist)
            print("MP3链接:", mp3_url)
            print("封面链接:", img_url)
    else:
        print("请求失败，状态码：", response.status_code)

except Exception as e:
    print("发生异常：", str(e))
