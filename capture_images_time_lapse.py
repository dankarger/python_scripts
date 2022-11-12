import os
from datetime import datetime
import time
for i in range(10):
    now = datetime.now()
    file_name = now.strftime("%d_%m_%y--%H:%M:%S")
    os.system(f"fswebcam -r 1280x720 --no-banner /home/dandan/images/{file_name}.jpg")
    time.sleep(500/1000)