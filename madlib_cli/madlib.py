import re
def wlcm_msg():
    print("""Welcome to madlib game!\nyou just need to write simple things """)


game_input_words = ['Adj', 'Adj', 'Name', 'Past Tense ', 'Name', 'Adj', 'Adj',
            'Plural Noun', 'L-size Animal', 'S-size Animal', "Female Name", 'Adj', 'Plural Noun', 'Adj', 'Plural Noun',
            'Number[1to50]', 'Name', 'Number', 'Plural Noun', 'Number', 'Plural Noun']
user_input = []


def enter_word():
    for i in range(len(game_input_words)):
        input_val = input('>> Enter %s  ' % (game_input_words[i]))
        user_input.append(input_val)


def read_template(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('The file not found')


def parse_template(text):
    edited = re.sub('{[^}]+}', '{}', text)
    text_rm = tuple(re.findall("{(.*?)}", text))
    return edited, text_rm


def merge(parsed, user_input):
    return parsed.format(*user_input)


def copying(merged):
    with open('./assets/copying.txt', 'wb') as write_copying:
        return write_copying.write(bytes(merged, 'utf-8'))

if __name__ == '__main__':
    wlcm_msg()
    enter_word()
    with open('assets/make_me_a_video_game_template.txt', 'r') as file:
        text = file.read()
    text = re.sub(r"\{(.*?)\}", "{}", text)
    for word in user_input:
        text = text.replace("{}", word, 1)
    with open('assets/game_results.txt', 'w') as file:
        file.write(text)
    print(" this is your input ")
    print(text)
