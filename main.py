import cv2
from ultralytics import YOLO

# 加载预训练的YOLOv10模型
model = YOLO("yolov10n.pt")

# 初始化摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取摄像头视频帧")
            break

        # 使用模型进行预测
        results = model(frame)
        
        # 获取检测结果
        boxes = results[0].boxes
        
        # 处理检测结果并绘制边界框和标签
        for box in boxes:
            xyxy = box.xyxy[0].cpu().numpy().astype(int)
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f'{model.names[cls]} {conf:.2f}'
            cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (255, 0, 0), 2)
            cv2.putText(frame, label, (xyxy[0], xyxy[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # 显示结果
        cv2.imshow('YOLOv10 Object Detection', frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
