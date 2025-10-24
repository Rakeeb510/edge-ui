# 📸 Edge Detector: Interactive Edge Detection UI (CS-4218 A1)

## Project Description
[cite_start]This is an interactive, web-based application developed using **Python** and **Streamlit** for visual experimentation with classical edge detection algorithms[cite: 6, 39]. [cite_start]The interface enables users to upload an image and dynamically adjust algorithm-specific parameters (Sobel, Laplacian, and Canny) to immediately observe their effects on the output image in real-time[cite: 31].

[cite_start]This project was assigned as A1 for the course CS-4218 Introduction to Computer Vision[cite: 2, 3].

***

## Setup and Installation Instructions

1.  **Prerequisites:** Ensure you have **Python 3.x** and `pip` installed.
2.  **Clone the Repository:**
    ```bash
    git clone YOUR_GITHUB_REPOSITORY_URL
    cd YOUR_REPOSITORY_NAME
    ```
3.  **Install Dependencies:** This project strongly recommends using the following libraries[cite: 40]:
    ```bash
    pip install streamlit opencv-python numpy
    ```

***

## How to Run the Application

1.  Navigate to the project directory in your terminal.
2.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
3.  The application will automatically open in your default web browser (typically at `localhost:8501`).

***

## Features Implemented

The application fulfills all core requirements for an interactive edge detection UI[cite: 7].

| Feature Category | Details |
| :--- | :--- |
| **Image Handling** | Allows users to browse and select an image from the local file system[cite: 9]. Accepts common image formats (JPG, PNG, BMP)[cite: 10]. |
| **User Interface** | Side-by-side 'Input' (Original Image) and 'Output' (Processed Result) displays with clear titles[cite: 13, 16, 17]. Uses a wide layout for clarity. |
| **Algorithms** | Provides a selection dropdown for **Canny**, **Sobel**, and **Laplacian** algorithms[cite: 19, 20, 21, 22]. |
| **Canny Parameters** | Sliders for Lower/Upper Thresholds, and Sigma for Gaussian blur[cite: 26]. |
| **Sobel Parameters** | Select boxes for Kernel Size and Gradient Direction (X, Y, or Combined)[cite: 27]. |
| **Laplacian Parameters** | Select box for Kernel Size[cite: 28]. |
| **Interactivity** | Output image updates in real-time as parameters are adjusted[cite: 31, 32].|
| **Parameter Reset** | A dedicated button in the sidebar resets all parameters to their default values while keeping the loaded image. |

***

## Screenshots

*Please replace the placeholder text below with actual screenshots of your running application as required[cite: 53, 54, 55].*

### Main Interface (Input & Output)

[Insert Image showing the uploaded image in the 'Input' column and the edge-detected image in the 'Output' column, side-by-side.]

### Parameter Adjustment UI

[Insert Image clearly showing the sidebar with the algorithm selected and the parameter controls (sliders/select boxes) visible.]
