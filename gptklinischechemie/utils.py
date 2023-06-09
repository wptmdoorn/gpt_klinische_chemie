import re


def remove_header_footer(pdf_extracted_text):
    page_format_pattern = r'([pagina]+[\d]+)'
    pdf_extracted_text = pdf_extracted_text.lower().split("\n")
    header = pdf_extracted_text[0].strip()
    footer = pdf_extracted_text[-1].strip()
    if re.search(page_format_pattern, header) or header.isnumeric():
        pdf_extracted_text = pdf_extracted_text[1:]
    if re.search(page_format_pattern, footer) or footer.isnumeric():
        pdf_extracted_text = pdf_extracted_text[:-1]
    pdf_extracted_text = "\n".join(pdf_extracted_text)
    return pdf_extracted_text
