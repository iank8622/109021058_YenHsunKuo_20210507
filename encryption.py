# 加密與解密(亂數打亂)
import sys
import random as rand
import numpy as np


if __name__ == "__main__":
    if len(sys.argv) > 2:
        seedValu = int(sys.argv[1])
        # 用seed()打亂
        data = list(sys.argv[2])
        rand.seed(seedValu)
        rand.shuffle(data)
        # 用相同的key打亂
        key = list(np.arange(0, len(data)))
        rand.seed(seedValu)
        rand.shuffle(key)
        print("".join(data))
        print(key)

        newData = []
        count = 0
        while count != len(key):
            for i in range(len(key)):
                if int(key[i]) == count:
                    newData.append(data[i])
                    count += 1
        print(newData)
                

        


