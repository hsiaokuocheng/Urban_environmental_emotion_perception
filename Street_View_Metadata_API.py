import requests  #經緯度讀取
import csv
import numpy as np

def generate_grid_coordinates(sw_corner, ne_corner, num_points):
    """在區域內生成更高密度的經緯度網格"""
    # 增加網格點數，使密度更高
    side_length = int(np.sqrt(num_points)) + 1  # 增加邊長點數
    latitudes = np.linspace(sw_corner[0], ne_corner[0], side_length)
    longitudes = np.linspace(sw_corner[1], ne_corner[1], side_length)
    return [(lat, lng) for lat in latitudes for lng in longitudes]

def check_street_view(lat, lng, api_key):
    """檢查某經緯度是否有街景資料"""
    url = "https://maps.googleapis.com/maps/api/streetview/metadata"
    params = {
        "location": f"{lat},{lng}",
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["status"] == "OK"

def get_street_view_coordinates(api_key, sw_corner, ne_corner, num_points=100):
    """獲取有街景資料的經緯度列表"""
    coordinates = generate_grid_coordinates(sw_corner, ne_corner, num_points * 2)  # 生成更多點
    street_view_coordinates = []
    for lat, lng in coordinates:
        if check_street_view(lat, lng, api_key):
            street_view_coordinates.append((lat, lng))
        if len(street_view_coordinates) >= num_points:  # 限制最多 num_points 個點
            break
    return street_view_coordinates

def save_to_csv(coordinates, output_file):
    """將結果保存到 CSV 文件"""
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["latitude", "longitude"])
        writer.writerows(coordinates)

# 示例：定義島嶼區域範圍
api_key = "thisisnottherightkpipleaseapplyurown"  # 替換為你的 Google Maps API 密鑰
sw_corner = (23.472826, 120.438244)  # 西南角經緯度
ne_corner = (23.487572, 120.460219)  # 東北角經緯度

# 執行，增加網格密度
coordinates = get_street_view_coordinates(api_key, sw_corner, ne_corner, num_points=200)
output_file = "street_view_coordinates.csv"

save_to_csv(coordinates, output_file)
print(f"有街景的經緯度已保存到 {output_file}")



