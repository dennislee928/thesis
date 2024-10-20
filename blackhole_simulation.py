# 1導入 QuTiP 來模擬量子糾纏
from qutip import *
import numpy as np

# 初始化“一個”量子糾纏態：(2,x)的2表示2個糾纏的數據，即(x,0)⊗(x,1)的0,1表示耦合成對性（即設定為a數據為1則b數據為0，反之亦然）
bell_state = (tensor(basis(2,0), basis(2,1)) + tensor(basis(2,1), basis(2,0))).unit()

# 列印以確認（measure）量子態
print(bell_state)


def simulate_data_loss(distance, noise_level, packet_size):
    """
    模擬數據丟失率，考慮距離、noise和封包大小的影響。
    """
    # 距離越遠，丟失率越高，且封包越大，數據丟失的風險越大
    distance_loss = np.exp(-distance / noise_level)
    
    # 假設封包越大，丟失率越高
    # 這裡 packet_loss 是根據 packet_size 的對數函數調整
    packet_loss = 1 - np.exp(-packet_size / 1000)  # 比例基於數據包大小
    
    # 總丟失率考慮了距離和封包大小的影響
    total_loss = distance_loss * packet_loss
    return total_loss

# 模擬不同距離和數據包大小的數據丟失
distances = np.linspace(0, 100, 50)
packet_sizes = np.linspace(100, 1000, 5)  # 不同大小的封包

# 繪製不同 packet_size 下的數據丟失曲線
import matplotlib.pyplot as plt
for packet_size in packet_sizes:
    losses = [simulate_data_loss(d, 10, packet_size) for d in distances]
    plt.plot(distances, losses, label=f'Packet Size: {packet_size} bytes')

# 圖像配置
plt.xlabel('Distance')
plt.ylabel('Data Loss')
plt.title('Data Loss vs Distance for Different Packet Sizes')
plt.legend()
plt.show()


