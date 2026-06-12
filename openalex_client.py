import requests
from typing import List, Dict

BASE_URL = "https://api.openalex.org"


class OpenAlexClient:

    def __init__(self):
        self.base_url = BASE_URL

    def search_researchers(
        self,
        research_interest: str,
        max_results: int = 100
    ) -> List[Dict]:

        url = f"{self.base_url}/authors"

        params = {
            "search": research_interest,
            "per-page": max_results
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return []

        data = response.json()

        researchers = []

        for author in data.get("results", []):

            institution = ""
            country = ""

            if author.get("last_known_institutions"):

                institution_data = author[
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

            researchers.append({
                "id": author.get("id"),
                "name": author.get("display_name"),
                "institution": institution,
                "country": country,
                "works_count": author.get(
                    "works_count",
                    0
                ),
                "citation_count": author.get(
                    "cited_by_count",
                    0
                ),
                "topics": [
                    topic.get("display_name")
                    for topic in author.get(
                        "topics",
                        []
                    )
                ]
            })

        return researchers

    def get_author_papers(
        self,
        author_id: str,
        max_results: int = 5
    ):

        openalex_id = author_id.split("/")[-1]

        url = f"{self.base_url}/works"

        params = {
            "filter": f"author.id:https://openalex.org/{openalex_id}",
            "per-page": max_results
        }

        response = requests.get(
            url,
            params=params
        )

        if response.status_code != 200:
            return []

        data = response.json()

        papers = []

        for work in data.get("results", []):

            paper_url = ""

            if work.get("primary_location"):
                paper_url = work.get(
                    "primary_location",
                    {}
                ).get(
                    "landing_page_url",
                    ""
                )

            papers.append({
                "title": work.get(
                    "display_name",
                    ""
                ),
                "year": work.get(
                    "publication_year"
                ),
                "url": paper_url,
                "citations": work.get(
                    "cited_by_count",
                    0
                )
            })

        return papers
    
    def get_author_papers(
        self,
        author_id: str,
        max_results: int = 5
    ):

        openalex_id = author_id.split("/")[-1]

        url = f"{self.base_url}/works"

        params = {
            "filter": f"author.id:https://openalex.org/{openalex_id}",
            "per-page": max_results
        }

        response = requests.get(
            url,
            params=params
        )

        if response.status_code != 200:
            return []

        data = response.json()

        papers = []

        for work in data.get("results", []):

            paper_url = ""

            if work.get("primary_location"):
                paper_url = work.get(
                    "primary_location",
                    {}
                ).get(
                    "landing_page_url",
                    ""
                )

            papers.append({
                "title": work.get(
                    "display_name",
                    ""
                ),
                "year": work.get(
                    "publication_year"
                ),
                "url": paper_url,
                "citations": work.get(
                    "cited_by_count",
                    0
                )
            })

        return papers

    def search_papers(
        self,
        topic: str,
        max_results: int = 50
    ):

        url = f"{self.base_url}/works"

        params = {
            "search": topic,
            "per-page": max_results
        }

        response = requests.get(
            url,
            params=params
        )

        if response.status_code != 200:
            return []

        data = response.json()

        papers = []

        for work in data.get(
            "results",
            []
        ):

            papers.append({
                "paper_id": work.get("id"),
                "title": work.get(
                    "display_name",
                    ""
                ),
                "year": work.get(
                    "publication_year"
                ),
                "citations": work.get(
                    "cited_by_count",
                    0
                ),
                "authors": work.get(
                    "authorships",
                    []
                )
            })

        return papers