import numpy as np
import cv2


def convert_pil_to_numpy(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
