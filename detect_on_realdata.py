import torch
import os
from ultralytics import YOLO


# To check on real data.

def predict_output(im_path, model_path, imgsz, project, conf=0.5):
    torch.cuda.empty_cache()
    model = YOLO(model_path)

    model(im_path, imgsz=imgsz, conf=conf, project=project, save=True, save_txt=True, save_conf=True,
          name=im_path.split("/")[-1].split('.')[0])


if __name__ == '__main__':
    im_path = "planes.jpg"
    weight_path = 'obb_runs/train3/weights/best.pt'
    project = "detected_outputs"

    if project not in os.listdir():
        os.mkdir(project)
    conf = 0.4
    imgsz = 960
    predict_output(im_path, weight_path, imgsz, project, conf)
