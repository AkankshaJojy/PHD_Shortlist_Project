import json


def generate_shortlist(
    researchers,
    filename="shortlist.json"
):

    shortlist = []


    for r in researchers:

        item = {

            "name": r.get(
                "name",
                ""
            ),

            "institution": r.get(
                "institution",
                ""
            ),

            "country": r.get(
                "country",
                ""
            ),

            "research_focus": r.get(
                "topics",
                []
            ),


            "evidence": {

                "papers": r.get(
                    "papers",
                    []
                ),

                "citation_count": r.get(
                    "citation_count",
                    0
                )

            },


            "why_match":

            (
            "Research alignment with "
            + ", ".join(
                r.get(
                    "topics",
                    []
                )[:2]
            )
            ),


            "tier":
            "target"

        }


        shortlist.append(item)


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            shortlist,
            f,
            indent=4,
            ensure_ascii=False
        )


    return shortlist