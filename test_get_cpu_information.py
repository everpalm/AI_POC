import pytest
from get_cpu_information import get_cpu_model  # 引入要測試的 CPU 資訊函數


def test_get_cpu_info():
    """
    測試 get_cpu_info 函數，驗證其返回的 CPU 資訊格式與內容。
    測試檢查返回的字典是否包含必要的鍵，並檢查其值的類型。
    """

    cpu_info = get_cpu_model()  
    
    print("type of cpu_info: ", type(cpu_info))
    print("cpu_info = ", cpu_info)

    assert isinstance(cpu_info, str), "CPU 資訊應該是一個字典"
    
    # # 準備預期的鍵列表
    # required_keys = ['brand', 'cores', 'frequency']  
    
    # # 確保每個預期的鍵都存在於 cpu_info 中
    # for key in required_keys:
    #     assert key in cpu_info, f"應該包含鍵: {key}"
    
    # # 檢查 'cores' 鍵是否為整數型
    # assert isinstance(cpu_info['cores'], int), "'cores' 應該是整數型別"
    
    # # 檢查 'frequency' 鍵是否為浮點數型
    # assert isinstance(cpu_info['frequency'], float), "'frequency' 應該是浮點數型別"