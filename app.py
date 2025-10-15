import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io

# ---------- Page setup ----------
st.set_page_config(page_title="EdgeVision Studio", page_icon="✨", layout="wide")
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg,#f8fafc 0%,#e2e8f0 100%); }
    .title { font-size:34px; font-weight:800; text-align:center;
             background: -webkit-linear-gradient(#0ea5e9,#2563eb);
             -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .subtitle { text-align:center; color:#475569; margin-bottom:20px; }
    .card { background:white; border-radius:16px; padding:12px;
            box-shadow:0 8px 24px rgba(15,23,42,0.08); }
    .img-title { font-weight:600; color:#0f172a; margin-bottom:6px; }
    .about { font-size:14px; color:#475569; margin-top:16px; text-align:center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>EdgeVision Studio</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Compare and visualize image edges using Sobel, Laplacian & Canny filters — instantly.</div>", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Controls")
    use_camera = st.checkbox("Use camera instead of upload", value=False)
    uploaded_file = None
    if not use_camera:
        uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png", "bmp"])

    algo = st.radio("Choose algorithm", ["Sobel", "Laplacian", "Canny"], index=0)
    compare_mode = st.checkbox("Compare with another algorithm")
    st.markdown("---")

    params = {}
    if algo == "Sobel":
        params["ksize"] = st.slider("Kernel size", 1, 9, 3, step=2)
        params["dx"] = st.selectbox("dx", [0, 1, 2], index=1)
        params["dy"] = st.selectbox("dy", [0, 1, 2], index=0)
    elif algo == "Laplacian":
        params["ksize"] = st.slider("Kernel size", 1, 9, 3, step=2)
    elif algo == "Canny":
        params["threshold1"] = st.slider("Lower threshold", 0, 255, 100)
        params["threshold2"] = st.slider("Upper threshold", 0, 255, 200)
        params["apertureSize"] = st.slider("Aperture size", 3, 7, 3, step=2)

    if st.button("Reset"):
        st.rerun()

# ---------- Edge functions ----------
def sobel(img, dx, dy, k):
    if dx == dy == 0: dx = 1
    g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    grad = cv2.Sobel(g, cv2.CV_64F, dx, dy, ksize=k)
    return cv2.convertScaleAbs(grad)

def laplacian(img, k):
    g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    lap = cv2.Laplacian(g, cv2.CV_64F, ksize=k)
    return cv2.convertScaleAbs(lap)

def canny(img, t1, t2, ap):
    g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return cv2.Canny(g, t1, t2, apertureSize=ap)

def process(img, algo, p):
    if algo == "Sobel":   return sobel(img, p["dx"], p["dy"], p["ksize"])
    if algo == "Laplacian": return laplacian(img, p["ksize"])
    if algo == "Canny":   return canny(img, p["threshold1"], p["threshold2"], p["apertureSize"])
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def to_pil(arr):
    if len(arr.shape)==2: arr = cv2.cvtColor(arr, cv2.COLOR_GRAY2RGB)
    return Image.fromarray(arr)

# ---------- Core display ----------
col1, col2 = st.columns(2, gap="large")

def show_pair(original, processed, title1="Original", title2="Processed"):
    with col1:
        st.markdown(f"<div class='card'><div class='img-title'>{title1}</div>", unsafe_allow_html=True)
        st.image(original, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><div class='img-title'>{title2}</div>", unsafe_allow_html=True)
        st.image(processed, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

if use_camera:
    st.markdown("<div style='text-align:center; font-weight:600;'>Live Camera Mode</div>", unsafe_allow_html=True)
    cam = st.camera_input("Capture photo")
    if cam:
        img = np.array(Image.open(io.BytesIO(cam.getvalue())).convert("RGB"))
        result = process(img, algo, params)
        show_pair(img, result, "Captured", f"{algo} Output")
        buf = io.BytesIO(); to_pil(result).save(buf, "PNG")
        st.download_button("Download", buf.getvalue(), file_name=f"edge_{algo.lower()}.png")
else:
    if uploaded_file:
        img = np.array(Image.open(uploaded_file).convert("RGB"))
        res1 = process(img, algo, params)
        if compare_mode:
            second_algo = st.selectbox("Compare with:", ["Laplacian","Sobel","Canny"], index=1)
            st.info(f"Comparing {algo} vs {second_algo}")
            res2 = process(img, second_algo, params)
            colA, colB, colC = st.columns(3)
            with colA: st.image(img, caption="Original", use_column_width=True)
            with colB: st.image(res1, caption=f"{algo} Output", use_column_width=True)
            with colC: st.image(res2, caption=f"{second_algo} Output", use_column_width=True)
        else:
            show_pair(img, res1, "Input", f"{algo} Output")
        buf = io.BytesIO(); to_pil(res1).save(buf, "PNG")
        st.download_button("Download Processed Image", buf.getvalue(),
                           file_name=f"edge_{algo.lower()}.png", mime="image/png")
    else:
        show_pair(Image.new("RGB",(512,384),(240,240,245)),
                  Image.new("RGB",(512,384),(250,250,250)))

st.markdown("<div class='about'>Built using Python & Streamlit (2025).<br>© EdgeVision Studio — Final Polish Edition.</div>", unsafe_allow_html=True)
