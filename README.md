Hello everyone!
With the advancement in detection, ultralytics recently launched their yolo v8 that is now compatible with oriented
bounding boxes. (OBB)
<br><br>

### So what does that mean?<br>

It means that now we can detect diagonal objects without the need to annotate them as horizontal or vertical.

### Objective:

What I really want to achieve here is simple. The code is out recently and it might take some time for everyone to catch
up with their docs. Here is a simple project using the yolov8 obb to detect planes using the DOTA dataset. Hopefully,
this helps everyone know what arguments to use and where.

#### Data Format:
![alt text](https://github.com/shivekchhabra/diagonal_object_detection_yolov80bb/blob/master/outputs/label_format.png)

## Training Phase:

So I have used the training data from DOTA (open source data with obb annotations) and trained for just 50 epochs. My
global mAP was 69%. This can be improved with a better model and better hyperparameters
![alt text](https://github.com/shivekchhabra/diagonal_object_detection_yolov80bb/blob/master/outputs/training.png)

## Metrics:
I have put in a file which you can use to validate your model on your val/test sets.

## Detection:
Finally, there is a file to help you detect on real data.
![alt text](https://github.com/shivekchhabra/diagonal_object_detection_yolov80bb/blob/master/outputs/planes_detected.jpg)

## References:
https://github.com/ultralytics/ultralytics<br>
https://docs.ultralytics.com/datasets/obb/<br>
https://docs.ultralytics.com/tasks/obb/
