import onnx, onnxruntime
import streamlit as st
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np

alphabet_dict = {0: 'A',1: 'B',2: 'C',3: 'D',4: 'E',5: 'F',6: 'G',7: 'H',8: 'I',9: 'K',10: 'L',11: 'M',
    12: 'N',13: 'O',14: 'P',15: 'Q',16: 'R',17: 'S',18: 'T',19: 'U',20: 'V',21: 'W',22: 'X',23: 'Y'}

model_path = 'models\CNN_Model_Sign_Language_best.onnx'
onnx_model = onnx.load(model_path)
onnx.checker.check_model(onnx_model)

#to preprocess an external image
preprocess = transforms.Compose([
                transforms.Resize((28,28)),
                transforms.Grayscale(num_output_channels=1),
                transforms.ToTensor()])        

EP_list = ['CUDAExecutionProvider', 'CPUExecutionProvider']

ort_session = onnxruntime.InferenceSession(model_path, providers=EP_list)

def predict_class(img_list):
    """
    Predicts the class of input images using an ONNX model.

    Args:
        img_list (list): A list of input image tensors.

    Returns:
        list: A list of predicted class indices.

    """
    predictions = []
    for img in img_list:
        img = np.array(preprocess(img).unsqueeze(0).cpu())
        ort_inputs = {ort_session.get_inputs()[0].name: img}
        ort_outs = ort_session.run(None, ort_inputs)
        pred = list(ort_outs[0][0]).index(max(ort_outs[0][0]))
        predictions.append(pred)
    
    return [str(alphabet_dict[p]) for p in predictions]
