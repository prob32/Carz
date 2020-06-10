import numpy as np

def model_inputs (mileage,year,make,model, my_list):
    inputs = [0] * 40
    Year = "Year_"+year
    Make = "Make_"+make
    Model = "Model_"+model

    inputs[0] = mileage
    if Year in my_list:
        year_pos = my_list.index(Year)
        inputs[year_pos] = 1
    if Make in my_list:
        make_pos = my_list.index(Make)
        inputs[make_pos] = 1
    if Model in my_list:
        model_pos = my_list.index(Model)
        inputs[model_pos] = 1

    list = np.array(inputs)
    list = list.reshape(-1,40)
    return list
