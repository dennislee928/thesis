# 1導入 QuTiP 來模擬量子糾纏
from qutip import *
import numpy as np

# 初始化“一個”量子糾纏態：(2,x)的2表示2個糾纏的數據，即(x,0)⊗(x,1)的0,1表示耦合成對性（即設定為a數據為1則b數據為0，反之亦然）
bell_state = (tensor(basis(2,0), basis(2,1)) + tensor(basis(2,1), basis(2,0))).unit()

# 列印以確認（measure）量子態
print(bell_state)
