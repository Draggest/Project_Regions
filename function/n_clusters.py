import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score

# Функция локтя для поиска оптимального кол-ва кластеров
def elbow(data):
    def get_inertia(cluster_num, X):
        k_means =  KMeans(n_clusters=cluster_num,n_init=10, random_state=42)
        k_means.fit(X)
        inertia = k_means.inertia_
        return inertia

    res = {"inertia": [], "cluster": []}

    X = data.drop(['Region'],axis=1)

    for cluster_num in range(1, 10):
        res["inertia"].append(get_inertia(cluster_num, X))
        res["cluster"].append(cluster_num)

    res_df = pd.DataFrame(res)

    sns.set_style("darkgrid")
    sns.lineplot(data=res_df, x="cluster", y="inertia", marker= "o")
    return None

# Функция силуэта для поиска оптимального кол-ва кластеров
def silhouette(data):
    def get_silhouette(cluster_num, X):
        kmeans =  KMeans(n_clusters=cluster_num, init='k-means++', n_init=10, random_state=42)
        kmeans.fit(X)
        silhouette = silhouette_score(X, kmeans.predict(X))
        return silhouette

    silhouette_res = {"silhouette": [], "cluster": []}
    
    X = data.drop(['Region'],axis=1)

    for cluster_num in range(2, 10):
        silhouette_res["silhouette"].append(get_silhouette(cluster_num, X))
        silhouette_res["cluster"].append(cluster_num)
        
    silhouette_df = pd.DataFrame(silhouette_res)
    sns.set_style("darkgrid")
    sns.lineplot(data=silhouette_df, x="cluster", y="silhouette", marker= "o")
    return None