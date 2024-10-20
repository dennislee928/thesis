# Black Hole Simulation

## 簡介

政大數位內容碩士學位學程-110462011 李沛宸的畢業論文程式模擬部分：此專案使用 QuTiP 來模擬量子糾纏態，並通過考慮距離、雜訊和封包大小等因素來模擬數據丟失率。專案中包含多種情境的數據丟失模擬。

## 目錄

- [安裝](#安裝)
- [使用方法](#使用方法)
- [功能](#功能)
- [貢獻](#貢獻)
- [授權](#授權)
- [聯絡](#聯絡)

## 安裝

1. 確保已安裝 Python 和 pip。
2. 安裝 QuTiP 和其他依賴：
   ```bash
   pip install qutip numpy matplotlib
   ```
3. 或是用 docker 跑
   拉取映像：docker pull dennisleetw/blackhole-simulation:latest
   運行映像：docker run -it dennisleetw/blackhole-simulation:latest

## 使用方法

運行 `blackhole_simulation.py` 來模擬數據丟失：

這將生成不同封包大小下的數據丟失曲線圖。

## 功能

- 初始化量子糾纏態。
- 模擬數據丟失率，考慮距離、雜訊、封包大小、環境因素和網路擁塞。
- 提供多種情境的數據丟失模擬：
  - 小封包高丟失率
  - 短距離高丟失率
  - 小封包和短距離高丟失率
  - 大封包和長距離高丟失率

## 貢獻

如果你想貢獻，請遵循以下步驟：

1. Fork 此儲存庫
2. 創建你的分支 (`git checkout -b feature/你的功能`)
3. 提交你的更改 (`git commit -m '添加一些功能'`)
4. 推送到分支 (`git push origin feature/你的功能`)
5. 創建一個新的 Pull Request
6. 學貓咪喵喵叫
7. 然後
8. 猛力衝刺！！！！！！

## 授權

此專案使用 [MIT License](LICENSE) 授權。

## 聯絡

- 110462011@g.nccu.edu.tw
