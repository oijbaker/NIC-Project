import random

global function_array
function_array = ['avg5', 'max5', 'min5','avg10', 'max10', 'min10','avg15', 'max15', 'min15', 'avg25', 'max25', 'min25', 'avg50', 'max50', 'min50', 'close']
function_array_method = ['avg', 'max', 'min']

for _ in range(20):
    temp = function_array_method[random.randint(0, 2)] + str(random.randint(1, 99))
    function_array.append(temp)