def get_intervals(excluded, maximum):
	intervals = []
	expected = 0
	while excluded:
		value = excluded.pop(0)
		if value == expected + 1:
			intervals.append(expected)
		elif value > expected + 1:
			intervals.append((expected, value - 1))
		expected = value + 1
	if expected == maximum:
		intervals.append(maximum)
	elif expected < maximum:
		intervals.append((expected, maximum))
	return intervals

def test_get_intervals_basic():
	excluded = [1, 5, 7, 10, 50, 100]
	expected = [0, (2, 4), 6, (8, 9), (11, 49), (51, 99)]
	intervals = get_intervals(excluded, 100)
	assert intervals == expected, 'Intervals: {}, expected: {}'.format(intervals, expected)
	print u'Test basic passed!'

if __name__ == '__main__':
	test_get_intervals_basic()
