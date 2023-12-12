# figuring out how to exit the loop after 5 minutes and how to check every 5 seconds without using sleep
import time

starting_time_time = time.time()
print(starting_time_time)
# time.sleep(2)
# print(round((starting_time_time - time.time()) % 2))

timeout = starting_time_time + 10
while True:
    print(round(time.time() - starting_time_time))
    if (round(time.time() - starting_time_time) % 5) == 0:
        print("5 second interval")
    if time.time() < timeout:
        print(time.time())
    else:
        break
