# Returns the empty indice from string.
def find_empty(pos):
	return int(pos.find("0"))

# Takes the swap query indices and returns swapped string.
def swap(str, i1, i2):
	t = list(str)
	i1, i2 = int(i1), int(i2)
	t[i2], t[i1] = t[i1], t[i2]
	return ''.join(t)

# Searches different moves across possible configurations.
def _rearrange(current_pos, end_pos, curr_ordering, all_orderings):
	if current_pos == end_pos:
		all_orderings.append(curr_ordering.copy())
		return

	empty_pos = find_empty(current_pos)
	# try next combination
	for i, v in enumerate(current_pos):
		if v != "0":
			next_pos = swap(current_pos, i, empty_pos)
			# if we did not reach to this sequence yet, move on
			if next_pos not in curr_ordering:
				curr_ordering.append(next_pos)
				_rearrange(next_pos, end_pos, curr_ordering, all_orderings)
				curr_ordering.remove(next_pos)

	return

def rearrange(start_pos, end_pos):
	# keeps the movements as a list of strings
	all_orderings = []
	curr_ordering = [start_pos]

	# try different possible configurations, move any car to the empty lot
	_rearrange(start_pos, end_pos, curr_ordering, all_orderings)

	return all_orderings


if __name__ == "__main__":
	start = "1203"
	end = "3120"
	all_configs = rearrange(start, end)
	print("number of different configurations: ", len(all_configs))
	print("shortest config:", sorted(all_configs, key=len)[0])