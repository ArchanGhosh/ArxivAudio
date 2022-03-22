from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
from preprocess import pre_process


def get_pages(filename, start_page=0, end_page=0):
    page_number = []
    for i in range(start_page, end_page):
        page_number.append(i)
    print(page_number)
    #filename = str(paper.title)+'.pdf'
    pages = extract_pages(filename, page_numbers=page_number)

    content = ""
    for page_layout in pages:
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                content = content+element.get_text()
    content = pre_process(content)

    return content
