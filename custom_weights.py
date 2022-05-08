from cvlib.object_detection import YOLO

yolo = YOLO(weights, config, labels)
bbox, label, conf = yolo.detect_objects(img)
yolo.draw_bbox(img, bbox, label, conf)

bbox, label, conf = yolo.detect_objects(img, enable_gpu=True)