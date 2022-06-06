from statistics import median
from nltk.text import Text
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt

# Load the words of Don Quijote
corpus_root = "C:/Users/visa4/OneDrive/Desktop/Spanish Senior Showcase Project"
don_quijote_corpus_reader = PlaintextCorpusReader(corpus_root, '.*')
don_quijote_text = Text(don_quijote_corpus_reader.words('Don Quijote Text.txt'))

# Linguistic Dispersion Plot
def linguistic_dispersion_plot():
    targets = ["Quijote", "Sancho", "Cervantes", "Capítulo", "duque", "sobrina"]
    don_quijote_text.dispersion_plot(targets)

# How many times does the future subjunctive appear
def future_subjunctive_analysis():    
# I can't figure out how to deal with edge cases like "lugares" without having a dictionary of nouns)
    don_quijote_words = list(word.lower() for word in don_quijote_text if word.isalpha())
    subjunctive_words = [word for word in don_quijote_words if not word.startswith("quier") and
                        ((word.endswith("are") or word.endswith("ares") or word.endswith("aremos") or word.endswith("areis") or word.endswith("aren")) or 
                        (word.endswith("iere") or word.endswith("ieres") or word.endswith("ieremos") or word.endswith("iereis") or word.endswith("ieren"))
                        )]

    print(subjunctive_words)

# Sentence length analyzer (includes punctuation in count; sentences are only ended with periods, so interrupting dialogue is considered part of the sentence)
def sentence_length_analysis():
    don_quijote_sentences = don_quijote_corpus_reader.sents()
    y_values = [len(don_quijote_sentences[i]) for i in range(0, len(don_quijote_sentences))]

    mid_index = int(len(y_values)/2)
    print(median(y_values[:mid_index]))
    print(median(y_values[mid_index:]))

    plt.title("Palabras/punctuación en cada oración")
    plt.plot(y_values, linewidth=1)
    plt.show()

sentence_length_analysis()