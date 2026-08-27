#!/usr/bin/env python3
import cv2
import datetime

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Tidak dapat membuka webcam")
        return

    # Removed forced 1920x1080 resolution to let the camera use its default/natural size
    
    print("Aplikasi dimulai. Gunakan jendela tampilan untuk berinteraksi.")
    
    # State
    mode = "LIVE"
    brightness = 0 # Default brightness offset

    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Apply brightness adjustment
        # Convert to float to avoid overflow
        adjusted_frame = cv2.convertScaleAbs(frame, alpha=1.0, beta=brightness)
        
        # Draw Menu Overlay
        display_frame = adjusted_frame.copy()
        cv2.putText(display_frame, "Menu: [1] Live, [2] Foto, [+] Terang, [-] Gelap, [q] Keluar", (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(display_frame, f"Mode: {mode} | Brightness: {brightness}", (20, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

        cv2.imshow('dx19-cam', display_frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('1'):
            mode = "LIVE"
        elif key == ord('2'):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"webcam_photo_{timestamp}.jpg"
            cv2.imwrite(filename, adjusted_frame)
            mode = "PHOTO_SAVED"
            cv2.waitKey(1000) 
            mode = "LIVE"
        elif key == ord('+'):
            brightness = min(brightness + 10, 100)
        elif key == ord('-'):
            brightness = max(brightness - 10, -100)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
