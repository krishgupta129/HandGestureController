# HandGestureController

A webcam-based hand gesture controller that lets you control **Minion Rush** using natural hand movements. Built with Python, OpenCV, MediaPipe, and PyAutoGUI, it translates detected hand poses into keyboard inputs in real time.

## Overview

HandGestureController uses a webcam to track one hand and interpret gestures as game controls. The camera feed is mirrored for an intuitive preview, hand landmarks are drawn on the frame, and an on-screen guide shows control zones and the currently detected gesture.

The project is organized into separate modules so tracking, gesture recognition, and keyboard control can be maintained independently.

## Features

- **Hand tracking:** Detects hand landmarks in a live webcam feed.
- **Jump:** Raise the index and middle fingers while keeping the ring finger and pinky folded.
- **Slide:** Make a fist.
- **Turn left / right:** Move an open hand toward the left or right side of the camera frame.
- **Tilt left / right:** Rotate the open palm beyond the configured tilt threshold. The controller holds `A` or `D` while the corresponding tilt gesture is detected.
- **Live visual feedback:** Displays the camera feed, hand landmarks, gesture label, and visual guide zones.
- **Input cooldown:** Adds a short cooldown to discrete actions to reduce repeated key presses.
- **Keyboard-based control:** Uses PyAutoGUI to send key presses to the active application.

> **Note:** The controls described here reflect the current source code. The application window is titled **Minion Rush Controller** and the overlay labels the jump and slide gestures.

## Gesture Controls

| Hand gesture / movement | Detected action | Input sent |
|---|---|---|
| Index and middle fingers open, ring finger and pinky folded | Jump | `Up Arrow` |
| All four tracked fingers folded (fist) | Slide | `Down Arrow` |
| Open hand moved left of the center zone | Turn left | `Left Arrow` |
| Open hand moved right of the center zone | Turn right | `Right Arrow` |
| Open palm tilted left | Tilt left continuously | Hold `A` |
| Open palm tilted right | Tilt right continuously | Hold `D` |
| Hand not detected | No hand | Releases any held tilt key |

The gesture detector estimates finger openness using MediaPipe landmarks. Left/right turning is based on wrist position relative to the center threshold, while tilt is based on the angle between the wrist and the middle-finger base.

## Project Structure

```text
HandGestureController/
├── main.py                 # Webcam loop and on-screen guide
├── hand_tracker.py         # MediaPipe hand landmark tracking
├── gesture_detector.py    # Maps landmarks to named gestures
├── controller.py           # Sends keyboard inputs using PyAutoGUI
├── requirements.txt        # Python package dependencies
├── README.md               # Project documentation
└── .gitignore              # Recommended Git exclusions
```

## Requirements

- Python version compatible with the pinned MediaPipe and NumPy releases in `requirements.txt`.
- A working webcam.
- The game/application you want to control open and focused before using gestures.

The project is designed around desktop webcam input and keyboard simulation. Camera access and synthetic keyboard input can vary by operating system; Windows is a sensible starting point, but every platform has not been verified.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/HandGestureController.git
   cd HandGestureController
   ```

2. (Recommended) Create and activate a virtual environment.

   **Windows PowerShell**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Windows Command Prompt**
   ```bat
   python -m venv .venv
   .\.venv\Scripts\activate.bat
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the controller:

   ```bash
   python main.py
   ```

## How to Use

1. Connect your webcam and make sure no other application is exclusively using it.
2. Start the controller with `python main.py`.
3. Keep one hand visible in the camera frame.
4. Open the game/application you want to control and make sure it is the active window.
5. Use the gestures listed above. The camera preview shows the detected gesture.
6. Press **Q** while the preview window is active to exit.

The controller sends inputs to the currently active application. If the game does not respond, click its window to focus it, then try again.

## Configuration

Gesture thresholds are defined in `gesture_detector.py`:

- `center_x`: Horizontal center reference for turning.
- `turn_threshold`: Distance from the center required to trigger a left/right turn.
- `tilt_threshold`: Palm-angle threshold in degrees for tilt gestures.

The discrete-action cooldown is defined in `controller.py`:

- `cooldown`: Minimum interval between accepted discrete actions, in seconds.

Adjust these values carefully and test in good lighting with your hand fully visible.

## Dependencies

The source code imports:

- **OpenCV** (`cv2`) for webcam capture, image processing, drawing, and display.
- **MediaPipe** for hand landmark tracking.
- **PyAutoGUI** for keyboard key presses and holds.

The uploaded `requirements.txt` pins package versions. Install from that file to reproduce the listed environment. If installation fails, check your Python version and the compatibility of the pinned packages before changing dependency versions.

## Troubleshooting

- **Camera does not open:** Close other webcam apps, check operating-system camera permissions, and confirm that the expected camera index is available.
- **No hand landmarks:** Improve lighting, keep the whole hand in frame, and try a less busy background.
- **Game ignores controls:** Make sure the target game is the active window. Some applications may restrict synthetic keyboard input.
- **Gestures trigger too often:** Adjust `turn_threshold`, `tilt_threshold`, or `cooldown` in the relevant modules.
- **Dependency installation fails:** Check Python and package compatibility with the pinned versions in `requirements.txt`.

## Limitations

- The tracker detects a maximum of one hand.
- Gesture recognition relies on landmark positions and fixed thresholds, so lighting, camera angle, and hand orientation can affect accuracy.
- The controller sends keyboard inputs to the active application; it does not directly integrate with the game's internal systems.
- The project currently has no graphical settings panel or automatic calibration.

## Future Improvements

- Add gesture calibration and sensitivity settings.
- Add selectable keyboard mappings.
- Improve recognition across different hand orientations.
- Add configurable camera selection and clearer camera-error messages.
- Include a demo video or screenshots in the repository.
- Add automated tests for gesture classification and controller behavior.

## License

No license was included in the supplied files. Add a `LICENSE` file before presenting the repository as open source. The MIT License is one common permissive option if it matches your intentions.

## Author

**Krish Gupta**

---

If you use or adapt this project, please credit the repository once it is published.
