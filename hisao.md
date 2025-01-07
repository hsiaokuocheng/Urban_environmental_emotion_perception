---
title: 'URBAN emotion perception'
subtitle: 'Urban color perception, Urban objectperception'
description: 'using google streerview photos as database'
postDate: 'DECEMBER 2024'
video: '\hsiao_pic\matzu\6_emotion'
colors:
  text: 'text-pearl-bush'
  background: 'bg-orient'
user:
  name: 'Hsiao Kuo Cheng'
  avatar: "/images/avatars/E74096263.jpg"
metadata:
  distance: '5.3 mi'
  altitude: '127 ft'
  location: 'Matzu, Taiwan'
---

Content



# 研究主題 Research TOPIC

運用語意分析模型透過街景圖像，分析都市色彩與都市物件對於居民情緒的相對關係。

---

 **1. 研究簡介 TOPIC detail**
- **[主要主題](#3-文字與顏色標記)**: 街景圖像的環境情緒
- **[研究區域]()**: 馬祖東莒島、嘉義市噴水圓環
- **[分析內容]()**: 色彩情緒分析、環境情緒分析、環境物件分析

上帝視角跟行人視角的謬誤，決定了本研究資料出發點，為街景資料，做為資料基底。針對都市空間，本研究關注都市色彩、常民空間、民生物件的在實際空間的占比，藉此來判斷，環境中對於城市居民的影響。分別使用了兩個大數據模型，來對於空間環境中的情緒判斷。

本研究針對馬祖南竿島與嘉義市圓環，利用城市街景大數據與深度學習方法，分析街景色彩特徵與實體環境元素對於居民情緒的影響。預期研究結果為，色彩複雜度與協調性顯著影響情緒感知，而特定的物件則會讓使用者們，對於環境中的特性，諸如創意、漂亮、安全、有趣等做出反應。適度的色彩複雜性可提升活力，過高則會引起疲勞等；協調的色彩組合增加美感與安全感。本研究為城市規劃提供參考，建議根據區域功能適度調整色彩特徵，並針對特殊環境創造針對性改善方法。
![研究架構diagram](src\assets\images\markdown\research_structure_1.png)


---

 **2. 資料收集 Required Datasets**
- **大量圖像來源 : **Google 街景圖(main)**、社群軟體圖、**

    "研究架構，先以Google street api，依據大量經緯度點，獲取街景圖像做為研究資料。"
    
    圖一表示了，馬祖上所具備街景圖像的所有經緯度點位置，並對每個經緯度點，模擬頭部旋轉角度的不同，總共擷取六張照片，並以這六張照片做為單個經緯度點的分析樣本，以點為單位去做後續分析。圖二為所有點樣本的示意圖片。
    但此方法存在些許誤差，街景圖像的分布狀況若在離島地區，分布較為不均勻。若以嘉義市為例，則採樣標準可信度較高。另一思考方向為，經緯度的採取資料應以街道為基準，或是以矩陣方式為基準，該如何去看待一塊空白的土地?
    
![研究架構diagram](public\hsiao_pic\api_example_1.png)
![研究架構diagram](public\hsiao_pic\api_example_2.png)
    

- **K-means 顏色城市分析模型**
    
    "根據顏色的色調（Hue）、亮度（Lightness）和飽和度（Saturation）分析該顏色可能引發的情緒。"
    
    使用 colorsys.rgb_to_hls 將 RGB 顏色轉換為 HLS 色彩空間，提取色調 (Hue)、亮度 (Lightness) 和飽和度 (Saturation)。
    根據色調分類 (Categorize by hue):

    對顏色的情緒進行初步分類，例如：
    紅色 (Hue 0.0–0.15): 熱情或緊張。
    綠色 (Hue 0.35–0.55): 平靜或自然。
    藍色 (Hue 0.55–0.75): 冷靜或沈穩。
    亮度低，將情緒設定為「憂鬱」。
    亮度高，則情緒設定為「快樂」。

    此模型主要通過顏色特性分析與心理學相關w的情緒反應，應用於場景分析、心理影響研究等領域。
   
![研究架構diagram](public\hsiao_pic\K-means_1.png)

- **PsP net 語意分析模型**

  "PSPNET的用處在於能幫我們分析好畫面中的物件為何。"

    PSPNet（Pyramid Scene Parsing Network）是一種用於
    圖像語意分割的深度學習模型。它最大的創新點在於加入了「金字塔池化模組」（Pyramid Pooling Module），可以理解不同尺度的圖像資訊，幫助模型更好地分析複雜的場景。
    具體來說，「金字塔池化模組」會針對圖片進行四種不同尺度的池化操作，分別是全局池化（1×1）、大範圍池化（2×2）、中等範圍池化（3×3）和小範圍池化（6×6）。這些處理後的結果會再經過疊合和採樣，然後與原始的特徵圖結合，形成包含豐富背景資訊的最終特徵圖。

    簡單來說，PSPNet能讓電腦更聰明地「看懂」圖片中的內容，並且準確地標記每個圖片中，所擁有的物件，以及佔的比例。

![研究架構diagram](public\hsiao_pic\PSPNET_1.png)
![研究架構diagram](public\hsiao_pic\PSPNET_2.png)

- **MIT PLACE PULSE PRETRAINED MODEL**
    
    "而我們則使用這個研究的資料，去對於馬祖及嘉義進行環境的情緒預判。"

    他們的研究始於一個名為「Place Pulse」的群眾外包平台。該平台邀請人們根據評估性問題，例如「哪個地方看起來更安全？」或「更有活力？」，等直觀性的問題從一對圖片中點擊選擇一張。

    Place Pulse 的第一個版本（Place Pulse 1.0）收集了超過 50 萬條偏好數據，這些數據用於評估來自四個城市（波士頓、紐約、林茲和薩爾茨堡）約 4,000 張圖片，並研究城市環境感知品質的空間相關性和不平等現象。幾年後，麻省理工學院的 Place Pulse 團隊推出了平台的更新版本（Place Pulse 2.0），包含來自超過 50 個城市的圖片，並收集了超過 100 萬條偏好數據。

![研究架構diagram](public\hsiao_pic\MIT_1.png)
![研究架構diagram](public\hsiao_pic\MIT_2.png)

**3. 軟體資源 Required Software:**
- 　Google Api 來獲取圖像
- 　Overpass API index
- 　MIT Places Pulse Dataset**
- 　Image-Aware Score Calculation and Classification***
- 　QGIS、OSM、
- 　Google collab

**4. 程式語言 Required Programming**
- Python: For implementing face detection, gaze estimation, data aggregation, and visualization analysis
- Google collab: 使用Google Collab 做為線上撰寫phyton 的平台，使用上述提到的那些預訓練模型


**5. 研究成果 project reference**

- **A.馬祖東莒島**
 
  - 色彩情緒分析
    
    這張gif動圖，總共有兩張圖片，灰黑色的圖片是這些經緯度點上的環境代表色。彩色點圖是代表，這些環境顏色上所能營造的情緒氛圍。
    ![研究架構diagram](public\hsiao_pic\matzu\matzu_color.gif)

  - 環境情緒分析
         
    下方的兩張gif圖，內部總共有六張圖。分別代表了六種不同的情緒。漂亮、無聊、富有、生氣、安全、沮喪等。第一種圖是將原本的圖轉換成情緒熱力圖，用能更簡易閱讀的方式，了解馬祖此地的，情緒分布。
    ![研究架構diagram](public/hsiao_pic/matzu/6_emotion_23.gif)
    ![研究架構diagram](public\hsiao_pic\matzu\hot_strength_dot_combined.png)
    ![研究架構diagram](public\hsiao_pic\matzu\matzu_6_Emotion_dot.gif)
    ![研究架構diagram](public\hsiao_pic\matzu\emotion_6_6_combined.png)
  
  - 馬祖街景實例
    
    以下以一張街景實例，表示環境情緒分析的運用實例。因判定標準是使用前面所述的MIT預訓練模型，所以判定標準的依據，是用大數據所操控。經過筆者主觀判定，判斷標準具有高度可性度。
    ![研究架構diagram](public\hsiao_pic\matzu\matzu_example.png)

   
  - 馬祖東莒島總結 
   
   馬祖東莒島，為一狹小海島地形，街景元素單一，海、灌木叢、零星街屋。情緒的變化值較大出現於少數的街屋區，富有指數與安全指數較高，位於自然環境中的街景圖像則帶來較多，漂亮與無聊的指數分布。


    **高度相關**
    lively_score 與 wealthy_score 有中度正相關 (0.39)：活力感越高的地方往往也顯示出更高的富裕程度。
    safety_score 與 depressing_score 有中度負相關 (-0.66)：安全感越高的地方往往令人壓抑的程度越低。
    boring_score 與 safety_score 有中度正相關 (0.52)：無聊感和安全感之間存在正相關。

    **負相關**
    lively_score 與 boring_score 的負相關較高 (-0.65)：活力感高的地方通常會被認為不無聊。
    beautiful_score 與 lively_score 存在輕微負相關 (-0.25)：美感較高的地方活力可能較低。

    **弱相關**
    latitude 和 longitude 與情緒指標的相關性普遍較低，顯示地理位置對情緒指標的影響可能不顯著。
    結論與建議
    
    ![研究架構diagram](public\hsiao_pic\matzu\matzu_conclusion.png)


            



- **B.嘉義市噴水圓環**
   
  - 色彩情緒分析
    
    圖一表示了，馬祖上所具備街景圖像的所有經緯度點位置，並對每個經緯度點，模擬頭部旋轉角度的不同，總共擷取六張照片，並以這六張照片做為單個經緯度點的分析樣本，以點為單位去做後續分析。圖二為所有點樣本的示意圖片。
    但此方法存在些許誤差，街景圖像的分布狀況若在離島地區，分布較為不均勻。若以嘉義市為例，則採樣標準可信度較高。另一思考方向為，經緯度的採取資料應以街道為基準，或是以矩陣方式為基準，該如何去看待一塊空白的土地?
    ![研究架構diagram](public\hsiao_pic\chiayi\color_emotion.png)

  - 環境情緒分析
         
    圖一表示了，馬祖上所具備街景圖像的所有經緯度點位置，並對每個經緯度點，模擬頭部旋轉角度的不同，總共擷取六張照片，並以這六張照片做為單個經緯度點的分析樣本，以點為單位去做後續分析。圖二為所有點樣本的示意圖片。
    但此方法存在些許誤差，街景圖像的分布狀況若在離島地區，分布較為不均勻。若以嘉義市為例，則採樣標準可信度較高。另一思考方向為，經緯度的採取資料應以街道為基準，或是以矩陣方式為基準，該如何去看待一塊空白的土地?
    ![研究架構diagram](public\hsiao_pic\chiayi\chiayi_emotion_motion.gif)
  
  - 嘉義街景實例
    
    這張是位於嘉義市圓環附近的街景圖像，可以跟上段馬祖的街景圖像，進行海島與都市的環境情緒比較。
    ![研究架構diagram](public\hsiao_pic\chiayi\CHIAYI_eXAMPLE.png)
  
  - 嘉義總結

    都市環境的組構元素較為複雜，但仍有許多可預期的判斷基準出現。例如街屋的高低對於負面情緒的影響，或者是都市綠帶、都市公園的出現，會對於正面情緒的回饋較高。而十字路口、馬路寬廣的街景圖像，對於安全值的回饋十分直接，整體而言都市環境的分析，仍需要更多街景圖像做為數據基底去進行分析。


    **beautiful_score 與其他情緒的關係：**
    與 lively_score 的相關性最高（0.50）：表示美感分數越高的地方，也傾向於被認為更有活力。
    與 wealthy_score 的相關性為 0.44：顯示美感與富裕程度具有中等正相關。
    與 depressing_score 為負相關（-0.16）：顯示越美感的地方，越不容易被認為令人壓抑。

    **wealthy_score 與其他情緒的關係：**
    與 lively_score 的相關性為 0.40：表示富裕程度越高的地方，也被認為更有活力。
    與 depressing_score 為負相關（-0.32）：顯示富裕程度越高的地方，越不容易令人感到壓抑。

    **safety_score 與其他情緒的關係：**
    與 beautiful_score 的相關性為 0.20：安全感與美感之間有弱相關。
    與 depressing_score 的相關性為 -0.32：顯示安全感越高的地方，越不容易令人感到壓抑。
    lively_score 與其他情緒的關係：
    與 beautiful_score 的相關性最高（0.50）：活力與美感之間關係密切。
    與 wealthy_score 的相關性為 0.40：活力與富裕程度具有正相關。

    **depressing_score 與其他情緒的關係：**
    與大多數情緒呈負相關（如 wealthy_score 和 safety_score 均為 -0.32）：壓抑感高的地方，通常與富裕和安全感低相關。
    與 boring_score 幾乎無相關（-0.03）：顯示壓抑感和無聊感之間的關係不明顯。

    **boring_score 與其他情緒的關係：**
    與其他指標相關性都很低，顯示無聊感並未受到其他情緒指標的顯著影響。


    ![研究架構diagram](public\hsiao_pic\chiayi\chiayi_conclusion.png)



**6. 後續應用可能性 Potential design method**

本研究結合城市景觀大數據與深度學習方法，對街景色彩特徵與環境情緒進行分析，揭示了城市空間元素與居民感知之間的重要關聯，對未來設計實踐具有多方面的啟發與應用潛力。

1. **城市色彩規劃與設計**
 研究結果表明，色彩複雜度與協調性調整能夠影響情緒感知。這一發現可被應用於城市色彩規劃，針對不同場景功能設計色彩組合。在住宅區可選擇情緒的低複雜度色彩組合，以提升居民的安全感與舒適感；而商業或文化區則可通過增加色彩的多樣性與鮮豔度，以激活活力和吸引力。此外，研究提出「適度的色彩複雜性」能提升活力，這可作為創建具有吸引力的公共空間或商業街區的設計原則。

2. **人本導向的都市家具設計**
研究指出，特定的物件（如都市家具或公共設施）能顯著影響居民對環境情緒的感知。例如愉悅、美觀、安全與舒適等心理感受。未來在城市家具設計上，可結合研究提供的情緒指標，設計富有居民需求的公共設施。例如，在現場線條語言增加創造性與友善的設施；或在街家具空間設置讓人感覺溫馨安全的座椅設計。
1. **空間功能導向的場景營造**
研究強調，街景物件與色彩對居民情緒的作用，可用於引導城市設計不同功能區的場景營造。例如，在街向通路（如重慶路口）這類交通樞紐地帶，設計時可考慮減少混雜疲勞的色彩與物件組合，避免交通狀態對使用者情緒造成負面影響。而對於特定地區（如馬祖南竿書局），則可利用鮮明的色彩與有趣的物件提升吸引力。
1. **精準地圖設計輔助工具**
研究方法中使用的精準地圖，將語意分析、色彩分析與情緒評估結合於不同功能性場景的設計需求。例如，針對城市更新場景中，設計輔助工具能夠提供具體數據與地圖支援，幫助設計師識別需改善的空間，並提供建議的設計方向。透過這些數據導向的設計方法，將提高設計的針對性與科學性。
1. **支持地方特色的規劃策略**
針對不同地區（如馬祖南竿島與嘉義市圓環）的研究結果，顯示環境設計需要參考地域文化與特色。未來在進行地方空間設計時，可結合研究方法，分析當地的街景特徵與居民情緒需求，進而提出量身訂製的規劃方案，創造既符合功能需求又能展現地方特色的空間。


**7. 參考範例 project reference**
- https://www.mdpi.com/2076-3417/14/20/9521 
- https://www.jstor.org/stable/43030760?seq=7
- https://developers.google.com/maps/documentation/javascript/get-api-key?hl=zh-tw
- https://www.media.mit.edu/projects/place-pulse-new/overview/
- https://paperswithcode.com/dataset/place-pulse-2-0
- https://github.com/strawmelon11/human-perception-place-pulse
- https://medium.com/image-processing-and-ml-note/pspnet-winner-in-ilsvrc-2016-semantic-segmentation-scene-parsing-800879d513e











