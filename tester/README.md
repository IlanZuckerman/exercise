Install packages:  
`cd tester && pip install -r requirements.txt`  

Execute tests:  
`pytest -q -s --actual_file_path  <path to actual json result from monitor. default is data/actual1.json> --config_file_path data <path to config file which serves us as an expected result>`  
  
For example:  
`pytest -q -s --actual_file_path data/actual1.json --config_file_path data/config1.yml` 
  
Note:  
config file is basically the same conf which is being used by the 'proc_generator' to generate the process`