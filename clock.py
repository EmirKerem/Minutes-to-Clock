minutes_passed = int(input())

def clock(minutes_passed):
    hour = (minutes_passed // 60) % 24
    minutes = minutes_passed % 60
    print(f"{hour:02}:{minutes:02}")

clock(minutes_passed)