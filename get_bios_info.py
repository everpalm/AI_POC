""" 
這個程式用來獲取電腦的 BIOS 版本資訊。 
使用方法： 
1. 執行程式。 
2. 程式將輸出當前系統的 BIOS 版本。 
"""

import platform
import subprocess


def get_bios_version():
    """ 獲取 BIOS 版本資訊 """
    try:
        # 使用 'wmic' 指令獲取 BIOS 版本資訊 (僅適用於 Windows)
        bios_info = subprocess.check_output("wmic bios get smbiosbiosversion", shell=True)  
        # 解碼並格式化輸出結果
        return bios_info.decode('utf-8').split('\n')[1].strip()
    except Exception as e:
        # 如果發生錯誤，則返回錯誤訊息
        return f"獲取 BIOS 資訊時發生錯誤: {e}"


if __name__ == '__main__':
    # 獲取 BIOS 版本並打印
    bios_version = get_bios_version()
    print(f"當前 BIOS 版本: {bios_version}")