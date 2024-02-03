# If you would like to test the metrics, you could use this
import torch
import os
from ultralytics import YOLO


def metrics_val_test(model_path, split, imgsz, project, batch, conf=0.5):
    torch.cuda.empty_cache()
    model = YOLO(model_path)
    metrics = model.val(split=split, imgsz=imgsz, batch=batch, conf=conf, project=project)
    print(metrics)


if __name__ == '__main__':
    weight_path = 'obb_runs/train3/weights/best.pt'
    project = "obb_runs"

    if project not in os.listdir():
        os.mkdir(project)
    batch = 8
    conf = 0.4
    imgsz = 960
    split = "val"  # You can also use "test" if you have some test data to check metrics on
    metrics_val_test(weight_path, split, imgsz, project, batch, conf)
