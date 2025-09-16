import pandas as pd


def csvfind(tableName, year):
    return  pd.read_csv(f"./csvs data/{tableName}/{year}/{tableName}_{year}.csv")


def get_total_income(year):
    a = csvfind("Total_Income", year)
    return a.groupby("ID")["Income"].sum().reset_index()