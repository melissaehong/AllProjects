# just exercise

=begin
    long comment
    another comment
    another comment
=end

puts "hello"
puts "Coding"
puts "Dojo"

print "hello"
print "Coding"

BEGIN{
    puts "this is the begin block"
}

END{
    puts "this is the end block"
}

x = 5; y = 10; z = x*y

puts z

first_name = "Melissa"
last_name = "Hong"

puts "Your Name is " + first_name + last_name
puts "Your first name is #{first_name} and your last name is #{last_name}"
puts "Your first name is %s and your last name is %s" % [first_name, last_name]

a = "hello" 
b = "world"

puts a, b 
puts a + b

puts "I am an instance of".class
puts String.new("I am an instance of the String class")