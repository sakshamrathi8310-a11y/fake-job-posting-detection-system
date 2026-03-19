import streamlit as st
import pickle

st.set_page_config(
    page_title="Fake Job Detector",
    page_icon="⚠️",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("job_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("tfidf_vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model()

st.title("🕵️ Fake Job Posting Detector")
st.markdown("Enter job details to check if it is **Real or Fake**.")

user_input = st.text_area("Enter Job Description Here:")

if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("Please enter job details.")
    else:
        with st.spinner("Analyzing..."):
            transformed_text = vectorizer.transform([user_input])
            prediction = model.predict(transformed_text)
            probability = model.predict_proba(transformed_text)

        confidence = round(max(probability[0]) * 100, 2)

        if prediction[0] == 1:
            st.error(f"⚠️ FAKE Job Posting\nConfidence: {confidence}%")
        else:
            st.success(f"✅ REAL Job Posting\nConfidence: {confidence}%")

st.markdown("---")
st.caption("Built by Saksham Rathi | Fake Job Detection Project")

