import cv2
import onnxruntime as ort
from inference.models.utils import get_roboflow_model

model = get_roboflow_model(
    model_id="tumor-detector-mjgdm/1",
    api_key="TZWGrcQ58qw0jpHYZWLq"
)

def run_inference(image_path, save_path=None):
    # Force CPU ExecutionProvider if possible
    if hasattr(model, 'session'):
        model.session.set_providers(['CPUExecutionProvider'])

    frame = cv2.imread(image_path)
    if frame is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    results = model.infer(
        image=frame,
        confidence=0.5,
        iou_threshold=0.5
    )

    if results and results[0].predictions:
        for pred in results[0].predictions:
            x, y = int(pred.x), int(pred.y)
            w, h = int(pred.width), int(pred.height)
            x0, y0 = x - w // 2, y - h // 2
            x1, y1 = x + w // 2, y + h // 2

            cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 255), 2)
            cv2.putText(frame, pred.class_name, (x0, y0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    else:
        print("No predictions found.")

    if save_path:
        cv2.imwrite(save_path, frame)

    return frame, results[0].predictions if results else []
