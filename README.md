# Emotion-Classification

---

### Problem Statement
The problem statement is to predict face emotion of a human being using Haarcascade algorithm and CNN based trained models.

In this project, we will analyse various face images that have been collected and classify them into following categories.
- Angry
- Disgusted
- Fearful
- Happy
- Neutral
- Sad
- Surprised

---
### Business Problem Overview

In many applications, it is a must to understand behavior of a person using facial expression.
Using this facial classification, it is possible to understand customers review without having him / her to wite / jot down current mood.
Out of the many applications, this can be also used to understand a person behavior while working on a desk to understand whether employee is satisfied during an interview, call or a meeting.

Taking this business problem in mind, we will move ahead in understanding this project in even more depth.

---

### Project Pipeline

For this we are using 2 models.

1. [Face Detection Using Haar-cascade Algorithm](#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml)
- This module includes detecting as many faces inside the image
- Creating bounding box around these faces
2. [CNN Trained Model](file:///modelling/model.h5):
- Library Management
- [Sourcing Data](#https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer)
- Model Training (With Hyperparameter Tuning)
3. Using Trained Model for detecting Face(s) & Emotion(s) on live video stream using WebCam

motion classification accuracy is capped at 61% as model training is still under development

User can run `main.py` to detect emotions.
Webcam is needed to capture live stream

---

### Conclusion
Accuracy of Trained Models Till Date:

| Date          | Train Accuracy (%) | Validation Accuracy (%) |
|---------------|--------------------|-------------------------|
| 18 April 2023 | 95.69              | 62.91                   |
| 19 April 2023 | ---                | ---                     |
