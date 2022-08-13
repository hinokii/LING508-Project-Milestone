# Word Info

You can obtain the information of a Japanese word or Korean word including the english translation, the Korean or Japanese translation (for a Japanese or Korean word, respectively), Part of Speech and TFIDF. Enter a Japanese or Korean word in the box, select a language (Japanese or Korean) from Radio button and click "Submit". The page will display the parse for that word as a JSON string, for example

For a Japanese word "渡櫓":

    "english": "Tower",
    "korean": "탑",
    "pos": "['Noun']",
    "tfidf": 0.347134,
    "word": "渡櫓"


For a Korean word "단일화":

    "english": "Unification",
    "japanese": "統一",
    "pos": "['Modifier', 'Noun']",
    "tfidf": 0.179157,
    "word": "단일화"


The API can be called directly without the UI, using a POST request (Postman). The endpoint is http://localhost:5000/post/. The POST request must contain a JSON body with the "word" key, for example {"word": "세율"}

Also, you can go to http://127.0.0.1:5000 or http://10.0.2.15:5000 and input the word to get the same information for the word entered. 