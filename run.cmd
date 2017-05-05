@echo off

::set "python=env\Scripts\python"

python in_dig.py "L2 Digital Input" > output\L2_DI.awl
python out_dig.py "L2 Digital Output" > output\L2_DO.awl
python in_anlg.py "L2 Analog Input" > output\L2_AI.awl
python out_anlg.py "L2 Analog Output" > output\L2_AO.awl

python in_dig.py "L3 Digital Input" > output\L3_DI.awl
python out_dig.py "L3 Digital Output" > output\L3_DO.awl
python in_anlg.py "L3 Analog Input" > output\L3_AI.awl
python out_anlg.py "L3 Analog Output" > output\L3_AO.awl

python in_dig.py "L9 Digital Input" > output\L9_DI.awl
python out_dig.py "L9 Digital Output" > output\L9_DO.awl
python in_anlg.py "L9 Analog Input" > output\L9_AI.awl
python out_anlg.py "L9 Analog Output" > output\L9_AO.awl

python di_mapping.py "L2 Digital Input" > output\L2_mapping_di.awl
python do_mapping.py "L2 Digital Output" > output\L2_mapping_do.awl
python ai_mapping.py "L2 Analog Input" > output\L2_mapping_ai.awl
python ao_mapping.py "L2 Analog Output" > output\L2_mapping_ao.awl

python di_mapping.py "L3 Digital Input" > output\L3_mapping_di.awl
python do_mapping.py "L3 Digital Output" > output\L3_mapping_do.awl
python ai_mapping.py "L3 Analog Input" > output\L3_mapping_ai.awl
python ao_mapping.py "L3 Analog Output" > output\L3_mapping_ao.awl

python di_mapping.py "L9 Digital Input" > output\L9_mapping_di.awl
python do_mapping.py "L9 Digital Output" > output\L9_mapping_do.awl
python ai_mapping.py "L9 Analog Input" > output\L9_mapping_ai.awl
python ao_mapping.py "L9 Analog Output" > output\L9_mapping_ao.awl

::python export.py > output\demo_result.awl

python ai_struct_type.py "L2 Analog Input" > output\L2_AI_STRUCT.awl
python ai_struct_type.py "L3 Analog Input" > output\L3_AI_STRUCT.awl
python ai_struct_type.py "L9 Analog Input" > output\L9_AI_STRUCT.awl

python fc_analog_in.py "L2 Analog Input" > output\L2_FC_AI.awl
python fc_analog_in.py "L3 Analog Input" > output\L3_FC_AI.awl
python fc_analog_in.py "L9 Analog Input" > output\L9_FC_AI.awl

python pid_struct.py "Sheet1" > output\PID_STRUCT.awl


pause 'Press [Enter] key to continue...'