local input = { 1, 2, 5, 8, 9, 20, 47, 69, 82, 124 }

local binary_search = function(list, target)
	local lo = 0
	local hi = #list

	while lo < hi do
		local mid = math.floor((hi + lo) / 2)

		if list[mid] == target then
			return mid
		end

		if list[mid] < target then
			lo = mid + 1
		end

		if list[mid] > target then
			hi = mid
		end
	end

	return -1
end

local target = 825
print("sample table:", table.concat(input, ","))
print("target:", target)
local index = binary_search(input, target)
print("found target:", index)
