import cv2
from hand_tracker import HandTracker
from gesture_detector import GestureDetector
from controller import GameController


def draw_ui(frame, gesture):
    h, w, _ = frame.shape

    # Left zone
    cv2.rectangle(frame, (0, 100), (int(w * 0.35), h - 100), (255, 0, 0), 2)
    cv2.putText(frame, "LEFT", (30, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Right zone
    cv2.rectangle(frame, (int(w * 0.65), 100), (w, h - 100), (0, 0, 255), 2)
    cv2.putText(frame, "RIGHT", (w - 170, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Jump box
    cv2.rectangle(frame, (int(w * 0.3), 0), (int(w * 0.7), 100), (0, 255, 0), 2)
    cv2.putText(frame, "JUMP = 2 Fingers", (int(w * 0.32), 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Move
    cv2.putText(frame, "MOVE", (int(w * 0.42), int(h * 0.5)),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Slide
    cv2.putText(frame, "FIST = SLIDE", (int(w * 0.35), h - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.putText(frame, f"Gesture: {gesture}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open nahi hua")
        return

    tracker = HandTracker()
    detector = GestureDetector()
    controller = GameController()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)

        frame, landmarks = tracker.detect(frame)
        gesture = detector.detect_gesture(landmarks)

        controller.execute(gesture)
        draw_ui(frame, gesture)

        cv2.imshow("Minion Rush Controller", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    controller.cleanup()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
