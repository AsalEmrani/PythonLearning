
from deep_translator import GoogleTranslator

# try:
    
filepath = "C:\\Asal\\"
filename = "Frozen (2013) Bluray-1080p.en"
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open(os.path.join(filepath, filename)+'.srt') as f :
    sub_line = f.readlines()

with open((os.path.join(filepath, filename)+'.txt'), 'w') as f :
    for line_en in sub_line :
        if line_en[0] in numbers :
            f.write(line_en)
        elif line_en == '\n' :
            f.write('\n')
        else :
            line_fa = GoogleTranslator(source='en', target='fa').translate(line_en)
            f.write(line_fa.text)

# print(f"Original: {line}")
    # print(f"Translated: {translated}")

# except Exception as e:
#     print("Translation failed!")
#     print(f"Error: {e}")
