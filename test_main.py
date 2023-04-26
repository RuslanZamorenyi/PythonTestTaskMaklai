
from main import get_paraphrase
import pytest


def test_get_paraphrase():
    data = "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) " \
             "(NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) " \
             "(VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) " \
             "(CC and) (NP (JJ Catalan) (NNS estaurants) ) ) ) ) ) ) )"
    # right test
    func = get_paraphrase(data, 3)
    assert type(func) == list
    assert len(func) == 3
    assert func is not None
    # failed test
    first_data = "ruslan"
    func = get_paraphrase(first_data, -5)
    second_data = 4
    three_data = {"Ruslan": "Zamorenyi"}
    assert func == "problem with your limit data please check and repeat again"
    with pytest.raises(ValueError, match="problem with your data please check and repeat again"):
        get_paraphrase(second_data, 6)
    with pytest.raises(ValueError, match="problem with your data please check and repeat again"):
        get_paraphrase(three_data, 'ha')




