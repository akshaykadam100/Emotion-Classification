# Emotion-Classification

Objective of this case study is to identify facial emotion and classify them under 
- Angry
- Disgusted
- Fearful
- Happy
- Neutral
- Sad
- Surprised

For this we are using 2 models.

1. [Haarcascade Frontal Face Default](#https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml): This is a pretrained model (for detecting human face) which comes up from opencv-contrib-python module
2. [CNN Trained Model](file:///modelling/model.h5): Trained locally using Custom built CNN model from scratch to detect emotions

Data for this case study is sourced from [Kaggle](#https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer)

Currently, emotion classification accuracy is capped at 61% as model training is still under development

User can run `main.py` to detect emotions.
Webcam is needed to capture live stream
