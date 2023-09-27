import os
import openai
import ast
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_dictionary(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_menu_dict_from_ocr_output(menu_info):
    prompt = """
        Below you'll find an array of bounding box information my OCR code using easyocr gathered.
        I tried to scan the image of a menu and the information on the menu is Ethiopian foods and their prices.
        The information outputted from the code is of the following format ["text='Kitfo': left=747, right=797, up=197, down=217" ...].
        Forget the left, right, up, and down information and focus on the texts. Since the OCR tool I used isn't perfect, some of the
        texts are gibberish. So you might see something like [text='syoli': left=421, right=473, up=160, down=187]. The items are arranged in
        price then menu item or menu item to price order. Example for price to menu item is [text='260.00': left=742, right=818, up=220, down=246]
        [text='SC"QA #AT /normal dulet': left=143, right=410, up=244, down=277]. What I want you to do is create a dictionary. In that dictionary
        put in "menu item": "price" information. So for the example I just gave you, the result would be "Normal Dulet": "260.00". If you noticed, I
        took out 'SC"QA #AT /' and just used 'normal dulet' because the first part was gibberish. Try to use your best judgement to figure out the Ethiopian
        food names from the texts. For the menu item to price order, it's all the same except the order of it is changed. I want you to loop through the array
        and then return the dictionary as I described it. Here is the array:
    """ + str(menu_info)

    
    dct = get_dictionary(prompt)
    dct  = dct.replace("'", "\"")
    parsed_dict = ast.literal_eval(dct)
    return parsed_dict




