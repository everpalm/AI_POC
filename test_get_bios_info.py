import pytest
from get_bios_info import get_bios_info  # 匯入需測試的函數


def test_get_bios_info():
    """
    測試 get_bios_info 函數的正確性。
    在這個測試中，我們將檢查函數是否能正確返回 BIOS 信息。
    """
    # 假設結果（可根據實際情況進行調整）
    expected_result = {"version": "1.0.0", "manufacturer": "Example Corp"}

    # 呼叫 get_bios_info 函數
    result = get_bios_info()

    # 驗證返回的結果與預期結果相符
    assert result == expected_result, f"預期: {expected_result}, 實際: {result}" 


if __name__ == "__main__":
    pytest.main()  # 執行測試