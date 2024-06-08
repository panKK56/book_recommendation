import numpy as np
# from src.exception import CustomException
import sys



def fetch_poster(suggestion,book_pivot,final_rating):
    # try: 
        book_name=[]
        ids_index=[]
        poster_url=[]

        for book_id in suggestion:
            book_name.append(book_pivot.index[book_id])

        for name in book_name[0]:
            ids=np.where(final_rating['book_title']==name)[0][0]
            ids_index.append(ids)

        for idx in ids_index:
            url=final_rating.iloc[idx]['image_url_l']
            poster_url.append(url)
        
        return poster_url
    # except Exception as e:
        # raise CustomException(sys,e)


def recommend_books(book_name,book_pivot,model,final_rating):
    # try:
        book_list=[]
        book_id=np.where(book_pivot.index == book_name)[0][0]
        distance,suggestion=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)

        poster_url=fetch_poster(suggestion,book_pivot,final_rating)

        for i in range(len(suggestion)):
            books=book_pivot.index[suggestion[i]]
            for j in books:
                book_list.append(j)
        return book_list,poster_url
    # except Exception as e:
        # raise CustomException(sys,e)
    