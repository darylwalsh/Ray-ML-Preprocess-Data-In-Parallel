import json
import os

import nltk
import ray
from bs4 import BeautifulSoup
from transformers import AutoTokenizer

news_path = os.path.join(".", "news_files")
enc_path = os.path.join(".", "news_encoded")


@ray.remote
def store_encoding(fname: str, category: str, tokenizer):
    with open(os.path.join(news_path, category, fname)) as f:
        content = BeautifulSoup(f.read(), "html.parser")
        txt = content.text

        sentences = nltk.sent_tokenize(txt)

        enc = tokenizer(sentences, max_length=500, padding=True,
                        truncation=True)['input_ids']

    with open(os.path.join(enc_path, category, fname.replace("html", "json")), "w") as f:
        json.dump(enc, f)
    return 1


def main():
    tkzrs = []
    for i in range(4):
        tkzrs.append(AutoTokenizer.from_pretrained('bert-base-cased'))
    if not os.path.exists(enc_path):
        os.makedirs(enc_path)

    categories = [fd for fd in os.listdir(news_path) if os.path.isdir(
        os.path.join(news_path, fd))]

    for category in categories:
        if not os.path.exists(os.path.join(enc_path, category)):
            os.makedirs(os.path.join(enc_path, category))

    res = []
    for ctegory in categories:
        fls = os.listdir(os.path.join(news_path, ctegory))
        for f in fls:
            ref = store_encoding.remote(f, ctegory, tkzrs[i%4])
            res.append(ref)
            i += 1

    for r in res:
        ray.get(r)


if __name__ == '__main__':
    ray.init(num_cpus=8, dashboard_port=8265)
    main()
