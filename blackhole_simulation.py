# 1導入 QuTiP 來模擬量子糾纏
from qutip import *
import numpy as np

# 初始化“一個”量子糾纏態：(2,x)的2表示2個糾纏的數據，即(x,0)⊗(x,1)的0,1表示耦合成對性（即設定為a數據為1則b數據為0，反之亦然）
bell_state = (tensor(basis(2,0), basis(2,1)) + tensor(basis(2,1), basis(2,0))).unit()

# 列印以確認（measure）量子態
print("Initial Bell state:")
print(bell_state)


def simulate_data_loss(distance, noise_level, packet_size, environment_factor=1.0, congestion_factor=1.0):
    """
    模擬數據丟失率，考慮距離、雜訊（物理層影響：如有線通訊的纜線材質、電阻、emp干擾、電壓穩定度等）和封包大小的影響。
    """
    print(f"Simulating data loss for distance: {distance}, packet size: {packet_size}")
    
    # 假設距離影響較小
    distance_loss = np.exp(-distance / (noise_level * 10))
    
    # 假設封包大小影響較小
    packet_loss = 1 - np.exp(-packet_size / 5000)
    
    # 環境因素影響
    environment_loss = environment_factor
    
    # 網路擁塞影響
    congestion_loss = congestion_factor
    
    # 總丟失率考慮了所有因素的影響
    total_loss = distance_loss * packet_loss * environment_loss * congestion_loss
    return total_loss

# 情境1：封包越小，丟失率越高
def simulate_data_loss_small_packet(distance, noise_level, packet_size, environment_factor=1.0, congestion_factor=1.0):
    packet_loss = np.exp(-packet_size / 5000)
    # 其他部分與原函數相同
    # ...

# 情境2：距離越短，丟失率越高
def simulate_data_loss_short_distance(distance, noise_level, packet_size, environment_factor=1.0, congestion_factor=1.0):
    distance_loss = 1 - np.exp(-1 / (distance + 1))
    # 其他部分與原函數相同
    # ...

# 情境3：封包越小且距離越短，丟失率越高
def simulate_data_loss_small_packet_short_distance(distance, noise_level, packet_size, environment_factor=1.0, congestion_factor=1.0):
    packet_loss = np.exp(-packet_size / 5000)
    distance_loss = 1 - np.exp(-1 / (distance + 1))
    # 其他部分與原函數相同
    # ...

# 情境4：封包越大且距離越長，丟失率越高（原假設）
def simulate_data_loss_large_packet_long_distance(distance, noise_level, packet_size, environment_factor=1.0, congestion_factor=1.0):
    # 這個情境與原函數相同
    return simulate_data_loss(distance, noise_level, packet_size, environment_factor, congestion_factor)

# 模擬不同距離和封包大小的數據丟失
print("Starting data loss simulation...")
distances = np.linspace(0, 100, 50)
packet_sizes = np.linspace(100, 1000, 5)  # 不同大小的封包

# 繪製不同 packet_size 下的數據丟失曲線
import matplotlib.pyplot as plt
for packet_size in packet_sizes:
    print(f"Simulating for packet size: {packet_size}")
    losses = [simulate_data_loss(d, 10, packet_size) for d in distances]
    plt.plot(distances, losses, label=f'Packet Size: {packet_size} bytes')

# 圖像配置
print("Plotting results...")
plt.xlabel('Distance')
plt.ylabel('Data Loss')
plt.title('Data Loss vs Distance for Different Packet Sizes')
plt.legend()
plt.show()



