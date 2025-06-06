import pytest
from get_cpu_info import get_cpu_info  # 假設有一個方法可以獲取 CPU 資訊


def test_get_cpu_info():
    """
    測試 get_cpu_info 函數以確保它返回正確的 CPU 資訊。
    
    使用 pytest 框架，執行此測試時應確保 get_cpu_info 返回的
    訊息符合預期格式。
    """

    # 呼叫 get_cpu_info 函數以獲取 CPU 資訊
    cpu_info = get_cpu_info()
    
    # 驗證 cpu_info 是否包含預期的鍵和值
    assert isinstance(cpu_info, dict), "CPU info should be a dictionary"
    assert "cores" in cpu_info, "CPU info should have a 'cores' key"
    assert "model" in cpu_info, "CPU info should have a 'model' key"
    
    # 驗證核心數量是否為正整數
    assert isinstance(cpu_info["cores"], int), "'cores' should be an integer"
    assert cpu_info["cores"] > 0, "'cores' should be greater than 0"
    
    # 驗證 CPU 型號的類型
    assert isinstance(cpu_info["model"], str), "'model' should be a string"
    assert len(cpu_info["model"]) > 0, "'model' should not be empty"