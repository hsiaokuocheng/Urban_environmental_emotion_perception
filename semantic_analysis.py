import os  #語意分析
import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import csv

# 檢查是否有可用的 GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 載入 PSPNet 模型並加載到適當的設備（CPU 或 GPU）
model = torch.hub.load('pytorch/vision:v0.10.0', 'fcn_resnet101', pretrained=True)
model.to(device)
model.eval()

# 定義圖像轉換
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

LABELS = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle",
    "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
    "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

def segment_image(image_path):
    """對圖片進行語意分割"""
    input_image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0).to(device)  # 將數據加載到設備（CPU 或 GPU）

    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0).cpu().numpy()  # 將結果移回 CPU 以進行處理

    return output_predictions

def analyze_semantics(image_folder, save_csv_path):
    """分析資料夾內所有圖片的語意分割"""
    os.makedirs(os.path.dirname(save_csv_path), exist_ok=True)
    results = []

    for image_name in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_name)
        if not os.path.isfile(image_path):  # 忽略非檔案對象
            continue

        print(f"Processing image: {image_name}")
        segment_map = segment_image(image_path)

        object_counts = np.bincount(segment_map.flatten(), minlength=len(LABELS))
        total_pixels = segment_map.size
        object_proportions = {LABELS[i]: round(count / total_pixels, 4) for i, count in enumerate(object_counts) if count > 0}

        results.append({"image_name": image_name, "object_proportions": object_proportions})

    # 儲存為 CSV
    with open(save_csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["image_name", "object_proportions"])
        writer.writeheader()
        for result in results:
            writer.writerow({
                "image_name": result["image_name"],
                "object_proportions": str(result["object_proportions"])
            })

    print(f"Semantic analysis saved to {save_csv_path}")

# 示例用法
analyze_semantics(
    image_folder="/content/street_view_images",  # 圖片資料夾
    save_csv_path="/content/semantic_analysis.csv"  # 儲存 CSV 檔案
)
