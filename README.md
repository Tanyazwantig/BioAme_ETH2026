# BioAme_ETH2026
# coonect to ETH euler 
ssh kg2616883@euler.ethz.ch     # click yes
enter password
cd /cluster/home/kg2616883
cd /cluster/scratch/kg2616883   # volve quote given is 2.5T, can have up to 1, 000000 folders , good for large data run
# the target is cn2: it is a neurotoxin from scorpion venom: PDB 2YC1, Cn2 with the antibody fragment scFv 9004G, 1.9 Å
# #1 = Cn2 (2yc1 - Reference baseline)

#2 = Ts1 (1tsa)  # this was dropped due to alignment issues. so I am workign with 3 sequences 

#3 = AaH II (1aho)

#4 = LqhIII (7k18)
# delete. To isolate just the toxin components from each PDB file and run a clean structural alignment, follow these exact commands in ChimeraX
# 2ycl 
delete #1/A,B,D,E,F
#7k18
delete #4/A
# others are single monomers

# alignment. Single-chain monomers like AaH II (1aho) and Ts1 (1tsa) align smoothly and automatically because there is zero ambiguity—there is only one protein chain present in the entire coordinate file.

mmaker #3 to #1 = 
mmaker #4 to #1
# results 
mmaker #3 to #1 =133.2
mmaker #4 to #1 =98.7

#go to tools, sequence viewer and select all target to see the conversed regions 
#chimerax alignment is structurally before sequence, 
#results 
conserved sequence is 36aa
#1/C:1-36 | #3/A:1-36 | #4/B:1-36

