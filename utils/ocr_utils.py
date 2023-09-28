import cv2
import easyocr
from typing import List, Tuple



def create_bbox_for_text(im_file, output):
    """Draws rectangles specified by `output` bounding boxes on image `im_file`.

    Args:
        im_file (str): Path to the image file.
        output (list): List of bounding boxes in the format ((x1, y1), _, (x2, y2), _).

    Returns (ndarray): The image with drawn bounding boxes.
    """

    try:
        im = cv2.imread(im_file)
        for bbox, *_ in output:
            left, up, right, down = get_corners_from_bbox(bbox)
            if left is None:
                continue
            im = cv2.rectangle(im, (left, up), (right, down), (0, 255, 0), 1)
            pass
    except Exception as e:
        print(f"Error encountered: {e}")
        im = None
    return im


def get_text_predictions(im_file: str):
    """Extract text predictions from an image and return the annotated image.

    This function reads an image file and uses an Optical Character Recognition (OCR)
    reader to detect and extract text within the image. Each detected text area is
    annotated with a bounding box on the image. The function returns a list of text
    predictions with their corresponding bbox coordinates and the annotated image

    Args:
        im_file (str): A string representing the path of the image file to be processed.

    Returns:
        total_preds (list): A list of strings where each string contains the predicted text from
            a section of the image and the coordinates of the bbox for that text in the format:
            'text=<text>: left=<left_coord>, right=<right_coord>, up=<up_coord>, down=<down_coord>'
    """

    reader = easyocr.Reader(["en"])
    output = reader.readtext(im_file, detail=1)

    pred_list = []
    for bbox, text, _ in output:
        left, up, right, down = get_corners_from_bbox(bbox)
        if not left:
            continue
        pred = f"{text=}: {left=}, {right=}, {up=}, {down=}"
        pred_list.append(pred)

    return pred_list, output


def get_corners_from_bbox(bbox: List[Tuple]):
    """Given a bounding box, this function extracts and returns the coordinates
    of the upper left and lower right corners.

    A bounding box is typically a list or tuple of four elements
    (upper_left, _, lower_right, _), where `upper_left` and `lower_right`
    are themselves tuples/lists representing the (x, y) coordinates of the
    respective corners of the bounding box. The underscore ('_') represents
    optional information not used by this function.

    The function converts the coordinates to integers using the built-in
    `map` function, as some sources might provide these as floats.

    Args:
        bbox(tuple or list): The bbox from which the corner coordinates are to be extracted.
            Expected format: ((x1, y1), _, (x2, y2), _)

    Returns
    -------
    tuple
        A tuple containing four integers representing the x and y coordinates
        of the upper left and lower right corners of the bounding box in the
        order (left, up, right, down).
    """
    try:
        upper_left, _, lower_right, _ = bbox
        left, up = map(int, upper_left)
        right, down = map(int, lower_right)
        return left, up, right, down
    except:
        return None, None, None, None
