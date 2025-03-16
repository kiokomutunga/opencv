import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim

def detect_fingerprint_similarity(image1_path, image2_path, threshold=0.7):
    # Load images
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize images to same size
    image1 = cv2.resize(image1, (300, 300))
    image2 = cv2.resize(image2, (300, 300))
    
    # Compare similarity
    (score, diff) = compare_ssim(image1, image2, full=True)
    print(f"Similarity Score: {score}")
    
    return score >= threshold

def open_camera_and_authenticate():
    cap = cv2.VideoCapture(0)
    authentic_fingerprint_path = 'authentic_fingerprint.jpg' # path to the saved authentic fingerprint image
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Fingerprint Authentication', gray_frame)
        
        # Simulate fingerprint capture (press 'c' to capture)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            captured_fingerprint_path = 'captured_fingerprint.jpg'
            cv2.imwrite(captured_fingerprint_path, gray_frame)
            
            if detect_fingerprint_similarity(authentic_fingerprint_path, captured_fingerprint_path):
                print("Authentication Successful!")
                break
            else:
                print("Authentication Failed. Please try again.")
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera_and_authenticate()
