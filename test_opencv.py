import streamlit as st

try:
    import cv2
    st.success("✅ OpenCV imported successfully!")
    st.write(f"OpenCV version: {cv2.__version__}")
except ImportError as e:
    st.error(f"❌ OpenCV import failed: {e}")
    st.info("This is expected on some deployment environments. The app will use limited functionality.")