import subprocess


def get_window_id(pid: int):
    result = subprocess.run(['wmctrl', '-lp'], stdout=subprocess.PIPE)
    windows = result.stdout.decode().splitlines()
    window_ids = []

    # print(result)
    for window in windows:
        window_pid = window.split()[2]
        if window_pid == str(pid):
            return int(window.split()[0], 16)  # 第一个字段是窗口 ID
    return None

if __name__ == '__main__':
    window_ids = get_window_id(390540)
    print(window_ids, type(window_ids))
