from sentence_transformers import SentenceTransformer
import numpy as np
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

def euclidean(testList, patternIdx):
    for i in range(len(testList)):
        patternIdx = patternIdx - 1
        sentences = [testList[i]["processed"],testList[patternIdx]["processed"]]
        # (1) 이용하여 임베딩
        sentence_embeddings = model.encode(sentences)
        # (2)거리 구하는 공식을 적용
        result = np.sqrt(np.sum((sentence_embeddings[0]-sentence_embeddings[1])**2))
        if result == 0:
            result = 1
        else:
            result = 1 / result
        testList[i]["similarity"] = result
    return testList

