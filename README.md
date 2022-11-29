# metagenomics-novel-detection
This package we provide you functions for analysing k-mer frequency profiles with 2 purposes.
  1) Comparing raw sequences with embedding sequences derived from existing deep learning based taxonomic classification models.
  2) Detecting novel species that are not in the reference database.
  
### Distances betweeen species
A function to calculate distances between known species and unknown species (know what is unknown). 
  - Input is known nad unknown features (k-mer frequency profiles), its labels (species ids), and type of distance using to calculate.
  - Output is a DataFrame containing mean of distances between known and unknown species.  
  
.. code:: python  

    class Distances:  
      def __init__(self, not_novel, not_novel_species, novel, novel_species, distance):  
        self.not_novel = not_novel  
        self.not_novel_species = not_novel_species  
        self.novel = novel  
        self.novel_species = novel_species  
        self.distance = distance  

      def get_distances_between_species(self):  
        d = [] # contain mean of distances between not novel species i and novel species j  
        ns = [] # contain novel species label  
        nns = [] # contain not novel species  
    
        for i in not_novel_species:
          for j in novel_species:
            # calculate distance between not novel species i and novel species j
            between_dist = pairwise_distances(self.novel.loc[self.novel.species == j, :].iloc[: , :-3],
                                              self.not_novel.loc[self.not_novel.species == i, :].iloc[: , :-3],
                                              metric = self.distance)
            d.append(np.mean(between_dist))
            nns.append(i)
            ns.append(j)

        # create dataframe of output
        op_metric = pd.DataFrame({'Novel Species':ns, 'Not Novel Species':nns, 'Mean of Distance':d})
        return op_metric  
        
The paarameters that can be set for this function are listed as follows:
-  ``not_novel``: This is the features (k-mer frequency profiles) for known species.
-  ``not_novel_species``: This is the lebels (species labels) for known species.
-  ``novel``: This is the features (k-mer frequency profiles) for unknown species.
-  ``novel_species``: This is the lebels (species labels) for unknown species.
-  ``distance``: This is the metric used to calculate distances between species.
 
