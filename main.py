import spacy
from flask import Flask, request, jsonify

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")


def get_paraphrase(get_tree_for_change, limit):
    """
    Function for permutations noun phrases, without changing the meaning.

        Parameters:
            get_tree_for_change (str): A tree for do change
            limit (int): limit change

        Returns:
            paraphrases (list): changed syntax trees
    """
    if isinstance(get_tree_for_change, str) and len(get_tree_for_change) > 0:
        bild_tree = nlp(get_tree_for_change)

        # search noun phrases
        np_item_list = []
        for np_item in bild_tree.noun_chunks:
            if ',' in np_item.text or 'and' in np_item.text or 'or' in np_item.text:
                np_item_list.append(np_item)

        # generation of interruptions noun phrases
        paraphrases = []
        for np in np_item_list:
            noun_phrases = np.text.split(',')
            if len(noun_phrases) > 1:
                permutation_list = [[noun_phrases[i]] for i in range(len(noun_phrases))]
                for x in range(len(noun_phrases)):
                    for y in range(len(permutation_list)):
                        if noun_phrases[x] not in permutation_list[y]:
                            new_list_for_permutation = permutation_list[y].copy()
                            new_list_for_permutation.insert(x, noun_phrases[x])
                            permutation_list.append(new_list_for_permutation)
                for item in permutation_list:
                    new_text = ' '.join([w.text for w in bild_tree if w not in np] + item)
                    paraphrases.append(new_text)
    else:
        raise ValueError("problem with your data please check and repeat again")
    if int(limit) > 0:
        paraphrases = paraphrases[:int(limit)]
        return paraphrases
    else:
        return "problem with your limit data please check and repeat again"


@app.route('/paraphrase', methods=['GET'])
def get_data():
    get_tree_for_change = request.headers.get('data')
    limit = request.headers.get('paraphrasing_limit')
    result = get_paraphrase(get_tree_for_change, limit)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="localhost")
