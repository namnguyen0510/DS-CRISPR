# Introduction
CRISPR technology promises to revolutionize biomedical science and medicine, in which the merit of this advancement lies in its ability to edit genes with high precision and efficiency. gRNA design of the CRISPR-associated proteins is the key to advancing this technology but requires large computations due to the massive search space. This work introduces CRISPR-SCORE$^\copyright$ and \textit{DS}-CRISPR to address: (1) a robust scoring metric of the gRNA based on its intrinsic-genetic contents and (2) a cost-efficient and effective approaches to synthesize gRNA, respectively. First, we demonstrate that the proposed CRISPR-SCORE$^\copyright$ positively correlates with efficacy scores, evaluated using six publicly available databases. Second, we show that the synthesized database from \textit{DS}-CRISPR is quality in silico designed gRNAs, which could reduce the cost and improve the success of in \textit{vivo} or in \textit{vitro} experiments. 
# Requirements
```python
python==3.7.0
numpy==1.21.5
sci-kit-learn==1.0.2
```
# Model Search Space
## Strategy 1
```python
model_gsds.py
```
## Strategy 2
```python
model_gfds.py
```
## Strategy 3 and 4
```python
model_csds.py
```
## Generate gRNA strings
```python
python data_generation.py
```
## Policy for the Usage of Data and Algorithm
All actions extended from the game that mean harm to human beings and lives are prohibited. Definition of **Harm** includes
- Hate: hateful symbols, negative stereotypes, comparing certain groups to animals/objects, or expressing or promoting hate based on identity.
- Harassment: mocking, threatening, or bullying an individual.
- Violence: violent acts and the suffering or humiliation of others.
- Self-harm: suicide, cutting, eating disorders, and other attempts at harming oneself.
- Illegal activity: drug use, theft, vandalism, and other illegal activities.
- Deception: major conspiracies or events related to major ongoing geopolitical events.
- Political: politicians, ballot boxes, protests, or other content that may be used to influence the political process or to campaign.
- Public and personal health: the treatment, prevention, diagnosis, or transmission of diseases or people experiencing health ailments without clinical supervision.
- Monetize: All resources generated within computation/simulation cannot be transferred to actual money or assets in any circumstances. Attempting to violate this policy will cope with legal issues.



