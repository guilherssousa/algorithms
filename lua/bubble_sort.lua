local input = { 8, 20, 5, 1, 9, 47, 82, 69, 124, 2 }

local bubble_sort = function(list)
  for i = 1, #list do
    for j = 1, #list - i do
      if list[j] > list[j + 1] then
        list[j], list[j + 1] = list[j + 1], list[j]
      end
    end
  end
end

print("Before:", table.concat(input, ','))
bubble_sort(input)
print("After:", table.concat(input, ','))
