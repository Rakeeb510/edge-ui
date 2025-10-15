# EdgeVision Studio

EdgeVision Studio is an interactive web app built with **Streamlit** that visualizes image edges using Sobel, Laplacian, and Canny edge detection algorithms.  
You can upload an image or capture one through your webcam, adjust parameters in real time, compare algorithms, and download results easily.

---

Features
- Upload or capture image through webcam  
- Choose between **Sobel**, **Laplacian**, and **Canny**  
- Adjustable parameters for each algorithm  
- Reset and compare outputs side-by-side  
- Download processed image  
- Clean, modern, and responsive UI  

---

Technologies Used
- Python 3.13
- Streamlit
- OpenCV
- NumPy
- Pillow

---

Installation & Run
1. Clone or extract the project folder  
2. Open a terminal in the folder  
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
4. Install required packages:
   pip install -r requirements.txt
5. Run the app:
   streamlit run app.py
6. Open the local URL shown (usually http://localhost:8501)