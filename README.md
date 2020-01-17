Heart rate zone calculator  
===================================================

##### :

Produces a report based on the formula's laid out in Training for the Uphill Athelete. 

### Example 

Running
  ```python
python3 runZoneCalc.py -Age 37 -AeT 147 -AnT 167
```
Will procude the followign report:
```python
According to the basic MAF forula your AeT should be: 146
The AeT that you've submitted was: 147
There's 1 % between the basic MAF formula and the AeT you submitted from your own test.
The Lactate Threshold you submitted was: 167
There's a 14 % diff from your AeT and your Ant
Your ADS is high, you still have much to gain from aerobic training in Zone2
Your HR zones are:
Recovery should be below  116
Zone 1 = 117 131
Zone 2 = 131 147
Zone 3 = 146 167
Zone 4 = 166 186

```

```python 
runZoneCalc.py

Required arguments:
                    -Age
                    -AeT == Aroebic Threshold
                    -AnT == Anerarobic/Lactate Threshold
```
    
### How to build/Install

```python
pip install -r requirements.txt
```  
### Requirments

Python3 or greater installed and PIP.

 
