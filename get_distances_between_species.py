#!/usr/bin/env python
# coding: utf-8


# Constructing DataFrame to use as an input for get_distances_between_species function.
def construct_DataFrame(not_novel, not_novel_species, novel, novel_species):
    not_novel = pd.DataFrame(not_novel)
    not_novel['species'] = not_novel_species
    not_novel_species = np.unique(not_novel_species)
    
    novel = pd.DataFrame(novel)
    novel['species'] = novel_species
    novel_species = np.unique(novel_species)
        
    return not_novel, not_novel_species, novel, novel_species


class Distances:
    def __init__(self,
                 not_novel,
                 not_novel_species,
                 novel, 
                 novel_species,
                 distance):
        self.not_novel = not_novel
        self.not_novel_species = not_novel_species
        self.novel = novel
        self.novel_species = novel_species
        self.distance = distance

    def get_distances_between_species(self):
        d = [] # contain mean of distances between not novel species i and novel species j
        ns = [] # contain novel species label
        nns = [] # contain not novel species
        
        not_novel, not_novel_species, novel, novel_species = construct_DataFrame(self.not_novel, 
                                                                                 self.not_novel_species,
                                                                                 self.novel, 
                                                                                 self.novel_species)
    
        for i in not_novel_species:
            for j in novel_species:
                # calculate distance between not novel species i and novel species j
                between_dist = pairwise_distances(novel.loc[novel.species == j, :].iloc[: , :-3],
                                                  not_novel.loc[not_novel.species == i, :].iloc[: , :-3],
                                                  metric = self.distance)
                d.append(np.mean(between_dist))
                nns.append(i)
                ns.append(j)

        # create dataframe of output
        op_metric = pd.DataFrame({'Novel Species':ns,
                                  'Not Novel Species':nns, 
                                  'Mean of Distance':d})
        return op_metric


d = Distances(not_novel, 
              not_novel_species, 
              novel, 
              novel_species, 
              distance='cosine')
d.get_distances_between_species()