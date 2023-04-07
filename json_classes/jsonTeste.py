import json
from pathlib import Path
file1 = r"/home/pedrokim/PedroFiles/ITA/1º Semestre Comp/CSI-22/ISS_defense/level_data/S1L1.JSON"

file2 = Path("level_data")/"S1L1.JSON"

with open(file2,'r') as f:
    level_data = json.load(f)

print(level_data['iss'][0])