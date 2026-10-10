import math


class GestureDetector:
    def __init__(self):
        self.center_x = 0.5
        self.turn_threshold = 0.22
        self.tilt_threshold = 12

    def detect_gesture(self, landmarks):
        if landmarks is None:
            return "NO HAND"

        index_open = landmarks[8].y < landmarks[6].y
        middle_open = landmarks[12].y < landmarks[10].y
        ring_open = landmarks[16].y < landmarks[14].y
        pinky_open = landmarks[20].y < landmarks[18].y

        fingers_open = sum([
            index_open,
            middle_open,
            ring_open,
            pinky_open
        ])

        # Fist = Slide
        if fingers_open == 0:
            return "SLIDE"

        # Two fingers = Jump
        if (
            index_open
            and middle_open
            and not ring_open
            and not pinky_open
        ):
            return "JUMP"

        # Open palm controls movement
        if fingers_open >= 3:
            wrist = landmarks[0]
            middle_mcp = landmarks[9]

            dx = middle_mcp.x - wrist.x
            dy = wrist.y - middle_mcp.y

            angle = math.degrees(math.atan2(dx, dy))

            # Hand moved far left = turn left
            if wrist.x < self.center_x - self.turn_threshold:
                return "LEFT"

            # Hand moved far right = turn right
            if wrist.x > self.center_x + self.turn_threshold:
                return "RIGHT"

            # Palm angle = tilt
            if angle < -self.tilt_threshold:
                return "TILT_LEFT"

            if angle > self.tilt_threshold:
                return "TILT_RIGHT"

            return "CENTER"

        return "CENTER"
