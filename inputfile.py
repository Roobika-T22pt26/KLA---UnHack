''' Input milestone0 using json and storing in dictionaries'''
import json

with open(r"C:\Users\csuser\Desktop\Milestone0.json",'r') as file:
    details = json.load(file)

print(details)


print("_______Wafer ______")
print(details['wafers'])
Wafer_deatils = details['wafers']
Quantity_Wafer = Wafer_deatils[0]['quantity']

ProcessingTime =  Wafer_deatils[0]['processing_times']
print(ProcessingTime)
s1_time =  ProcessingTime['S1']
print(s1_time)
s2_time =  ProcessingTime['S2']
print(s2_time)

Total_time = 0

Map = set()
S1_list =[]
S2_list =[]
Step_details = details['steps']
print(len(Step_details))
for i in range(len(Wafer_deatils)):
    Dependency = Step_details[i]['dependency']
    if Dependency == None :
        print("Its null dependency")
        for k in range(len(Wafer_deatils)):
            for j in range(len(Step_details)):
                Step1 = (Total_time,Total_time+s1_time)
                Step2 = (Total_time,Total_time+s2_time)
                Total_time = max(Total_time,s1_time,s2_time)
                S1_list.append(Step1)
                S2_list.append(Step2)
                Map.add(Step1)
                Map.add(Step2 )


print(f"W1-1 {S1_list[0]}")
print(f"W1-2 {S1_list[1]}")
print(f"W1-1 {S2_list[1]}")
print(f"W1-2 {S2_list[0]}")
print("____________________________")
print(S1_list)
print(S2_list)
print(Map)

Machine_details = details['machines']
print(Machine_details)
print(len(Machine_details))
MachineStep = {}
for i in range(len(Machine_details)):
    key = Machine_details[i]['machine_id']
    val = Machine_details[i]['step_id']
    MachineStep[key] = val


print("Machine and step Combination")
print(MachineStep)

print("\n")
print("Output")
#for tup in  
