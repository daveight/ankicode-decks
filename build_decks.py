# Copyright: Daveight and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
import os


def encode_csv(text: str):
    """
    Encodes text for CSV format
    :param text: target text
    :return: encoded text
    """
    text = text.replace('"', '""')
    return text


def get_file_content(path: str):
    """
    Reads file content by path
    :param path: file location path
    :return: file text content
    """
    f = None
    try:
        with open(path, "r") as f:
            return f.read()
    except OSError:
        return None
    finally:
        if f is not None:
            f.close()


SOLUTION_SECTIONS = [['header', ''], ['java', 'Java'], ['cpp', 'C++'], ['js', 'JavaScript'], ['python', 'Python']]

for deck_name in [item for item in os.listdir('.') if os.path.isdir(os.path.join('.', item))]:
    out = ''
    deck_name = './' + deck_name
    try:
        for name in sorted(os.listdir(f'{deck_name}/test_cases')):
            if not name.endswith('.tsv'):
                continue
            file = open(f'{deck_name}/test_cases/' + name, 'r')
            lines = file.readlines()

            name = name.replace('.tsv', '')
            description = get_file_content(f'{deck_name}/descriptions/' + name)
            if description is None:
                print('can\'t find description for ' + name)
                break

            title = get_file_content(f'{deck_name}/titles/' + name)
            if title is None:
                print('can\'t find title for ' + name)
                break

            func_name = get_file_content(f'{deck_name}/fn_names/' + name)
            if not func_name:
                print('can\'t find func name for ' + name)
                break

            solution = ''
            for section in SOLUTION_SECTIONS:
                txt = get_file_content(f'{deck_name}/solutions/{section[0]}/{name}')
                if not txt:
                    print(f'can\'t find {section[0]} solution for {name}')
                    break
                if section[1]:
                    solution += '### ' + section[1] + '\n'
                solution += txt + '\n'

            out += '"' + encode_csv(title.strip()) + '"' + '\t'
            out += '"' + encode_csv(description.strip()) + '"' + '\t'
            out += '"' + func_name.strip() + '"' + '\t'
            out += '"' + encode_csv(solution.strip()) + '"' + '\t'
            out += '"'

            for i, line in enumerate(lines):
                out += encode_csv(line)
            out += '"'
            out += '\n'

            result = open(f'{deck_name}.csv', 'w+')
            result.write(out)
            result.close()
    except FileNotFoundError:
        pass
