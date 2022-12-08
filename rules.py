import numpy as np 
import pandas as pd 

def read_file(file):
	cols =["vol1", "close1", "vol2", "close2","vol3", "close3","vol4", "close4","vol5", "close5","vol6", "close6","vol7", "close7","vol8", "close8", "vol9", "close9","vol10", "close10"]
	df = pd.read_csv(file, header = None, names = cols )
	return df

def moving_average(days, df):
	my_df = df.copy()
	for i in range(1, 11):
		my_df['ma_close' + str(i)] = my_df['close' + str(i)].shift(1).rolling(window=days).mean()
		my_df['ma_close' + str(i)] = my_df['ma_close' + str(i)].fillna(my_df['close' + str(i)])
	return my_df


def max_price(days, df):
	d = df.copy()
	for i in range(1,11):
		d['max_close'+ str(i)] = d['close'+str(i)].shift(1).rolling(window=days).max()
		d['max_close' + str(i)] = my_df['max_close' + str(i)].fillna(my_df['close' + str(i)])
	return d


def min_price(days, df):
	d = df.copy()
	for i in range(1,11):
		d['min_close'+ str(i)] = d['close'+str(i)].shift(1).rolling(window=days).min()
		d['min_close' + str(i)] = my_df['min_close' + str(i)].fillna(my_df['close' + str(i)])
	return d
 

def main():
	df = read_file("Training_data.csv")
	my_df = max_price(7, df)

if __name__ == '__main__':
		main()	