import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():

    detector=dlib.get_frontal_face_detector()

    sp=dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())

    facerec=dlib.face_recognition_model_v1(face_recognition_models.face_recognition_model_location())
    return detector, sp, facerec 

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)
    encoding=[]
    for face in faces:
        shape=sp(image_np, face) #68 landmarks
        face_descriptor=facerec.compute_face_descriptor(image_np, shape,1) #128 embeddings
        encoding.append(np.array(face_descriptor))
    return encoding

@st.cache_resource
def get_trained_model():

    student_db = get_all_students()
    X = []
    y = []
    if not student_db:
        return None
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding, dtype=np.float64))
            y.append(int(student['student_id']))

    if len(X) == 0:
        return None
    clf = None
    if len(set(y)) >= 2:
        clf = SVC(
            kernel='linear',
            probability=True,
            class_weight='balanced'
        )
        try:
            clf.fit(X, y)
        except ValueError:
            return None
    return {
        "clf": clf,
        "X": X,
        "y": y
    }
def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return model_data is not None

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}
    model_data = get_trained_model()
    if model_data is None:
        return detected_student, [], len(encodings)

    clf = model_data["clf"]
    X_train = model_data["X"]
    y_train = model_data["y"]
    all_students = sorted(set(y_train))
    for encoding in encodings:
        if clf is None:
            predicted_id = all_students[0]
        else:
            predicted_id = int(
                clf.predict([encoding])[0]
            )
        student_embedding = X_train[
            y_train.index(predicted_id)
        ]
        best_match_score = np.linalg.norm(
            student_embedding - encoding
        )
        resemblance_threshold = 0.6
        if best_match_score < resemblance_threshold:
            detected_student[predicted_id] = best_match_score
    return detected_student, all_students, len(encodings)
