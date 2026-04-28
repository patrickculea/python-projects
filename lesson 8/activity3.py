numbers =40
prev_mean =38
correct_num =56
wrong_num =36

prev_sum = prev_mean * numbers
correct_sum =prev_sum + correct_num - wrong_num
correct_mean = correct_sum / numbers
print(f"the correct mean is: {correct_mean}")