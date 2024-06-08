import pandas as pd 
import numpy as np
import pickle
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

final_rating=pd.read_csv(r'notebook\data\final_rating.csv',encoding='latin-1')
book_pivot=final_rating.pivot_table(columns='user_id',index='book_title',values='num_rating')
book_pivot.fillna(0,inplace=True)
book_sparse=csr_matrix(book_pivot)

# Building model
model=NearestNeighbors(algorithm='brute')
model.fit(book_sparse)

books_name=book_pivot.index

pickle.dump(model,open('artifacts/model.pkl','wb'))
pickle.dump(books_name,open('artifacts/books_name.pkl','wb'))
pickle.dump(final_rating,open('artifacts/final_rating.pkl','wb'))
pickle.dump(book_pivot,open('artifacts/book_pivot.pkl','wb'))


