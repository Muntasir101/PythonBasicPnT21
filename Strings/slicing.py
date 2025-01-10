expected_cost = 6020
actual_cost = "$6,020.00"

actual_cost_modified_1 = actual_cost.replace("$", "").replace(",","")
print(actual_cost_modified_1) # 6,020.00

actual_cost_modified_2 = float(actual_cost_modified_1)
print(actual_cost_modified_2) # 6020.0

actual_cost_modified_3 = int(actual_cost_modified_2)
print(actual_cost_modified_3) # 6020