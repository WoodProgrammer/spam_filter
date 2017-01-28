class Mail_Miner

  @data_word_counts=0
  @signs=["%","$"]
  $words=["free","money","credit","subscribe","girl","porn","sex","guaranteed"]


  def label_counter(file_url)
    file_csv=open("spam_data.csv","a+")
    keys = { free: 0, money: 0,credit: 0,subscribe: 0,girl:0,upper_case:0,porn:0,sex:0,guaranteed:0,sign:0}
    file=open(file_url)
    file.each do |line|
      $words.each do |word|
        if line.include?(word.upcase)||line.include?(word.downcase)
          keys[:"#{word}"]+=1
        if /\p{Upper}/.match(line)
          keys[:upper_case]+=1
          p line
        end
      end
    end
    end
    file_csv.puts(keys)

  end
end
data_obj=Mail_Miner.new
i=0
for i in 0..9
    file="CSDMC2010_SPAM/CSDMC2010_SPAM/TRAINING/TRAIN_0000#{i}.eml"
    data_obj.label_counter(file)
    p i
end
