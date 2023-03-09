import time

for i in range(10):
    print(f"\r离程序退出还剩{9-i}秒", end="")
    time.sleep(1)