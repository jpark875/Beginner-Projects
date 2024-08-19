def get_questions(filename):
    question_count = {}
    symbols = '.?!;:,\'"'

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        # If utf-8 fails, try a different encoding
        with open(filename, 'r', encoding='ISO-8859-1') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

    words = text.split()

    for word in words:
        word = word.lower()
        for symbol in symbols:
            word = word.replace(symbol, '')

        if word.endswith('ko') or word.endswith('kö'):
            if word in question_count:
                question_count[word] += 1
            else:
                question_count[word] = 1

    return question_count

print(get_questions('example1.txt')) #sample code