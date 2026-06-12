COUNTRY_MAP = {
    "US": "United States",
    "CA": "Canada",
    "GB": "United Kingdom",
    "AU": "Australia",
    "DE": "Germany"
}


def filter_country(
    researchers,
    allowed_countries
):

    filtered = []

    for r in researchers:

        if r.get(
            "country"
        ) in allowed_countries:

            filtered.append(r)


    return filtered

def remove_duplicates(
    researchers
):

    unique = {}

    for researcher in researchers:

        key = (
            researcher["name"],
            researcher["institution"]
        )

        unique[key] = researcher

    return list(unique.values())