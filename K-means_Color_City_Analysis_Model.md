### How does  K-means Color City Analysis Model work?


- **K-means Color City Analysis Model**

    "Based on the hue, lightness, and saturation of colors, analyze the emotions these colors may evoke."

    Using `colorsys.rgb_to_hls`, RGB colors were converted to the HLS color space to extract Hue, Lightness, and Saturation. 

    Preliminary emotional classification based on hue includes:
    - **Red (Hue 0.0–0.15)**: Passionate or tense
    - **Green (Hue 0.35–0.55)**: Calm or natural
    - **Blue (Hue 0.55–0.75)**: Cool or steady

    Lower lightness is associated with "melancholy," while higher lightness is linked to "happiness." This model primarily analyzes emotional responses associated with color properties and is applicable to scene analysis and psychological impact studies.

![K-means Model Diagram](hsiao_pic\K-means_1.png)

---
### How to Use the Script: [Color Emotion Analysis](color_emotion_analysis.py) as example

This guide will walk you through the steps to use the Python script for analyzing dominant colors and their associated emotions in a folder of images, saving the results to a CSV file.


#### Step 1: Install Required Python Packages

Make sure Python (3.x or higher) is installed on your system. Then, install the required Python libraries:

```bash
pip install opencv-python-headless scikit-learn pandas
```

#### Step 2: Update Script Parameters
Open the [Color Emotion Analysis](color_emotion_analysis.py) and update the following variables to match your requirements:

```python
image_folder = "/path/to/your/image_folder"  # Replace with the path to the folder containing your images
save_csv_path = "/path/to/save/color_emotion_analysis.csv"  # Replace with the path to save the analysis results as a CSV file
```
### Step 3: Run the Script
Save the script as color_emotion_analysis.py. Run the script using the following command:
```bash
python color_emotion_analysis.py
```

### Step 4: Output
The script will generate a CSV file (color_emotion_analysis.csv) containing the following columns:

- image_name: The name of the image file.
- dominant_color: The most dominant color (in RGB format) found in the image.
- emotion: The primary emotion associated with the dominant color.


