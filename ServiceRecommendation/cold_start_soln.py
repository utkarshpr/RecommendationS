#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd


# In[25]:


df_ratings = pd.read_csv('dell_ratings.csv')
df_serv = pd.read_csv('dell_services.csv')

# In[26]:


#df_ratings.head()


# In[27]:

def popular_services(df_ratings,product):
    df_ratings.drop(['Hardware Issue','Software Issue','Tickets Raised'],axis=1,inplace=True)
    df_ratings = df_ratings[df_ratings['Product type']== product]
    df_ratings.drop(['Product type'],axis=1,inplace=True)


    df_serv_count = pd.DataFrame(df_ratings.groupby('serviceID').size(),columns = ['count'])
    mean = df_serv_count.mean(axis =0)
    mean =int(mean)

    popularity_thres = mean
    popular_services = list(set(df_serv_count.query('count >= @popularity_thres').index))
    df_ratings_drop_services = df_ratings[df_ratings.serviceID.isin(popular_services)]


    #df_users_cnt = pd.DataFrame(df_ratings_drop_services.groupby('UserID').size(), columns=['user_rating'])

    df_service = df_ratings.filter(['serviceID','user_rating'], axis=1)
    df_service =df_service.rename(columns ={"user_rating":"service_rating(avg)"})
    df_service_mean = df_service.groupby('serviceID').mean().reset_index()
    df_service_mean = df_service_mean.sort_values(by=['service_rating(avg)'],ascending = False)



    pop_service_index = list(df_service_mean.serviceID[0:3])
    pop_service_index
    print("recommended services:")
    for i in pop_service_index:
        print(df_serv.service_name[i-1])

def main():
    product = "Laptop"
    popular_services(df_ratings,product)

if __name__ == "__main__":
    main()
