import gensim
from gensim.models import KeyedVectors
import pandas as pd

class WordEmbedding:
    def __init__(self, embedding_file, limit=1000000):
        self.wv = self.load_word2vec_embeddings(embedding_file, limit)

    def load_word2vec_embeddings(self, location, limit):
        wv = KeyedVectors.load_word2vec_format(location, binary=True, limit=limit)
        return wv

    def save_as_csv(self, output_file):
        self.wv.save_word2vec_format(output_file)

    def calculate_similarity(self, phrase1, phrase2, method='cosine'):
        # Implement similarity calculation using word embeddings
        pass

def main():
    embedding_file = '/Users/aasthamalhotra/Downloads/GoogleNews-vectors-negative300.bin'
    phrases_file = '/Users/aasthamalhotra/Downloads/DE assessment/phrases (1).csv'
    word_embedding = WordEmbedding(embedding_file)
    word_embedding.save_as_csv('vectors.csv')  # Convert and save the embeddings as CSV

    # Load phrases from CSV and calculate similarities
    phrases_df = pd.read_csv(phrases_file)
    for _, row in phrases_df.iterrows():
        phrase1 = row['phrase1']
        phrase2 = row['phrase2']
        similarity = word_embedding.calculate_similarity(phrase1, phrase2)
        # print(f"Similarity between '{phrase1}' and '{phrase2}': {similarity}")

if __name__ == "__main__":
    main()
