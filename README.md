# PYSINDY O.D.E GENERATION FOR BIOLOGICAL SYSTEMS APPROACH 3 

Refer diagram below.

Summary: This Project seeks to model the reaction kintetics of Glycine and Alanine Reactions. Research done under Prof. John Yin (Dept of CBE, UW-Madison) and Prof. Srinivas Rangarajan (Dept of CBE, Lehigh University) for the Chemical Origins of Life (COoL) Group.

Initially our group used Rule Input Network Generator (RING) based on RDL++ to study prebiotic peptide reactions. I also made an app that auto-converts SMILES strings to Chemical Compound Structures. In doing so, I utilized knowledge of batch files and low level languages to build and run RING scripts that simulate chemical reactions involving the kinetics of amino acids forming peptides in prebiotic systems, a process containing hundreds of potential reactions. Eventually we realized that RING is not too good for this process as it has lots of ambiguity and the scale up of a few molecules would increase exponentially, until and unless very specific constraints were placed. We estimated that this would upwards of several years and decided to change to using SINDY-PY.

SINDY-PY is a library that generates ODEs from data and offers many mathematical simulation opoortunities with said generated model. I made use of SINDY-PY to generate ODEs from chemical data and apply forward simulation to generate machine-learned renditions of prebiotic alanine-glycine reactions. I also measured the viability of a noise recovered model when the noise levels and sampling frequency are altered. Error was computed by comparing the coefficients of the noise-recovered model versus no-noise-recovered model. In the last few weeks of the project, I also incorporated mass balance checking (with bounds of 20%) to verify the physical feasibility of the model.

Below you will find a flow diagram of the project, located now in /Approach 3/

![Approach 3 diagram](https://user-images.githubusercontent.com/68752381/151466516-97b3513d-d549-483f-826e-ace500ec2448.png)
