import time

class SignalGenerator:
    def __init__(self):
        self.start_time = None
        # self.duration = 0
    
    def start(self):
        """开始计时并设置持续时间"""
        self.start_time = time.time()  # 记录当前时间
        # self.duration = duration  # 设置信号持续时间
    
    def get_value(self):
        """根据当前时间和已设定的持续时间返回信号值"""
        if self.start_time is None:
            self.start()
            return float()
            # raise ValueError("SignalGenerator not started yet")
        # 当前时间减去开始时间，计算已经过去的时间
        elapsed_time = time.time() - self.start_time
        return elapsed_time