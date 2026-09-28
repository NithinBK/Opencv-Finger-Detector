import cv2
from cvzone.HandTrackingModule import HandDetector

def main():
    """
    Detects and labels each finger of a single hand from a webcam feed.
    """
    # Initialize the HandDetector
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    # Start video capture from the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    # Set the desired resolution (e.g., 1280x720)
    # This might fail if the camera does not support the requested resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # List of finger names and their landmark indices
    finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
    tip_indices = [4, 8, 12, 16, 20]

    while True:
        # Read a frame from the webcam
        success, img = cap.read()
        if not success:
            break

        # Find hands in the current frame.
        hands, img = detector.findHands(img, draw=True)

        # Process the single detected hand
        if hands:
            hand = hands[0]
            lmList = hand['lmList']
            
            if lmList:
                for i, finger_index in enumerate(tip_indices):
                    x, y, z = lmList[finger_index]

                    # Draw a filled circle and display the finger name
                    cv2.circle(img, (x, y), 10, (255, 0, 255), cv2.FILLED)
                    cv2.putText(img, finger_names[i], (x + 20, y), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display the processed image
        cv2.imshow("Single Hand Finger Detector", img)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()