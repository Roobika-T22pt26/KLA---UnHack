''' Input milestone0 using json and storing in dictionaries'''
import json

with open(r"C:\Users\csuser\Desktop\Milestone1.json",'r') as file:
    details = json.load(file)

print(details)


print("_______Wafer ______")
print(details['wafers'])
Wafer_deatils = details['wafers']
Quantity_Wafer = Wafer_deatils[0]['quantity']

ProcessingTime =  Wafer_deatils[0]['processing_times']
print(ProcessingTime)
s_time =[]
s_time.append(ProcessingTime['S1'])
s_time.append(ProcessingTime['S2'])

Total_time = 0

Map = set()
S_list =[]
Step_details = details['steps']
print()
print("step length: ",len(Step_details))
print("total no of wafers : ",len(Wafer_deatils))
print("Wafer Quantity",Quantity_Wafer)
print()
#n= len(Step_details) - 1
temp = []
wDict = {}
for i in range(len(Wafer_deatils)):
    Dependency = Step_details[i]['dependency']
    if Dependency == None :
        print("Its null dependency")
        for k in range(int(Quantity_Wafer)):
            for j in range(len(Step_details)):
                coord = (Total_time,Total_time+s_time[j])
                temp.append(Total_time+s_time[j])
                S_list.append(coord)
                wDict[coord] = f"W{i+1}-{k+1}"
            Total_time = max(temp)

print("The output is ")
print(S_list) 

print()
print("Mapping Wafer coordinates")
print(wDict)
print()

print(f"W1-1 {S_list[0]}")
print(f"W1-2 {S_list[1]}")
print(f"w1-2 {S_list[2]}")
print(f"W1-3 {S_list[3]}")
print(f"W1-3 {S_list[4]}")
print(f"W1-1 {S_list[5]}")
print("____________________________")
print(S_list)


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

schedule = [ {"wafer_id": "W1-1", "step": "S1", "machine": "M1", "start_time": 0, "end_time": 10},
{"wafer_id": "W1-2", "step": "S2", "machine": "M2", "start_time": 0, "end_time": 15},
{"wafer_id": "W1-2", "step": "S1", "machine": "M1", "start_time": 15, "end_time": 25},
{"wafer_id": "W1-3", "step": "S2", "machine": "M2", "start_time": 15, "end_time": 30},
{"wafer_id": "W1-3", "step": "S1", "machine": "M1", "start_time": 30, "end_time": 40},
{"wafer_id": "W1-1", "step": "S2", "machine": "M2", "start_time": 30, "end_time": 45} 
]

print(schedule)

with open("sample_mile1.json", "w") as outfile:
    json.dump(schedule, outfile)
