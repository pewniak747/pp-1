#!/usr/bin/env ruby

require 'yaml'

model_file = ARGV[0]
data_file = ARGV[1]

model = File.read(model_file).split("\n")
data = YAML.load(File.read(data_file))

processed = model.map { |line|
  if line.empty?
    line
  else
    data.each do |variable, value|
      line.gsub!(variable, value.to_s)
    end
    line << ";" unless line[-1] == ";"
  end
}.join("\n") << "\n"

print(processed)
