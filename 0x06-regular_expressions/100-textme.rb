#!/usr/bin/env ruby

input_string = ARGV[0]

sender = input_string.scan(/\[from:([^\]]+)\]/).flatten.first

receiver = input_string.scan(/\[to:([^\]]+)\]/).flatten.first

flags = input_string.scan(/\[flags:([^\]]+)\]/).flatten.first

puts "#{sender},#{receiver},#{flags}"
