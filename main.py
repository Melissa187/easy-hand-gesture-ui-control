import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
hands = mp_hands.Hands()
face_mesh = mp_face.FaceMesh(refine_landmarks=True)
mp_draw = mp.solutions.drawing_utils

# Webcam input
cap = cv2.VideoCapture(0)
mode = "gesture"
blink_counter = 0

# Gesture mapping
def get_gesture_action(lm_list):
    if len(lm_list) != 21:
        return "none", []

    fingers = []

    # Thumb
    fingers.append(1 if lm_list[4][0] > lm_list[3][0] else 0)

    # Fingers (index to pinky)
    for id in [8, 12, 16, 20]:
        fingers.append(1 if lm_list[id][1] < lm_list[id - 2][1] else 0)

    # Check actions
    if fingers == [1, 0, 0, 0, 0]:
        return "volume_up", fingers
    elif fingers == [0, 1, 1, 0, 0]:
        return "volume_down", fingers
    elif fingers == [1, 1, 1, 0, 0]:
        return "zoom_out", fingers
    elif fingers == [0, 1, 0, 0, 0]:
        return "zoom_in", fingers
    else:
        return "none", fingers

# Blink detection
def detect_blink(face_landmarks):
    left_eye_top = face_landmarks[159]
    left_eye_bottom = face_landmarks[145]
    vertical_distance = abs(left_eye_top.y - left_eye_bottom.y)
    return vertical_distance < 0.015

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results_hands = hands.process(img_rgb)
    results_face = face_mesh.process(img_rgb)

    lm_list = []
    detected_fingers = []

    # Hand landmarks
    if results_hands.multi_hand_landmarks:
        for hand_landmarks in results_hands.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = img.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Face landmarks for blink
    if results_face.multi_face_landmarks:
        for face_landmarks in results_face.multi_face_landmarks:
            if detect_blink(face_landmarks.landmark):
                blink_counter += 1
                if blink_counter > 2:
                    mode = "audio" if mode == "gesture" else "gesture"
                    blink_counter = 0
            else:
                blink_counter = 0

    action, detected_fingers = get_gesture_action(lm_list) if mode == "gesture" else ("none", [])

    # Perform action
    if action == "volume_up":
        pyautogui.press("volumeup")
    elif action == "volume_down":
        pyautogui.press("volumedown")
    elif action == "zoom_in":
        pyautogui.hotkey("ctrl", "+")
    elif action == "zoom_out":
        pyautogui.hotkey("ctrl", "-")

    # Display mode, action, finger pattern
    cv2.putText(img, f"Mode: {mode}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, f"Action: {action}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(img, f"Fingers: {detected_fingers}", (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 200, 100), 2)

    cv2.imshow("Easy Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()







