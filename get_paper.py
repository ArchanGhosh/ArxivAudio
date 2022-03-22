import arxiv


def get_paper(paper=""):
    id = paper.split(" - ")
    print("id= ", id)

    paper = next(arxiv.Search(id_list=[id[-1]]).results())
    print("paper title= ", paper.title)
    name = str(paper.title) + '.pdf'
    name = name.replace('?', '')
    paper.download_pdf(filename=name)

    return(paper)
