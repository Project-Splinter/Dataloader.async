# Dataloader.async
An asynchronous pytorch Dataloader for general neural network pipeline accelaration. (Tested for `torch==2.1.0`)

<div align="center">
<img src="figure.png" width="500px"/>
<p> Our dataloader is fully compatible with offical Dataloader, with extension that allows async processors.</p>
</div>

## Usage:

```
$ python setup.py install
```

then

```
from dataloaderAsync import DataLoader

...
```

* Note: Only tested on pytorch 1.3.0. Should be able to compatible with older versions.
