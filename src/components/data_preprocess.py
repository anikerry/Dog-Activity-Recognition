import pandas as pd


def preprocess(data):

    columns_name = [
        "record",
        "time",
        "ax",
        "ay",
        "az",
        "wx",
        "wy",
        "wz",
        "AngleX",
        "AngleY",
        "AngleZ",
    ]

    df = pd.DataFrame([x.split(",") for x in data.split("\n")[1:]],
                      columns=columns_name,
                      )

    df.dropna(inplace=True)
    df.drop(["record", "time"], axis=1, inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df
