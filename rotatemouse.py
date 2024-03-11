import pyautogui
import math
import time


def move_in_circle(center_x, center_y, radius):
    num_steps = 4
    angle_step = 2 * math.pi / num_steps

    start_x, start_y = pyautogui.position()

    pyautogui.press("ctrl")

    for step in range(num_steps + 1):
        angle = step * angle_step
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))

        pyautogui.moveTo(x, y, duration=0.0001)

    pyautogui.moveTo(start_x, start_y, duration=0.0001)


try:
    while True:
        center_x, center_y = pyautogui.position()
        radius = 10
        duration_between_cycles = 5  # Set the duration between circle movements in second
        move_in_circle(center_x, center_y, radius)
        time.sleep(duration_between_cycles)

except KeyboardInterrupt:
    print("Script stopped by user.")
