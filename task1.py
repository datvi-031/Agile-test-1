# @author : Daathwinaagh - CS20B1031
# @Category : Intern Test-1 (Agile)
# @Date : 17th April, 2023

import pandas as pd
import numpy as np

class task_one:
	def __init__(self):
		self.df1 = pd.read_csv("./rigorbuilder.csv")

	def taskOne(self):
		self.df1_sorted = self.df1.sort_values(by='total_statements', ascending=False)
		self.df1_sorted['Rank'] = (self.df1_sorted['total_statements']+self.df1_sorted['total_reasons']).rank(ascending=False, method='dense')
		self.df1_sorted['Rank'] = self.df1_sorted['Rank'].astype(int)
		self.df1_sorted = self.df1_sorted.reindex(columns=['Rank', 'name', 'uid', 'total_statements', 'total_reasons'])

		self.df1_sorted = self.df1_sorted.sort_values(by='Rank', ascending=True)
		self.df1_sorted.to_csv('task_one.csv', index=False)
		self.choice = input("Do you want to display ? [y/n]: ")
		if self.choice == "y":
			print(self.df1_sorted)

class task_two():
	def __init__(self):
		self.df1 = pd.read_csv("./users.csv")
		self.df2 = pd.read_csv("./rigorbuilder.csv")
	
	def taskTwo(self):
		self.df = pd.merge(self.df1, self.df2, left_on="User ID", right_on="uid")
		self.df = self.df.drop(['name', 'S No_y', 'User ID'], axis=1)

		self.grouped_df = self.df.groupby('Team Name')[['total_statements', 'total_reasons']].mean().reset_index()
		self.sorted_df = self.grouped_df.sort_values(by='total_statements', ascending=False)
		self.sorted_df = self.sorted_df.reset_index()
		self.sorted_df = self.sorted_df.rename(columns={'Team Name': 'Thinking Teams Leaderboard',
		                                      'total_statements': 'Average Statements',
		                                      'total_reasons': 'Average Reasons'})
		self.sorted_df['Team Rank'] = self.sorted_df.index + 1
		self.sorted_df = self.sorted_df[['Team Rank', 'Thinking Teams Leaderboard', 'Average Statements', 'Average Reasons']]

		self.sorted_df.to_csv('task_two.csv', index=False)
		self.choice = input("Do you want to display ? [y/n]: ")
		if self.choice == "y":
			print(self.sorted_df)

def main():
	t1 = task_one(); t1.taskOne()
	t2 = task_two(); t2.taskTwo()

if __name__ == '__main__':
	main()