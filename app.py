import streamlit as st
from PIL import Image
from utils.onnx_runtime import predict_class

# Define custom CSS styling for Streamlit components
st.markdown("""
<style>
.header {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-bottom: 30px;
}
.title {
    font-size: 48px;
    color: #FF6347;
    padding: 20px;
}
.icon {
    font-size: 64px;
    margin-bottom: 10px;
    color: #FF6347;
}
</style>
""", unsafe_allow_html=True)

# Display the StreamSign title
# Display the StreamSign title
st.markdown('<div class="header"><h1 class="title">StreamSign</h1></div>', unsafe_allow_html=True)

# Upload an image
uploaded_files = st.file_uploader(
    "Upload images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])


if uploaded_files is not None:
    images = [Image.open(file) for file in uploaded_files]

    # Display the letter predictions for each image
    predictions = predict_class(images)
    st.subheader("Predicted Letters and Images")
    for i in range(len(images)):
        st.subheader("Predicted Letter")
        st.markdown(
            f'<p class="icon">{predictions[i]}</p>', unsafe_allow_html=True)
        st.subheader("Image")
        st.image(images[i], use_column_width=True,caption=f"Image {i+1}", clamp=True, output_format="JPEG")
        