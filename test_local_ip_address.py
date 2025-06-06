import pytest
from local_ip_address import get_local_ip  # 假設這是要測試的函數


def test_get_local_ip():
    """
    測試 get_local_ip 函數是否可以正確獲取本地 IP 地址。
    """
    # 假設這裡我們需要的測試環境，以模擬返回的本地 IP 地址
    expected_ip = '192.168.1.1'  # 這是一個示例的預期 IP 地址

    # 調用 get_local_ip 函數並獲取結果
    result = get_local_ip()

    # 斷言結果是否符合預期
    assert result == expected_ip, f'預期 IP 為 {expected_ip}，但得到 {result}'


def test_get_local_ip_empty():
    """
    測試 get_local_ip 函數在沒有可用 IP 地址時的行為。
    """
    # 當沒有可用的 IP 地址時，假設函數會返回 None
    result = get_local_ip()

    # 驗證返回值應該是 None
    assert result is None, '當沒有可用 IP 地址時，結果應為 None'


if __name__ == '__main__':
    pytest.main()  # 直接執行測試