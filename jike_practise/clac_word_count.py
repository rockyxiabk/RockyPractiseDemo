import re

COUNT_SIZE = 100


def parse_to_word_list(text, last_word, word_list):
    text = re.sub(r'[^\w ]', ' ', last_word + text)
    text = text.lower()
    cur_word_list = text.split(' ')
    cur_word_list, last_word = cur_word_list[:-1], cur_word_list[-1]
    word_list += filter(None, cur_word_list)
    return last_word


def solve():
    with open('in.txt', 'r') as fin:
        word_list, last_word = [], ''
        while True:
            text = fin.read(COUNT_SIZE)
            if not text:
                break  # 读取完毕，中断循环
            last_word = parse_to_word_list(text, last_word, word_list)

        word_cnt = {}
        for word in word_list:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1

        sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
        sorted_word_cnt.sort()
        return sorted_word_cnt
