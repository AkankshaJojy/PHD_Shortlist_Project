import math


def calculate_score(
    researcher
):

    paper_score = (
        researcher.get(
            "paper_count",
            0
        )
        *
        10
    )


    citation_score = math.log(
        researcher.get(
            "citation_count",
            1
        )
    )


    activity_score = math.log(
        researcher.get(
            "works_count",
            1
        )
    )


    return round(
        paper_score
        +
        citation_score
        +
        activity_score,
        2
    )



def rank_researchers(
    researchers,
    top_k=100
):

    for researcher in researchers:

        researcher["score"] = calculate_score(
            researcher
        )


    researchers.sort(
        key=lambda x:
        x["score"],
        reverse=True
    )


    return researchers[:top_k]
def remove_invalid_researchers(
    researchers
):

    return [
        r for r in researchers
        if r.get("institution")
        and r.get("name")
    ]