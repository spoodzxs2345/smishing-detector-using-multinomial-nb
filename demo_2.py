import gradio as gd
import pickle

def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

model_path = 'smish_detector.pkl'
model = load_model(model_path)

def smishing_detection(text):
    pred = model.predict([text])[0]
    if pred == 0:
        return 'This is not a smishing message.'
    else:
        return 'This is a potential smishing message.'

iface = gd.Interface(
    fn=smishing_detection,
    inputs='text',
    outputs='text',
    title='Smishing Detection',
    live=True,
    description='This is a demo for smishing detection.',
    examples=[
        'Your account has been suspended. Please click the link to verify your account.',
        'Attention! Your account has been hacked. Please click the link to change your password.'
    ]
)

iface.launch()