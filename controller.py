import pyautogui
import time


class GameController:
    def __init__(self):
        self.last_action = 0
        self.cooldown = 0.35

        self.last_gesture = None
        self.held_tilt_key = None

    def release_tilt(self):
        if self.held_tilt_key is not None:
            pyautogui.keyUp(self.held_tilt_key)
            self.held_tilt_key = None

    def hold_tilt(self, key):
        if self.held_tilt_key == key:
            return

        self.release_tilt()

        pyautogui.keyDown(key)
        self.held_tilt_key = key

    def execute(self, gesture):
        current = time.time()

        # Continuous tilt left
        if gesture == "TILT_LEFT":
            self.hold_tilt("a")
            self.last_gesture = gesture
            return

        # Continuous tilt right
        if gesture == "TILT_RIGHT":
            self.hold_tilt("d")
            self.last_gesture = gesture
            return

        # Any other gesture stops tilt
        self.release_tilt()

        # No hand
        if gesture == "NO HAND":
            self.last_gesture = None
            return

        # Center hand
        if gesture == "CENTER":
            self.last_gesture = None
            return

        # Prevent same gesture repeating
        if gesture == self.last_gesture:
            return

        # Cooldown
        if current - self.last_action < self.cooldown:
            return

        if gesture == "JUMP":
            print("JUMP")
            pyautogui.press("up")
            self.last_action = current

        elif gesture == "SLIDE":
            print("SLIDE")
            pyautogui.press("down")
            self.last_action = current

        elif gesture == "LEFT":
            print("TURN LEFT")
            pyautogui.press("left")
            self.last_action = current

        elif gesture == "RIGHT":
            print("TURN RIGHT")
            pyautogui.press("right")
            self.last_action = current

        self.last_gesture = gesture

    def cleanup(self):
        self.release_tilt()
