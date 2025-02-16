# 🧑‍🤝‍🧑 Head Count Detection using OpenCV & Tkinter

## 📌 Overview
This project detects and counts heads in images, videos, and real-time webcam streams using **OpenCV's Haar Cascade Classifiers**.

## 🛠 Features
✔️ **Image Processing** – Detect heads in uploaded images  
✔️ **Video Processing** – Analyze pre-recorded videos  
✔️ **Real-Time Webcam Detection** – Detect heads live using your webcam  
✔️ **Tkinter GUI** – Easy-to-use interface  

## 📂 Project Structure
📁 Head Count Detection ├── head_count.py # Main Python script ├── haarcascade_frontalface_default.xml # Face detection model ├── haarcascade_profileface.xml # Profile face detection model ├── README.md # Documentation ├── requirements.txt # Dependencies

bash
Copy
Edit

## 🚀 Installation & Usage
1️⃣ **Clone the repository**  
   ```sh
   git clone https://github.com/your-username/head-count-detection.git
   cd head-count-detection
2️⃣ Install dependencies

sh
Copy
Edit
pip install opencv-python numpy pillow
3️⃣ Run the script

sh
Copy
Edit
python head_count.py
🎯 How It Works
Image Mode: Upload an image, and the model will detect and count heads.
Video Mode: Upload a video file, and it will process each frame.
Webcam Mode: Runs real-time detection from the webcam feed.
🏗 Future Improvements
🔹 Improve accuracy with deep learning models (YOLO, SSD, or CNNs)
🔹 Add crowd density analysis
🔹 Enhance GUI with interactive features

📜 License
This project is open-source and contributions are welcome! 🚀
