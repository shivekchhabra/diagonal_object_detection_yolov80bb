import torch
import os
from ultralytics import YOLO


def train(yaml_path, epochs, imgsz, batch, project):
    # Emptying cache before running can help with multiple small experiements
    torch.cuda.empty_cache()
    model = YOLO('yolov8n-obb.pt')
    results = model.train(data=yaml_path, epochs=epochs, imgsz=imgsz, batch=batch, project=project,
                          device=0, cache='ram')


if __name__ == '__main__':
    yaml_path = 'data_files/data.yaml'

    f = open(yaml_path, 'r')
    data = f.read()
    f.close()
    data = data.replace("data_path", f"{os.getcwd()}{os.sep}dota")
    f = open(yaml_path, 'w')
    f.write(data)
    f.close()

    epochs = 50
    img_size = 960
    batch = 4
    project = "obb_runs"

    if project not in os.listdir():
        os.mkdir(project)

    train(yaml_path, epochs, img_size, batch, project)
