# Word Info

You can obtain the information of a Japanese word or Korean word including english translation, Korean or Japanese translation, pos and TFIDF. Enter a Japanese or Korean word in the box, select a language (Japanese or Korean) from Radio button and click "Submit". The page will display the parse for that word as a JSON string, for example

For a Japanese word "天守":


    "english": "Housing",
    "japanese": "ハウジング",
    "pos": "['Noun']",
    "tfidf": 0.297862,
    "word": "주택"


For a Korean word "주택":


    "english": "Housing",
    "japanese": "ハウジング",
    "pos": "['Noun']",
    "tfidf": 0.297862,
    "word": "주택"


The API can be called directly without the UI, using a POST request (Postman). The endpoint is http://localhost:5000/post/. The POST request must contain a JSON body with the "word" key, for example {"word": "세율"}

Also, you can go to http://127.0.0.1:5000 or http://10.0.2.15:5000 and input the word to get the same information for the word entered. 