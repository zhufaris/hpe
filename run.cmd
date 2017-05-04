@echo off

::set "python=env\Scripts\python"

python in_dig.py "L2 Digital Input" > output\L2_DI.txt
python out_dig.py "L2 Digital Output" > output\L2_DO.txt
python in_anlg.py "L2 Analog Input" > output\L2_AI.txt
python out_anlg.py "L2 Analog Output" > output\L2_AO.txt

python in_dig.py "L3 Digital Input" > output\L3_DI.txt
python out_dig.py "L3 Digital Output" > output\L3_DO.txt
python in_anlg.py "L3 Analog Input" > output\L3_AI.txt
python out_anlg.py "L3 Analog Output" > output\L3_AO.txt

python in_dig.py "L9 Digital Input" > output\L9_DI.txt
python out_dig.py "L9 Digital Output" > output\L9_DO.txt
python in_anlg.py "L9 Analog Input" > output\L9_AI.txt
python out_anlg.py "L9 Analog Output" > output\L9_AO.txt

python di_mapping.py "L2 Digital Input" > output\L2_mapping_di.txt
python do_mapping.py "L2 Digital Output" > output\L2_mapping_do.txt
python ai_mapping.py "L2 Analog Input" > output\L2_mapping_ai.txt
python ao_mapping.py "L2 Analog Output" > output\L2_mapping_ao.txt

python di_mapping.py "L3 Digital Input" > output\L3_mapping_di.txt
python do_mapping.py "L3 Digital Output" > output\L3_mapping_do.txt
python ai_mapping.py "L3 Analog Input" > output\L3_mapping_ai.txt
python ao_mapping.py "L3 Analog Output" > output\L3_mapping_ao.txt

python di_mapping.py "L9 Digital Input" > output\L9_mapping_di.txt
python do_mapping.py "L9 Digital Output" > output\L9_mapping_do.txt
python ai_mapping.py "L9 Analog Input" > output\L9_mapping_ai.txt
python ao_mapping.py "L9 Analog Output" > output\L9_mapping_ao.txt

::python export.py > output\demo_result.txt

python ai_struct_type.py "L2 Analog Input" > output\L2_AI_STRUCT.txt
python ai_struct_type.py "L3 Analog Input" > output\L3_AI_STRUCT.txt
python ai_struct_type.py "L9 Analog Input" > output\L9_AI_STRUCT.txt

python fc_analog_in.py "L2 Analog Input" > output\L2_FC_AI.awl
python fc_analog_in.py "L3 Analog Input" > output\L3_FC_AI.awl
python fc_analog_in.py "L9 Analog Input" > output\L9_FC_AI.awl


pause 'Press [Enter] key to continue...'