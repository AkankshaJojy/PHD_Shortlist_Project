def filter_research_institutions(
    researchers
):

    blocked_keywords = [
        "College Board",
        "Company",
        "Corporation",
        "Inc",
        "Ltd"
    ]


    filtered = []


    for r in researchers:

        institution = r.get(
            "institution",
            ""
        )


        if any(
            word.lower()
            in institution.lower()
            for word in blocked_keywords
        ):
            continue


        filtered.append(r)


    return filtered