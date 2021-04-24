from translate import Translator

trans = Translator(to_lang = 'ne')
try:
    with open('Noex.txt' , mode='r') as trans_file:
      to_trans = trans_file.read()
      translation = trans.translate(to_trans)
      print(translation)
      with open('transfile.txt',mode = 'w',encoding='utf-8') as Trans_file:
          Trans_file.write(translation)
except FileNotFoundError as err:
    print('silly me')