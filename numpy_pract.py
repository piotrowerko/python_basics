import numpy as np

def main():
    pp = np.array([0,-2,-4,-6,-8,-10])
    indices = np.array([0,1,2])
    kk = np.take(pp, indices)
    kk_ = np.abs(kk).argmin()
    return kk_



if __name__ == '__main__':
    print(main())