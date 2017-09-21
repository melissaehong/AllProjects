

(1..255).each {|i| puts i}

#puts print_1_to_255

(1..255).each {|i| puts i if i.odd?}

#puts print_odds

sum = 0
(0..255).each {|i| puts "New number: #{i} Sum: #{sum += i}"}

x = [1,3,5,7,9,13]
#puts x.each { |i| x[i]}

#puts x.max

arr = [2,10,3]

#puts arr.reduce(:+) / arr.length.to_f


