file=open("CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TRAIN_00000.eml")
data_word_counts=0
up_case=0

words=["free","money","credit","subscribe"]
keys = { free: 0, money: 0,credit: 0,subscribe: 0,upper_case:0}

file.each do |line|
  words.each do |word|
    if line.include?(word.upcase)||line.include?(word.downcase)
      keys[:"#{word}"]+=1
    if /\p{Upper}/.match(line)
      keys[:upper_case]+=1
    end
  end
end
end
p keys
