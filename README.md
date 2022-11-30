# Metagenomics-novel-detection
This package we provide you functions for analysing k-mer frequency profiles with 2 purposes.  
1) Comparing raw sequences with embedding sequences derived from existing deep learning based taxonomic classification models.  
2) Detecting novel species that are not in the reference database.
  
## API Reference

### Distances between species

```python
get_distances_between_species()
```
A function for calculating distances between unknown species and known species (know what is unknown). 
  - Input is unknown and known features (k-mer frequency profiles), its labels (species ids), and type of distance used to calculate.
  - Output is a DataFrame containing mean of distances between unknown and known species.  

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `not_novel` | `array` | The features (k-mer frequency profiles) for known species. |
| `not_novel_species` | `array` | The lebels (species labels) for known species. |
| `novel` | `array` | The features (k-mer frequency profiles) for unknown species. |
| `novel_species` | `array` | The lebels (species labels) for unknown species. |
| `distance` | `String` | The distance metric used to calculate distances between species. |

#### How to use this function
Takes two dataset of species (features and labels of both known and unknown) and returns the DataFrame containing pair-wise distances between unknown and known species.
```python
d = Distances(not_novel, not_novel_species, novel, novel_species, distance)
d.get_distances_between_species()
```

An example of output from this function.
| Novel Species | Not Novel Species  | Mean of Distances  |
| :------------ | :----------------- | :----------------- |
| 1085644 |	1270    |	0.941044 |
| 1085644 | 2021    |	0.905730 |
| 1085644 |	28104   |	0.873885 |
| 1085644 |	29581 	| 0.861263 |
| 1085644 |	33028 	| 0.532799 |
| 1085644 |	115561  |	0.759104 |
| 1085644 |	153493  |	0.728929 |
| 1085644 |	154288  |	0.553854 |
| 1085644 |	180957  | 0.748921 |
| 1085644 |	485870  |	0.871557 |
| 1085644 |	485898  |	0.849495 |

According to this output:
  - The species '1270' (known) has the furthest dtistance away from species '1085644' (unknown).
  - The species '33028' (known) has the closest distance to species '1805644' (unknown).

