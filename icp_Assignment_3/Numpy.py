import numpy as np

def replace_maxmium(array, replace_value, axis):
    output = np.where(array == np.max(
        array, axis=1).reshape(-1, 1), 0 * array, array)
    print(output)


def main():
    random20 = np.random.random_sample(20) * 20 + 1
    print(random20)
    random20_4by5 = random20.reshape((4, 5))
    print(random20_4by5)
    replace_maxmium(random20_4by5, 0, 1)


if __name__ == "__main__":
    main()