#!/usr/bin/env ruby

input_str = ARGV[0]

sender = input_str.match(/\[from:([^[\]]+)\]/)&.captures&.first
receiver = input_str.match(/\[to:([^[\]]+)\]/)&.captures&.first
flags = input_str.match(/\[flags:([^[\]]+)\]/)&.captures&.first

puts "#{sender},#{receiver},#{flags}"
