import pytest
from get_cpu_info import get_cpu_info  # 引入待測試的CPU資訊獲取函數


def test_get_cpu_info():
    """
    測試 get_cpu_info 函數以驗證其返回的 CPU 資訊是否正確。
    包含對返回資料格式及內容的檢查。
    """
    # 調用 get_cpu_info 函數以獲取 CPU 信息
    cpu_info = get_cpu_info()  
    
    # 驗證 cpu_info 是否為字典格式
    assert isinstance(cpu_info, dict), "CPU 資訊應該是一個字典"
    
    # 定義我們期望的鍵
    expected_keys = ['brand', 'cores', 'frequency']  
    
    # 確認這些鍵都存在於返回的 cpu_info 中
    for key in expected_keys:
        assert key in cpu_info, f"應該存在鍵: {key}"
    
    # 檢查 'cores' 鍵值是否為整數
    assert isinstance(cpu_info['cores'], int), "'cores' 應該是整數型別"
    
    # 檢查 'frequency' 鍵值是否為浮點數
    assert isinstance(cpu_info['frequency'], float), "'frequency' 應該是浮點數型別"