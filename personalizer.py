from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_why_match(
    student_interest,
    researcher
):

    prompt = f"""

You are helping a PhD applicant.

Student research interests:
{student_interest}


Professor information:

Name:
{researcher.get("name")}

Research areas:
{researcher.get("research_focus")}

Important papers:
{researcher.get("evidence",{}).get("papers")}


Write a short personalized reason why this professor is a good PhD match.

Rules:
- Mention specific research/paper if possible
- Avoid generic words
- Keep it 2 sentences
- Professional email style


"""


    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content