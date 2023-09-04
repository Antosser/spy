import os
import datetime
from mss import mss
from PIL import Image
from pynput.mouse import Listener

image_radius = 400
image_quality = 20 # 0 - 100
directory_name = 'spy'

# Path to the user directory
user_directory = os.path.expanduser('~')

# Listener callback function
def on_click(x, y, button, pressed):

    if pressed:
        with mss() as sct:
            monitor = {'top': y-image_radius, 'left': x-image_radius, 'width': image_radius * 2, 'height': image_radius * 2}
            sct_img = sct.grab(monitor)

            # Get current time and date
            now = datetime.datetime.now()
            date_str = now.strftime('%Y-%m-%d')
            time_str = now.strftime('%H-%M-%S-%f')

            # Create spy directory if not exist
            spy_directory_path = os.path.join(user_directory, directory_name, date_str)
            os.makedirs(spy_directory_path, exist_ok=True)

            # Save the screenshot
            img_path = os.path.join(spy_directory_path, f'{time_str}.jpg')
            Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX').save(img_path, quality = image_quality)

if __name__ == '__main__':
    # Collect events until released
    with Listener(on_click=on_click) as listener:
        listener.join()