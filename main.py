from src.openalex_client import OpenAlexClient

from src.researcher_builder import (
    build_researchers_from_papers
)

from src.researcher_enricher import (
    enrich_researcher
)

from src.filters import (
    filter_country
)

from src.ranker import (
    rank_researchers,
    remove_invalid_researchers
)

from src.quality_filter import (
    filter_research_institutions
)

from src.output import (
    generate_shortlist
)

from src.personalizer import generate_why_match


client = OpenAlexClient()



papers = client.search_papers(
    "Medical Imaging",
    max_results=200
)

print(
    "Papers Found:",
    len(papers)
)


researchers = build_researchers_from_papers(
    papers
)

print(
    "Researchers Found:",
    len(researchers)
)



enriched = []


for researcher in researchers[:150]:

    result = enrich_researcher(
        researcher
    )

    enriched.append(
        result
    )


print(
    "Enriched:",
    len(enriched)
)




clean = remove_invalid_researchers(
    enriched
)


print(
    "After Cleaning:",
    len(clean)
)




country_filtered = filter_country(
    clean,
    [
        "US",
        "CA"
    ]
)


print(
    "After Country Filter:",
    len(country_filtered)
)





quality_checked = filter_research_institutions(
    country_filtered
)
for researcher in quality_checked:

    researcher["why_match"] = generate_why_match(
        [
            "Medical AI",
            "Computer Vision",
            "Deep Learning"
        ],
        researcher
    )


    researcher["contact_email"] = "Not found"

    researcher["phd_program"] = (
        "Check university graduate admissions page"
    )

print(
    "After Quality Filter:",
    len(quality_checked)
)




ranked = rank_researchers(
    quality_checked,
    top_k=50
)


print(
    "Final Ranked Researchers:",
    len(ranked)
)





generate_shortlist(
    ranked,
    "output/shortlist.json"
)


print(
    "JSON created successfully"
)





for r in ranked[:10]:

    print("\n----------------")

    print(
        "Name:",
        r.get("name")
    )

    print(
        "Institution:",
        r.get("institution")
    )

    print(
        "Country:",
        r.get("country")
    )

    print(
        "Score:",
        r.get("score")
    )