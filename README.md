# YOLOv10 Real-Time Object Detection

This project demonstrates real-time object detection using the YOLOv10 model and a local camera. The code captures video frames from a webcam, processes them with a YOLOv10 model, and displays the detected objects with bounding boxes and labels.

## Prerequisites

Ensure you have the following libraries installed:

```bash
pip install ultralytics opencv-python torch numpy
```

## Usage

1. Clone the repository and navigate to the project directory.

2. Ensure you have the YOLOv10 pre-trained weights (`yolov10n.pt`). You can download them from the [Ultralytics YOLOv10 GitHub repository](https://github.com/ultralytics/ultralytics).

3. Run the script:

```bash
python main.py
```

## Notes

- Ensure your webcam is properly connected and accessible by the script.
- The script can be modified to use different YOLOv10 model versions by changing the model file name.

## Troubleshooting

- If the webcam window doesn't appear, ensure the webcam is correctly initialized and accessible.
- Check for any errors or warnings in the terminal for further debugging.

## License

This project is open-source and available under the [MIT License](LICENSE).
