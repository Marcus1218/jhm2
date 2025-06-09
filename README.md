## JHM2 專案總覽

這是 JHM2 的倉庫，包含多個 Python 小專案。  
如需參考請先告知作者，請勿直接抄襲！

### 專案列表

#### Chill_guy
- **main.py**  
  可能涉及音訊播放，需安裝 `pygame`。
  ```
  pip install pygame
  ```

#### Expenses_Tracker
- **main.py**  
  基本的記帳功能，無特殊依賴（如有用到 pandas 請安裝）。
  ```
  pip install pandas
  ```

#### Ghost_Leg
- **main.py**  
  可能為遊戲或隨機分配工具，若有 GUI 需求建議安裝 `tkinter`（Python 內建）。

#### Pygame
- **main.py**  
  使用 `pygame` 製作的遊戲或多媒體應用。
  ```
  pip install pygame
  ```

#### Stock_Prediction
- **Download_data.py, main.py**  
  股票數據下載與預測，建議安裝：
  ```
  pip install pandas yfinance scikit-learn matplotlib
  ```

#### Weather
- **Weather_api.py**  
  天氣查詢，需安裝 `requests`。
  ```
  pip install requests
  ```

---

## 專案檔案結構簡介

本倉庫包含以下主要資料夾與檔案：

- `Chill_guy/`：音訊播放相關專案，含 `main.py` 及音檔。
- `Expenses_Tracker/`：簡易記帳工具，含 `main.py`。
- `Ghost_Leg/`：遊戲或分配工具，含 `main.py`。
- `Pygame/`：以 pygame 製作的遊戲或多媒體專案，含多個圖片與 `main.py`。
- `Stock_Prediction/`：股票數據下載與預測，含 `Download_data.py`、`main.py`。
- `Weather/`：天氣查詢工具，含 `Weather_api.py`。
- `README.md`：本說明文件。

---

## 各 Python 檔案用途說明

- `Chill_guy/main.py`：用於播放音樂或音效，結合 mp3 檔案（如 `yeahyeahyeahsmapsclip.mp3`），適合做簡單的音訊應用或娛樂小工具。
- `Expenses_Tracker/main.py`：記帳或支出追蹤工具，適合個人財務管理。
- `Ghost_Leg/main.py`：實現「鬼腳圖」遊戲或隨機分組分配，常用於抽籤或分隊。
- `Pygame/main.py`：利用 pygame 製作的遊戲或互動多媒體程式，結合多張圖片資源，適合學習遊戲開發。
- `Stock_Prediction/Download_data.py, main.py`：用於下載股票資料並進行股價預測，結合資料分析與機器學習。
- `Weather/Weather_api.py`：查詢天氣資訊，通常會調用天氣 API 並顯示結果。

這些 Python 程式涵蓋了多媒體、遊戲、資料分析、API 應用等多種主題，適合學習不同領域的 Python 實作。

---

### 聯絡方式
Discord: marcus_1218
OK
