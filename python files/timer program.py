import time
seconds = 15
for j in range(seconds, 0, -1):
    print(f"Time left: {j} seconds", end="\r")
    time.sleep(1)
print("\n time's up.")