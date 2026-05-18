import pyautogui
import time
import os


def get_coords():
    print("=== Subway Surfers Coordinate Helper ===")
    print("Hover your mouse over the target area. Press Ctrl+C to stop.\n")

    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()

            print(f"x: {x} y: {y}")

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n\nStopped.")


if __name__ == "__main__":
    get_coords()