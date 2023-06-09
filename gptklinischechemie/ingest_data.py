# importing required modules
import PyPDF2
import json
import re

from utils import remove_header_footer

# creating a pdf file object
file_object = open('data/basis2021.pdf', 'rb')

# creating a pdf reader object
reader_object = PyPDF2.PdfReader(file_object)

# printing number of pages in pdf file
len(reader_object.pages)

# append everything into one string
text = ''

for i in range(len(reader_object.pages)):
    text += ' '.join(reader_object.pages[i].extract_text().split(' ')[6:])
print(len(text.split("Tentamen deel ")))

output = {}

# split and also generate index in looop
for i, deel in enumerate(text.split("Tentamen deel ")[1:]):
    # eerste deel kunnen we negeren (zijn instructies)

    output[f'deel {i+1}'] = []

    if i == 0:  # tt deel 1
        for ic, casus in enumerate(re.split('Casus \d+', deel)[1:]):
            split_op_vragen = casus.split("Vraag ")

            output[f'deel {i+1}'].append({
                'casus': split_op_vragen[0].strip(),
                'vragen': []
            })

            # split op vraag
            for vraag in split_op_vragen[1:]:
                output[f'deel {i+1}'][ic]['vragen'].append(vraag.strip())
    else:  # tt deel 2, geen casussen
        split_op_vragen = deel.split("Vraag ")

        output[f'deel {i+1}'].append({
            'casus': None,
            'vragen': []
        })

        # split op vraag
        for vraag in split_op_vragen[1:]:
            output[f'deel {i+1}'][0]['vragen'].append(vraag.strip())

# exporteer output naar out/ als JSON file (formatteer met indent=4)
json.dump(output, open('out/basis2021.json', 'w'), indent=4)

# schrijf ruwe tekst naar out/ als txt file
with open('out/basis2021.txt', 'w', encoding="utf-8") as f:
    f.write(text)
