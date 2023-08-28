word_16 = input("Input word longer 16 characters and even: ")
characters = len(word_16)
result_word = ""

#basis of all other functions
stage_1 = characters - 10
start_ammount = int((stage_1)/2)

#ammounts to start and end of middle function
middle_start = int(start_ammount)
middle_end = int(middle_start + 10)

#ammounts to start and end of end functions
end_start = int(middle_end)
end = int(end_start + start_ammount)

        #the following order of code is not in order of the scenario but in order of logic and the placment of the final encryption

# this is step 2 within the scenario
string_3_1st = word_16[0:start_ammount]
final_1 = string_3_1st[::-1]
                                                            #adding recived string to the final
result_word = result_word + final_1

#this is step 1 within the scenario
string_1_2nd = word_16[middle_start:middle_end]
final_2 = string_1_2nd[::-1]
                                                            #adding recived string to the final
result_word = result_word + final_2

#this is step 3 within the scenario
string_2_3rd = word_16[end_start:end]
final_3 = string_2_3rd[::-1]
                                                            #adding recived string to the final
result_word = result_word + final_3

print (result_word)






