import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

def detect_heads(image):
    """Detects and counts heads in an image."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect frontal and profile faces
    faces_frontal = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    faces_profile = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    faces = list(faces_frontal) + list(faces_profile)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image, len(faces)

def process_image():
    """Handles image selection and processing."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        return

    image = cv2.imread(file_path)
    processed_image, head_count = detect_heads(image)

    # Convert processed image to display in Tkinter
    img_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    label_image.config(image=img_tk)
    label_image.image = img_tk
    label_count.config(text=f"Detected Heads: {head_count}")

def process_video():
    """Handles video processing."""
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi")])
    if not file_path:
        return

    cap = cv2.VideoCapture(file_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, head_count = detect_heads(frame)

        cv2.putText(processed_frame, f'Heads: {head_count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Head Count Detection', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def process_webcam():
    """Handles real-time webcam processing."""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, head_count = detect_heads(frame)

        cv2.putText(processed_frame, f'Heads: {head_count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Webcam Head Count Detection', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# GUI Setup
root = tk.Tk()
root.title("Head Count Detection")
root.geometry("600x500")

btn_image = tk.Button(root, text="Process Image", command=process_image, width=20)
btn_image.pack(pady=10)

btn_video = tk.Button(root, text="Process Video", command=process_video, width=20)
btn_video.pack(pady=10)

btn_webcam = tk.Button(root, text="Start Webcam", command=process_webcam, width=20)
btn_webcam.pack(pady=10)

label_count = tk.Label(root, text="Detected Heads: 0", font=("Arial", 14))
label_count.pack(pady=10)

label_image = tk.Label(root)
label_image.pack(pady=10)

root.mainloop()
