#!/usr/bin/env python
# coding: utf-8

# In[1]:

import Untitled3
import pandas as pd
from array import *

from pandas import DataFrame
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

df_ratings = pd.read_csv('dell_ratings.csv')
df_services = pd.read_csv('dell_services.csv')


# In[3]:


# df_ratings.head()


# In[4]:

def clean_data(df_ratings, product):
    df_ratings.drop(['Hardware Issue', 'Software Issue', 'Tickets Raised'], axis=1, inplace=True)
    df_ratings = df_ratings[df_ratings['Product type'] == product]
    df_ratings.drop(['Product type'], axis=1, inplace=True)
    # df_serv_count = pd.DataFrame(df_ratings.groupby('serviceID').size(), columns=['count'])
    # df_user_count = pd.DataFrame(df_ratings.groupby('UserID').size(), columns=['count'])

    # list_of_idx = list(df_user_count.index.values)

    df_ratings_sorted = df_ratings.sort_values(by=['user_rating'], ascending=True)
    df_ratings_sorted = df_ratings_sorted.sort_values(by=['UserID', 'serviceID'], ascending=True)
    # df_ratings_sorted.tail(20)

    df_ratings_drop = df_ratings_sorted.drop_duplicates(['UserID', 'serviceID'], keep='last')

    df_service_features = df_ratings_drop.pivot(index='UserID', columns='serviceID', values='user_rating').fillna(0)

    df_serv_cnt: DataFrame = pd.DataFrame(df_ratings_drop.groupby('serviceID').size(), columns=['count'])
    popularity_thres = 6
    popular_services = list(set(df_serv_cnt.query('count >= @popularity_thres').index))

    df_ratings_drop_services = df_ratings_drop[df_ratings_drop.serviceID.isin(popular_services)]

    df_users_cnt = pd.DataFrame(df_ratings_drop_services.groupby('UserID').size(), columns=['count'])

    ratings_thres = 4
    active_users = list(set(df_users_cnt.query('count >= @ratings_thres').index))
    df_ratings_drop_users = df_ratings_drop_services[df_ratings_drop_services.UserID.isin(active_users)]
    # print('shape of original ratings data: ', df_ratings_drop.shape)
    # print('shape of ratings data after dropping both unpopular services and inactive users: ', df_ratings_drop_users.shape)
    return df_ratings_drop_users


def create_matrix(df_ratings_clean):
    service_user_mat = df_ratings_clean.pivot(index='UserID', columns='serviceID', values='user_rating').fillna(0)
    df_services.drop(['service_rating (avg)'], axis=1, inplace=True)
    service_to_idx = {
        service: i for i, service in
        enumerate(list(df_services.set_index('serviceID').loc[service_user_mat.columns].service_name))
    }
    # print(service_to_idx)

    service_user_mat_sparse = csr_matrix(service_user_mat.values.transpose())
    return service_user_mat_sparse, service_to_idx


def apply_knn(mat_sparse):
    # define model
    model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)
    # fit
    model_knn.fit(mat_sparse)
    return model_knn


def matching(mapper, service_used):
    # get match
    match_tuple = []
    for service_name, idx in mapper.items():
        if service_name == service_used:
            match_tuple.append((service_used, idx))
    return match_tuple[0][1]

# In[164]:

'''
data = service_user_mat_sparse
idx = matching(service_to_idx, 'S3')
print(idx)
print(data[idx])
'''

# In[165]:

'''
distances, indices = model_knn.kneighbors(data[idx], n_neighbors=5)
print(distances)
print(indices)
'''

def make_recommendation(model_knn, data, mapper, service_used, n_recommendations):
    model_knn.fit(data)
    # get input movie index
    print('You have input service:', service_used)
    idx = matching(mapper, service_used)

    print('Recommendation system start to make inference')
    print('......\n')
    distances, indices = model_knn.kneighbors(data[idx], n_neighbors=n_recommendations + 1)

    raw_recommends = sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[
                     :0:-1]
    # get reverse mapper
    reverse_mapper = {v: k for k, v in mapper.items()}
    # print recommendations
    print('Recommendations for {}:'.format(service_used))

    for i, (idx, dist) in enumerate(raw_recommends):
        print('{0}: {1}, with distance of {2}'.format(i + 1, reverse_mapper[idx], dist))
    #array1 = array('i', [])


def main():
    x=input("enter the service such as  S1:__")
    my_favourite = x
    n_recommendations = 3
    df_clean = clean_data(df_ratings,"Laptop")
    data, mapper = create_matrix(df_clean)
    model_knn = apply_knn(data)
    make_recommendation(model_knn,data,mapper,my_favourite,n_recommendations)
    Untitled3.main()




if __name__ == "__main__" :
    main()


'''
my_favorite = 'S7'

make_recommendation(
    model_knn=model_knn,
    data=service_user_mat_sparse,
    service_used=my_favorite,
    mapper=service_to_idx,
    n_recommendations=3)
'''
# In[ ]:
