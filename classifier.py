
import logging
import numpy as np
from PIL import Image as pil_image

import onnxruntime




class Classifier:
    nsfw_model = None

    def __init__(self, model_path):
        self.nsfw_model = onnxruntime.InferenceSession(model_path)

    def classify(self, image_path):

    # Hardcoded values
        batch_size = 1
        image_size = (256, 256)
        categories = ["unsafe", "safe"]

    # Load and preprocess the image
        loaded_images, loaded_image_paths = load_images([image_path], image_size, image_names=[image_path])

        if not loaded_image_paths:
            return {}

        preds = []
        model_preds = []
    
    # Run predictions
        _model_preds = self.nsfw_model.run(
        [self.nsfw_model.get_outputs()[0].name],
        {self.nsfw_model.get_inputs()[0].name: loaded_images},
    )[0]

        model_preds.append(_model_preds)
        preds += np.argsort(_model_preds, axis=1).tolist()

        probs = []
        for i, single_preds in enumerate(preds):
           single_probs = []
           for j, pred in enumerate(single_preds):
               single_probs.append(model_preds[int(i / batch_size)][int(i % batch_size)][pred])
               preds[i][j] = categories[pred]

               probs.append(single_probs)

        images_preds = {}
        for i, loaded_image_path in enumerate(loaded_image_paths):
            if not isinstance(loaded_image_path, str):
                loaded_image_path = i

        images_preds[loaded_image_path] = {}
        for _ in range(len(preds[i])):
            images_preds[loaded_image_path][preds[i][_]] = float(probs[i][_])
                                                                 
        return images_preds


def load_images(image_paths, image_size, image_names):
    loaded_images = []
    loaded_image_paths = []

    for i, img_path in enumerate(image_paths):
        try:
            image = load_images(image_paths, target_size=image_size)
            image = (image) / 255  #Normalization
            loaded_images.append(image)
            loaded_image_paths.append(image_names[i])
        except Exception as ex:
            logging.exception(f"Error reading {img_path} {ex}", exc_info=True)

    return np.asarray(loaded_images), loaded_image_paths

if __name__ == "__main__":
    model_path = "\classifier_model.onnx"
    m = Classifier(model_path)

    while 1:
        images = input().split("||")
        images = [image.strip() for image in images]
        print(m.classify(images), "\n")
