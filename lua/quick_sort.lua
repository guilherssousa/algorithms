local create_random_table = function(length)
	length = length or 300
	local list = {}

	for _ = 1, length do
		local random_number = math.random(1, 100)
		table.insert(list, random_number)
	end

	return list
end

local partition = function(table, lo, hi)
	local pivot = table[hi]

	local index = lo - 1

	for i = lo, hi do
		if table[i] < pivot then
			index = index + 1
			local tmp = table[i]
			table[i] = table[index]
			table[index] = tmp
		end
	end

	index = index + 1
	table[hi] = table[index]
	table[index] = pivot

	return index
end

local qs
qs = function(table, lo, hi)
	if lo >= hi then
		return
	end

	local partitionIndex = partition(table, lo, hi)

	qs(table, lo, partitionIndex - 1)
	qs(table, partitionIndex + 1, hi)
end

local quick_sort = function(table)
	qs(table, 1, #table)
end

local list = create_random_table(300)
print("before", table.concat(list, ","))

local start = os.time()
quick_sort(list)
local end_time = os.time()

print("after", table.concat(list, ","))

local elapsed_time = os.difftime(end_time, start)
print("It took", elapsed_time)
