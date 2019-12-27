# my_tqdm
my_tqdm. It doesn't flood ipython notebooks with newlines. It is done in a one single file so it doesn't require any installation.

**"Installation"**:
```
!wget https://raw.githubusercontent.com/rashchedrin/my_tqdm/master/my_tqdm.py -nc -O my_tqdm.py
from my_tqdm import my_tqdm
```
**Usage**:
```
for _ in my_tqdm(range(50000000)):
    pass
```
Example output:
```
50000000 / 50000000. 1527040.411 ops/sec. Expected end: 2019-12-16 14:47:48.528161. Left: 0s. Spent: 32s..
```
