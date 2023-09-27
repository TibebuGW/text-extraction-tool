import matplotlib.pyplot as plt
import asyncio
from utils.ocr_utils import get_text_predictions, create_bbox_for_text
from utils.secret_manager_utils import get_secret_value_dict
from utils.chatgpt_utils import get_menu_dict_from_ocr_output
from DataModels.Menu import Menu

if __name__ == "__main__":
    im_file = "/Users/tibeb/Desktop/menu.png"

    # secret_value = get_secret_value_dict()
    total_preds, ocr_output = get_text_predictions(im_file)
    annotated_im = create_bbox_for_text(im_file, ocr_output)
    
    def get_dictionary(predictions):
        dct = get_menu_dict_from_ocr_output(predictions)
        return dct
    
    arranged_dictionary = get_dictionary(total_preds)
    menu = Menu()
    for name, price in arranged_dictionary.items():
        menu.addMenuItem(name, price)

    plt.imshow(annotated_im)
    plt.show()
