def guess_number guess
    number = 25
    puts "You got it" if guess == number
    puts "Guess was too low" if guess < number
    puts "Guess was too high" if guess > number
end

guess_number 25.00000000

puts (1..100).detect { |i| i == 5}

y= ('a'..'z')
puts y.to_a.to_s

puts (1..255).to_a

puts (1..255).find_all { |i| i%2 == 0 }

def print_sum
  x = (1..255).to_a
  z = 0
  for i in x
    z = z+i
    puts "New Number: " + i.to_s
    puts "Sum is: " + z.to_s
  end
end
print_sum

def print_total x
  z = 0
  for i in x
    z = z+i
    puts "Sum is: " + z.to_s
  end
  print x.find_all { |i| i > 10}
end
print_total [3,5,1,2,7,9,8,13,25,32]



def print_names x
  z = []
  puts x.shuffle
  for i in x
    if i.length > 5
      z.push i
    end
  end
  print z
end

print_names ['John', 'KB', 'Oliver', 'Cory', 'Matthew', 'Christopher']



def alphabet
  y = ('a'..'z')
  x = y.to_a.shuffle
  puts x[x.length-1]
  if x[0].to_s == 'a'
    puts 'you found a vowel'
  end
  if x[0].to_s == 'e'
    puts 'you found a vowel'
  end
  if x[0].to_s == 'i'
    puts 'you found a vowel'
  end
  if x[0].to_s == 'o'
    puts 'you found a vowel'
  end
  if x[0].to_s == 'u'
    puts 'you found a vowel'
  end
else
  puts 'you found ' + x[0] + ' instead'
end

alphabet

def random_numbers
  x = (55..100).to_a
  puts x.sample(10)
end

random_numbers

def random_array
  x = (55..100).to_a.sample(10).sort
  p x
  p x[0]
  p x[x.length-1]
end

random_array

def random_string
  i = 0
  x = 5
  s = ''
  while i < x
    s.insert(i, (65+rand(26)).chr)
    i += 1
  end
  p s
end

random_string

def random_string_array
  i = 0
  z = []
  while i < 10
    s = ''
    x = 0
    while x < 5
      s.insert(x, (65+rand(26)).chr)
      x += 1
    end
    z.insert(i,s)
    i += 1
  end
  p z
end

random_string_array
