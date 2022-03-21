import arxiv

def get_paper(paper = "GAN You Do the GAN GAN? - 1904.00724v1"):
  id = paper.split(" - ")
  paper = next(arxiv.Search(id_list=[id[-1]]).results())
  paper.download_pdf(filename=(paper.title+".pdf"))

  return(paper)