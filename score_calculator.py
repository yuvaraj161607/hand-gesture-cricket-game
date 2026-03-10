import cv2
import mediapipe as mp

gestures = {
    1: [(0,1,0,0,0),(0,0,1,0,0),(0,0,0,0,1)],
    2: [(0,1,1,0,0),(0,0,1,1,0),(0,0,0,1,1)],
    3: [(0,1,1,1,0),(0,0,1,1,1),(0,1,0,1,1)],
    4: [(0,1,1,1,1)],
    5: [(1,1,1,1,1)],
    6: [(1,0,0,0,0)],
    7: [(1,1,0,0,0)],
    8: [(1,1,1,0,0)],
    9: [(1,1,1,1,0)],
    10: [(0,1,0,0,1)],
}

mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = None

def open_camera():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)

def close_camera():
    global cap
    if cap is not None:
        cap.release()
        cv2.destroyAllWindows()
        cap = None

def detect_gesture(landmarks):
    lm = landmarks.landmark
    thumb  = 1 if lm[4].x  < lm[3].x  else 0
    index  = 1 if lm[8].y  < lm[6].y  else 0
    middle = 1 if lm[12].y < lm[10].y else 0
    ring   = 1 if lm[16].y < lm[14].y else 0
    pinky  = 1 if lm[20].y < lm[18].y else 0
    pattern = (thumb, index, middle, ring, pinky)
    for gesture, patterns in gestures.items():
        if pattern in patterns:
            return gesture
    return None

def get_player_gesture(score=0, balls=0, target=None, label="Your Turn"):
    open_camera() 
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        frame = cv2.resize(frame, (640, 480))
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands_detector.process(rgb)

        detected_gesture = None

        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                detected_gesture = detect_gesture(hand)
                if detected_gesture:
                    break

        cv2.rectangle(frame, (0, 0), (640, 90), (0, 0, 0), -1)
        cv2.putText(frame, f"Score: {score}", (15, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.putText(frame, f"Balls: {balls}", (200, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
        if target is not None:
            cv2.putText(frame, f"Target: {target}", (370, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 165, 255), 2)
        cv2.putText(frame, label, (15, 75),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        if detected_gesture:
            cv2.putText(frame, str(detected_gesture), (280, 300),
                        cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 100), 8)
            cv2.putText(frame, "SPACE = confirm", (180, 440),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
        else:
            cv2.putText(frame, "Show 1-10 fingers", (150, 300),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)

        cv2.imshow("Cricket Game", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 32 and detected_gesture:
            return detected_gesture
        if key == ord('q'):
            close_camera()
            return None


