import re

def preprocess_text(text):
    clean_text = re.sub(r'\s+', '', text)
    clean_text = re.sub(r'[^\w\s]', '', clean_text)
    return clean_text

def calc_sentence_importance(sentence, word_frequency):
    words = sentence.split()
    importance = sum(word_frequency.get(word, 0) for word in words)
    return importance

def generate_summary(text, num_sentences):
    clean_text = preprocess_text(text)
    sentences = clean_text.split('.')
    word_frequency = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

    sentence_scores = [(sentence, calc_sentence_importance(sentence, word_frequency)) for sentence in sentences]
    sorted_sentence = sorted(sentence_scores, key=lambda x: x[1], reverse = True)  
    top_sentence = sorted_sentence[:num_sentences]           
    summary = ".".join(sentence for sentence, score in top_sentence)
    return summary

if __name__ =="__main__":
    input_text = input ("Enter the text to summarize:")

    num_sentence_summary = 3

    summary = generate_summary(input_text, num_sentence_summary)
    print("\nsummary:")
    print(summary)