import matplotlib.pyplot as plt
import asyncio
import json
from utils.ocr_utils import get_text_predictions, create_bbox_for_text
from utils.secret_manager_utils import get_secret_value_dict
from utils.chatgpt_utils import get_menu_dict_from_ocr_output
from DataModels.Menu import Menu

if __name__ == "__main__":
    im_file = "./images/menu.png"

    # secret_value = get_secret_value_dict()
    total_preds, ocr_output = get_text_predictions(im_file)
    annotated_im = create_bbox_for_text(im_file, ocr_output)
    
    def get_dictionary(predictions):
        dct = get_menu_dict_from_ocr_output(predictions)
        return dct
    
    arranged_dictionary = get_dictionary(total_preds)

    with open('preds.txt', 'r') as file:
        existing_data = json.load(file)

    existing_data.update(arranged_dictionary)

    with open('preds.txt', 'w') as file:
        json.dump(existing_data, file)
    
    print("Menu items appended in preds.txt file")

    # menu = Menu()
    # for name, price in arranged_dictionary.items():
    #     menu.addMenuItem(name, price)

    plt.imshow(annotated_im)
    # plt.show()
