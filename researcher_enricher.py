import requests


BASE_URL = "https://api.openalex.org"


def enrich_researcher(
    researcher
):

    author_id = researcher["id"]

    openalex_id = author_id.split("/")[-1]

    url = f"{BASE_URL}/authors/{openalex_id}"


    response = requests.get(url)


    if response.status_code != 200:
        return researcher


    data = response.json()


    institution = ""

    country = ""


    if data.get(
        "last_known_institutions"
    ):

        institution_data = data[
            "last_known_institutions"
        ][0]


        institution = institution_data.get(
            "display_name",
            ""
        )


        country = institution_data.get(
            "country_code",
            ""
        )


    researcher.update({

        "institution": institution,

        "country": country,

        "works_count": data.get(
            "works_count",
            0
        ),

        "citation_count": data.get(
            "cited_by_count",
            0
        ),

        "topics": [
            topic.get("display_name")
            for topic in data.get(
                "topics",
                []
            )
        ]

    })


    return researcher