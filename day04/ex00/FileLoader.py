import pandas as pa

class FileLoader:
    def load(self, path):
        data = pa.read_csv(path)
        print ("Dimensions of the dataset is {} x {}".format(data.shape[0], data.shape[1]))
        return data

    def display(self, df, n):
        if n > 0:
            return print(df.head(n))
        else:
            n = n * -1
            return print(df.tail(n))

