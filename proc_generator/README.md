To create a docker image:  
`docker build .`  
  
Edit the `config.yml` to desired expected result  

To run the image and execute the proc generator:  
`docker run --rm <image id>`  
  
To enter the container in an interactive mode:  
First, uncoment the 'ENTRY' line in Docker file  
Rebuild the image  
Run it with:  
`docker run -it --rm <image id> /bin/bash`  

To manually execute the proc generator:   
`python main.py`