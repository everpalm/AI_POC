import platform


def get_cpu_model():
    """
    获取当前系统的 CPU 模型名称。
    
    返回: str: CPU 模型名称。
    """
    # 使用 platform 模块获取 CPU 信息
    cpu_model = platform.processor()
    return cpu_model


if __name__ == '__main__':
    # 仅在直接运行脚本时获取并打印 CPU 模型
    print(get_cpu_model())
