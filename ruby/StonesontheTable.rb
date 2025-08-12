def solution(stones)
  removals = 0
  (1...stones.length).each do |i|
    if stones[i] == stones[i-1]
      removals += 1
    end
  end
  removals
end