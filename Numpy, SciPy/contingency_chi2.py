import pandas as pd
from scipy.stats import chi2_contingency

npi = pd.read_csv("npi_sample.csv")

print(npi.head())

influence_blend_in_freq = pd.crosstab(npi.influence, npi.blend_in)
print("\n", influence_blend_in_freq)

blend_in_special_freq = pd.crosstab(npi.blend_in, npi.special)
blend_in_special_prop = blend_in_special_freq / len(npi)
print("\n", blend_in_special_prop)

special_leader_freq = pd.crosstab(npi.special, npi.leader)
special_leader_prop = special_leader_freq / len(npi)
chi2, pval, dof, expected = chi2_contingency(special_leader_prop)
print("\n", expected)

leader_authority_freq = pd.crosstab(npi.leader, npi.authority)
leader_authority_prop = leader_authority_freq / len(npi)
chi2, pval, dof, expected = chi2_contingency(leader_authority_prop)
print("\n", chi2)

# Results:
'''
  influence blend_in special leader authority
0        no      yes     yes    yes       yes
1        no      yes      no     no        no
2       yes       no     yes    yes       yes
3       yes       no      no    yes       yes
4       yes      yes      no    yes        no

 blend_in     no   yes
influence            
no          773  3535
yes        2626  4163

 special         no       yes
blend_in                    
no        0.110030  0.196269
yes       0.428314  0.265387

 [[0.26075492 0.27758877]
 [0.22361022 0.23804608]]

 3.0255982605008427
'''

# Yes I know, most of this doesn't tell you anything because I switched the variables too often \_('_')_/