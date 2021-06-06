from sentence_transformers import SentenceTransformer
import numpy as np
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

def euclidean(testList, patternIdx):

    result = []
    for i in range(len(testList)):
        patternIdx = patternIdx - 1
        sentences = [testList[i]["processed"],testList[patternIdx]["processed"]]
        # (1) 이용하여 임베딩
        sentence_embeddings = model.encode(sentences)
        # (2)거리 구하는 공식을 적용
        result.append(np.dot(sentence_embeddings[0],sentence_embeddings[1])/(np.linalg.norm(sentence_embeddings[0])*np.linalg.norm(sentence_embeddings[1])))
    
    for i in range(len(testList)):
        testList[i]["similarity"] = result[i] 
            

    return testList

