from multiprocessing import connection
import time
import sqlite3

start_time=time.time()
end_time=start_time
lap_num=1

print("Click on ENTER to count laps.\nPress CTRL+C to stop")

try:
    while True:

        input()
        time_laps=round((time.time() - end_time), 2)

        total_time=round((time.time() - start_time), 2)

        print("Lap No. "+str(lap_num))
        print("Total Time: "+str(total_time))
        print("Lap Time: "+str(time_laps))

        print("*"*20)

        end_time=time.time()
        lap_num+=1

except KeyboardInterrupt:
    print("Exit!")
