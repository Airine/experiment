from os import error
import pandas as pd
import glob
import json

headers = ["id","bandwidth", "burst", "bid", "metric", "application"]

if __name__ == "__main__":
    df = pd.DataFrame(columns=headers)
    dirs = sorted(glob.glob('clients/client*'), key=lambda x:int(x[x.find('-')+1:]))
    for i, d in enumerate(dirs):
        setting = json.load(open(d+'/setting.json', 'r'))
        last_line = None
        try:
            with open(d+"/log.txt", "r") as file:
                for last_line in file:
                    pass
        except error:
            pass
        qoe = -100
        if last_line:
            qoe = last_line[last_line.find(':')+1:]

        df.loc[i] = [
            i,
            setting["bandwidth"],
            setting["burst"],
            setting["bid"],
            qoe,
            setting["application"]
        ]

    df.set_index(["id"], inplace=True)
    print(df.head())
    df.to_csv('result.csv')
