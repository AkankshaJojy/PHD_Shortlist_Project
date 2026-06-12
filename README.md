# PhD Shortlist Builder


AI system that generates personalized PhD supervisor recommendations from student research interests.

The system retrieves researchers, verifies research relevance, ranks candidates, and produces a machine-readable shortlist.



## Architecture


Student Profile

↓

Research Interest Expansion

↓

OpenAlex Research Database

↓

Paper + Author Retrieval

↓

Researcher Filtering

↓

Ranking Model

↓

LLM Personalization

↓

JSON Shortlist



## Data Source

OpenAlex API

Provides:
- researchers
- institutions
- publications
- citation information



## Features

- Country filtering
- Research relevance ranking
- Evidence based matching
- Personalized why_match generation
- JSON output


 
## Run


Install:

pip install -r requirements.txt


Add .env:

OPENAI_API_KEY=your_key


Run:

python main.py



## Limitations

- Email extraction requires additional university scraping
- Some researcher verification requires external academic databases


## Future Improvements

- Semantic vector search
- Supervisor availability detection
- Feedback learning from student outcomes