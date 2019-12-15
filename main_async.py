import time
import torch
import tqdm

from dataloader import DataLoader

class Dataset():
    def __init__(self):
        super().__init__()

    def __len__(self):
        return 1000

    def __getitem__(self, index):
        return torch.tensor(3)

def nnet(x):
    time.sleep(0.033)
    return x + 0.1

def reconstruction(x):
    time.sleep(0.033)
    return x + 0.01
    
def render(x):
    time.sleep(0.033)
    return x + 0.001
    
if __name__ == '__main__':
    dataset = Dataset()
    loader = DataLoader(
        dataset, 
        batch_size=1, 
        num_workers=4, 
        pin_memory=True,
        processors=[
            lambda x: x.cuda(),
            lambda x: nnet(x), # 33 ms
            lambda x: reconstruction(x), # 33 ms
            lambda x: render(x), # 33 ms
        ])

    tic = time.time()
    ncount = 0
    for data in tqdm.tqdm(loader):
        print (data.shape, data.is_cuda, data.dtype, data)
        ncount+=1
    toc = time.time()

    print (f"average runtime is {(toc-tic)/ncount} s") # total 36 ms
