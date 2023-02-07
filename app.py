import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("MY_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        book = request.form["book"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(book),
            temperature=1,
            max_tokens=3080,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(book):
    return """Summerize the given book.

Book: The Theory of Everything
Summary: The Theory of Everything is a 2014 biographical drama film that is based on the life of Stephen Hawking, the world-renowned physicist, and cosmologist. The film explores his life, including his experiences with motor neuron disease and his relationship with his wife Jane Wilde. The movie covers the major events of Hawking's life, including his study at the University of Cambridge, his groundbreaking work on black holes and the theory of general relativity, and his rise to fame. It also focuses on the challenges he faced both professionally and personally, including his health issues and the strain it put on his marriage. Overall, The Theory of Everything is a portrayal of Stephen Hawking's life, his achievements, and his impact on the scientific world.
Book: The Fault in Our Stars
Summary: "The Fault in Our Stars" is a young adult novel by John Green that was published in 2012. The story is a love story between two teenagers, Hazel Grace Lancaster and Augustus Waters, who meet at a cancer support group. Despite their struggles with illness, the two fall in love and embark on an unforgettable journey together.

The book explores themes of love, loss, and the human condition, and it challenges readers to consider the meaning of life and death. The novel is known for its beautiful and heart-wrenching narrative, and it has touched the hearts of millions of readers around the world.

In summary, "The Fault in Our Stars" is a powerful and emotional story about two teens who find love in the face of illness and death.
Book: {}
Summary:""".format(
        book.capitalize()
    )
