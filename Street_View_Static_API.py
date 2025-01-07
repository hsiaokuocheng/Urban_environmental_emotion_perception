import os  #街景讀取
import requests
import csv
import pandas as pd

def fetch_street_view_image(lat, lng, api_key, save_dir):
    """從 Google Street View API 獲取街景圖片"""
    heading = 0  # 固定視角
    save_path = os.path.join(save_dir, f"street_view_{lat}_{lng}.jpg")
    url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "size": "640x640",
        "location": f"{lat},{lng}",
        "heading": heading,
        "pitch": 0,
        "fov": 90,
        "key": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        return save_path
    else:
        print(f"請求失敗 - 狀態碼: {response.status_code}, 錯誤信息: {response.text}")
        return None

def capture_images(input_csv_path, save_dir, api_key):
    """根據 CSV 的經緯度清單截取街景圖片"""
    os.makedirs(save_dir, exist_ok=True)
    df = pd.read_csv(input_csv_path)
    for _, row in df.iterrows():
        lat, lng = row["latitude"], row["longitude"]
        fetch_street_view_image(lat, lng, api_key, save_dir)

# 示例用法
capture_images(
    input_csv_path=r"/content/street_view_coordinates.csv",  # 經緯度清單 CSV 檔案
    save_dir=r"/content/street_view_images",  # 儲存目錄
    api_key="thisisnottherightkpipleaseapplyurown"  # Google Maps API 密鑰