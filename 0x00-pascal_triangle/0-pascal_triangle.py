#!/usr/bin/python3
"""This module will result in the Pascal's Triangle"""


def pascal_triangle(n):
	""" This function will implement the Pascals triangle"""
	triangle = []
	for i in range(n):
		row = [0] * (i + 1)
		row[0] = 1
		row[-1] = 1
		for j in range(1, i):
			row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
		triangle.append(row)
	return triangle

