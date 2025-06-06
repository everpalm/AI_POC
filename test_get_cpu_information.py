import pytest
from get_cpu_information import get_cpu_info # 假設要測試的函數在此導入


def test_get_cpu_info():
    """
    測試獲取 CPU 資訊的功能。
    
    使用 pytest 框架來測試 get_cpu_info 函數是否能正常返回 CPU 的詳細資訊。
    """
    # 調用函數以獲取 CPU 資訊
    cpu_info = get_cpu_info()
    
    # 檢查返回的資料型別
    assert isinstance(cpu_info, dict), "返回值應為字典型別"
    
    # 檢查字典中是否包含必要的 CPU 資訊
    assert "cpu_count" in cpu_info, "應包含 CPU 數量"
    assert "cpu_frequency" in cpu_info, "應包含 CPU 頻率"
    assert "cpu_load" in cpu_info, "應包含 CPU 負載"
    
    # 檢查 CPU 數量是否為正整數
    assert cpu_info["cpu_count"] > 0, "CPU 數量應大於零"
    
    # 除此之外還可以添加更多的測試條件