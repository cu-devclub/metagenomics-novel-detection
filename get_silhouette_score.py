#!/usr/bin/env python
# coding: utf-8


class Scores:
    def get_silhouette_score(self, 
                             train_embed, 
                             test_embed, 
                             n_samples, 
                             distance):
        self.train_embed = train_embed
        self.test_embed = test_embed
        self.n_samples = n_samples
        self.distance = distance
        
        # merge train and test embedding
        merged_embed = np.concatenate((train_embed, test_embed), axis=0)
    
        # feed merged embedding to HDBSCAN and extract clusters labels
        clusterer = hdbscan.HDBSCAN(min_cluster_size=round(n_samples/2), metric=distance)
        cluster_labels = clusterer.fit_predict(merged_embed)
    
        # calculate silhouette score
        score = silhouette_score(merged_embed, cluster_labels)
    
        return score