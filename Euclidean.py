'''
#from sentence_transformers import SentenceTransformer
import numpy as np

def bow(sentence):
      #(1) 입력받은 문장을 단어 단위로 쪼갠 뒤, 중복을 제거해﻿줍니다.
  word_list = sentence.split(' ')
  word_list = list(set(word_list))
  #(2) 단어의 수만큼 배열을 만들고, 0으로 채워﻿줍니다.
  embedding_matrix = [0 for element in range(len(word_list))]
  #(3) 각 인덱스의 단어가 몇 번 나오는지 count한뒤, 갱신해﻿줍니다.
  for index, word in enumerate(word_list):
    embedding_matrix[index] = sentence.count(word)
  return embedding_matrix

sent1 = "안녕 벤틀리 나는 윌리엄."
sent2 = "안녕 벤틀리 너는."

def euclidean(sent1, sent2):
  sentences = [sent1,sent2]
   # (1) 이용하여 임베딩
  sentence_embeddings1 = bow(sent1)
  sentence_embeddings2 = bow(sent2)
  #  (2)거리 구하는 공식을 적용
  result = 0
  for i in range(len(sentence_embeddings1)):
      result += np.sum((sentence_embeddings1[i]-sentence_embeddings2[i])**2)
  result = np.sqrt(result)
  if result == 0:
    result = 1
  else:
    result = 1 / result

  return result

result = euclidean(sent1,sent2)
print("Euclidean Similarity : ",result)
'''
from sentence_transformers import SentenceTransformer
import numpy as np

sent1 = "안녕 벤틀리 나는 윌리엄."
sent2 = "안녕 벤틀리 나는 윌리엄."
model = SentenceTransformer('paraphrase-distilroberta-base-v1')

def euclidean(sent1, sent2):
  sentences = [sent1,sent2]
   # (1) 이용하여 임베딩
  sentence_embeddings = model.encode(sentences)
  #  (2)거리 구하는 공식을 적용
  result = np.sqrt(np.sum((sentence_embeddings[0]-sentence_embeddings[1])**2))
  if result == 0:
    result = 1
  else:
    result = 1 / result

  return result

result = euclidean(sent1,sent2)
print("Euclidean Similarity : ",result)