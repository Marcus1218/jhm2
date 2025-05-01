import yfinance as yf
import sys

# 提示用户输入趋势（股票代码）
trend = input("input：")
if not trend:
    print("input invoild value。")
    sys.exit(1)

# 下载数据
try:
    data = yf.download(trend, start="2020-01-01", end="2025-04-25")
    if data.empty:
        print("error。")
        sys.exit(1)
    print("Done")
except Exception as e:
    print(f"error: {e}")
    sys.exit(1)

# 保存为 CSV 文件
csv_filename = f"{trend}_data.csv"
data.to_csv(csv_filename)
print(f"Save at {csv_filename}")