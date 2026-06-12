import json

def save_output(results, filename):

    with open(filename, "w") as f:

        json.dump(
            results,
            f,
            indent=4
        )