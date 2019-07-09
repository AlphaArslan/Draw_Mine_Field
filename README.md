# Draw_Mine_Field
---
## Background :
<p> In Mine Sweepers Competitions, robots try to find mines and map their location. this script will be probably used as the last node. this script takes a tuple of location.</p>

## Format & Notation :
#### We assume your field is mapped like follows :
```
A1    A2    A3    A4    .  .  .      NORTH
B1    B2    B3    B4                   ^
C1    C2    C3    C4                   |
D1    D2    D3    D4                   |
.                                    LENGTH
.                                      |
.                                      |
-----------------WIDTH-------------------
```
#### Script Input Format:
* the script takes _mines locations_ as a __tuple__
* A tuple element is typically one __UPPERCASE__ liter followed by a __number__ (i.e. "A2" )
