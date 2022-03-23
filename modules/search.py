import arxiv


def search(query="", max_results=10, sort_by="Relevance", sort_order="Descending"):

    sr_by_dict = {"Relevance": arxiv.SortCriterion.Relevance, "Last Updated Date":
                  arxiv.SortCriterion.LastUpdatedDate, "Submitted Date": arxiv.SortCriterion.SubmittedDate}
    sr_or_dict = {"Descending": arxiv.SortOrder.Descending,
                  "Ascending": arxiv.SortOrder.Ascending}

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=sr_by_dict[sort_by],
        sort_order=sr_or_dict[sort_order])
    src_lst = []
    for i in search.results():
        id = i.entry_id.split("/")
        src_lst.append(i.title+" - " + str(id[-1]))

    return src_lst
