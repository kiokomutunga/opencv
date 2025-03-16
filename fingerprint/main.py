import cv2

def open_camera_and_detect_face():
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    #open the default camera
    cap = cv2.VideoCapture(0)

    while True:
       
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('hello Motherfucker??????????????', frame)
        # Close by Pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera_and_detect_face()
