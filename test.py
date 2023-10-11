from character import edit_distance
from word import word_edit_distance,word_edit_distance_by_str

def test_word1():
    gt = "私 は 無能 で あろうか"
    test = "私 は 誰 だ"
    gt_word_list = gt.split()
    test_list = test.split()
    distance, replace, insert, delete, error_rate = word_edit_distance(test_list,gt_word_list)

    assert distance == 3
    assert replace == 2
    assert insert == 1
    assert delete == 0
    assert error_rate == 0.75

def test_word2():
    gt = "たこやき が 食べ"
    test = "たい焼き が 食べ たい"
    gt_word_list = gt.split()
    test_list = test.split()
    distance, replace, insert, delete, error_rate = word_edit_distance(test_list,gt_word_list)

    assert distance == 2
    assert replace == 1
    assert insert == 0
    assert delete == 1
    assert error_rate == 0.5

def test_word3():
    gt = "たこやき が 食べ"
    test = "たい焼き が 食べ たい"
    distance, replace, insert, delete, error_rate = word_edit_distance_by_str(test,gt)

    assert distance == 2
    assert replace == 1
    assert insert == 0
    assert delete == 1
    assert error_rate == 0.5

def test_char1():
    test = "ういろう"
    gt = "いんこ"
    distance, replace, insert, delete, error_rate = edit_distance(test,gt)

    assert distance == 3
    assert replace == 2
    assert insert == 0
    assert delete == 1
    assert error_rate == 0.75

def test_char2():
    test = "たんし"
    gt = "たんぱくしつ"
    distance, replace, insert, delete, error_rate = edit_distance(test,gt)

    assert distance == 3
    assert replace == 0
    assert insert == 3
    assert delete == 0
    assert error_rate == 1

def test_char3():
    gt = "ちからうどん"
    test = "からげんき"
    distance, replace, insert, delete, error_rate = edit_distance(test,gt)

    assert distance == 4
    assert replace == 1
    assert insert == 2
    assert delete == 1
    assert error_rate == 0.8

def test_char4():
    test = "あ、い、う。"
    gt = "あいう"
    distance, replace, insert, delete, error_rate = edit_distance(test,gt,is_remove=True)

    assert distance == 0
    assert replace == 0
    assert insert == 0
    assert delete == 0
    assert error_rate == 0

def test_char5():
    test = "あ、い、う。"
    gt = "あいう"
    distance, replace, insert, delete, error_rate = edit_distance(test,gt,is_remove=False)

    assert distance == 3
    assert replace == 0
    assert insert == 0
    assert delete == 3
    assert error_rate == 0.5
