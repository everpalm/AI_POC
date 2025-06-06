import pytest
from get_bios_info import get_bios_info  # 匯入需測試的函數


def test_get_bios_info():
    """
    測試 get_bios_info 函數的正確性。
    確保這個單元測試能檢查函數是否正確返回 BIOS 信息。
    """
    # 假設的預期結果，應根據實際的 get_bios_info 函數輸出進行修改
    expected_result = {"version": "1.0.0", "manufacturer": "Example Corp"}

    # 呼叫 get_bios_info 函數以獲取當前 BIOS 信息
    result = get_bios_info()

    # 驗證結果是否與預期相符
    assert result == expected_result, f"預期: {expected_result}, 實際: {result}" 


if __name__ == "__main__":
    pytest.main()  # 如果這個檔案被直接運行，則執行 pytest.main()