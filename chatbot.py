from google import genai
from dotenv import load_dotenv
import os

from vector_store import load_vector_store


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)



def ask_question(question):

    db = load_vector_store()


    docs = db.similarity_search(
        question,
        k=3
    )


    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )


    prompt = f"""

You are an AI PDF assistant.

Answer only using the given context.


Context:

{context}


Question:

{question}


If the answer is not available,
say:

"I couldn't find that information in the uploaded PDF."

"""


    response = client.models.generate_content(

        model="gemini-2.0-flash",

        contents=prompt

    )


    return response.text