import math
import time

class SignalGenerator:
    def __init__(self):
        self.start_time = None

    def start(self):
        """开始计时并设置持续时间"""
        self.start_time = time.time()  # 记录当前时间
    
    def get_elapsed_time(self):
        """根据当前时间和已设定的持续时间返回信号值"""
        if self.start_time is None:
            self.start()
            return float()
        elapsed_time = time.time() - self.start_time
        return elapsed_time
    def get_value(self):
        return self.get_elapsed_time()

class SinGenerator(SignalGenerator):
    def __init__(self, amplitude, frequency):
        super().__init__()
        self.amplitude = amplitude
        self.frequency = frequency
    def get_value(self):
        elapsed_time = super().get_elapsed_time()
        return self.amplitude * math.sin(2 * math.pi * self.frequency * elapsed_time)

custom_globals = {
    'SignalGenerator': SignalGenerator,
    'SinGenerator': SinGenerator
}