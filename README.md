![研究架構diagram](hsiao_pic/research_conceptdrawing.png)


# My Project Frontage
- **[Research topic](#3-文字與顏色標記)**: Emotional perception of street view images
- **[Research Areas]()**: Dongju Island , Matsu
- **[Analysis Content]()**: Color emotion analysis, environmental emotion analysis, and environmental object analysis
- **[Required Software and model]()**: Google map API key, MIT Places Pulse Dataset, QGIS,
---
### Intro
The fallacies of the "god's-eye view" and the "pedestrian perspective" determine the starting point of this study, which relies on street view data as the foundational dataset. This research focuses on urban spaces, paying attention to urban colors, common spaces, and the proportion of livelihood-related objects in actual spaces, to assess their impact on city residents. Two large-scale data models are employed to evaluate emotional responses to spatial environments.

This study analyzes the impact of street view color characteristics and physical environmental elements on residents' emotions, focusing on Nangan Island in Matsu and the traffic circle in Chiayi City. Using urban street view big data and deep learning methods, the research aims to identify how these elements influence perceptions. Expected findings include that color complexity and harmony significantly affect emotional perception. Specific objects in the environment may prompt users to respond to characteristics such as creativity, beauty, safety, and fun. Moderate color complexity is expected to enhance vitality, while excessive complexity may induce fatigue. Harmonious color combinations are anticipated to enhance aesthetics and a sense of safety. This study offers insights for urban planning, suggesting that color characteristics be adjusted appropriately based on regional functions and recommending targeted improvement strategies for specific environments.

---
### Workflow
1. use google api to collecting street views pictures and set
2. use google 



### **Model tutorial**

Plz read the tutorial by order, or you are not going to generate the right data.
  1. [Google api tutorial](Google_api_tutorial) 
  2. [K-means Color City Analysis Model](K-means_Color_City_Analysis_Model.md)
  3. [PSPNet Semantic Analysis Model](PSPNet_Semantic_Analysis_Model.md)
  4. [MIT Place Pulse Pretrained Model](Google_api_tutorial)


### **4. Required Programming**
- **Python**: For implementing face detection, gaze estimation, data aggregation, and visualization analysis
- **Google Colab**: Used as an online platform for Python coding, integrating pretrained models mentioned above.

---

### Research Results

#### **A. Dongju Island, Matsu**

- **Color Emotion Analysis**

    A GIF demonstrates representative environmental colors (gray-scale image) and corresponding emotional atmospheres (colored dot map) for different latitude and longitude points.

    ![Matsu Color GIF](hsiao_pic\matzu\matzu_color.gif)

- **Environmental Emotion Analysis**

    Heatmaps and dot maps represent six emotions (beautiful, boring, wealthy, angry, safe, depressed). Original images were transformed into easy-to-read emotion distribution maps.

    ![Emotion Heatmap](hsiao_pic\matzu\hot_strength_dot_combined.png)
    ![Emotion Dot Map](hsiao_pic\matzu\matzu_6_Emotion_dot.gif)

- **Matsu Street View Example**

    Below is a street view image example showcasing the practical application of environmental emotion analysis. Standards for emotional judgments are based on large-scale data controlled by the pretrained MIT model.

    ![Street View Example](hsiao_pic\matzu\matzu_example.png)

- **Summary of Dongju Island**

    Matsu's narrow island geography results in single-element street views, primarily sea, shrubs, and scattered street houses. Emotional variations are significant near street houses, with high indices for wealth and safety, while natural environments elicit beauty and boredom.

    - **Positive Correlations**
        - Lively score and wealthy score (0.39): Higher liveliness correlates with perceived wealth.
        - Safety score and depressing score (-0.66): Higher safety reduces perceived depression.

    - **Negative Correlations**
        - Lively score and boring score (-0.65): Higher liveliness corresponds to lower boredom.

    - **Weak Correlations**
        - Geographic latitude and longitude have minimal impact on emotional indices.

    ![Matsu Conclusion](hsiao_pic\matzu\matzu_conclusion.png)


Potential Applications**

1. **Urban Color Planning and Design**
2. **Human-Oriented Urban Furniture Design**
3. **Function-Oriented Scene Creation**
4. **Precision Map Design Tools**
5. **Region-Specific Planning Strategies**

---

### **7. References**
- [Research on Semantic Urban Perception](https://www.mdpi.com/2076-3417/14/20/9521)
- [Place Pulse Overview](https://www.media.mit.edu/projects/place-pulse-new/overview/)
- [PSPNet Explanation](https://medium.com/image-processing-and-ml-note/pspnet-winner-in-ilsvrc-2016-semantic-segmentation-scene-parsing-800879d513e)
