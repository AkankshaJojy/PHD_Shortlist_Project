def build_researchers_from_papers(
    papers
):

    researchers = {}

    for paper in papers:

        for author in paper["authors"]:

            author_info = author.get(
                "author",
                {}
            )

            author_id = author_info.get(
                "id"
            )

            if not author_id:
                continue

            if author_id not in researchers:

                researchers[author_id] = {
                    "id": author_id,
                    "name": author_info.get(
                        "display_name",
                        ""
                    ),
                    "paper_count": 0,
                    "total_citations": 0,
                    "papers": []
                }

            researchers[
                author_id
            ]["paper_count"] += 1

            researchers[
                author_id
            ]["total_citations"] += (
                paper["citations"]
            )

            researchers[
                author_id
            ]["papers"].append(
                paper["title"]
            )

    return list(
        researchers.values()
    )