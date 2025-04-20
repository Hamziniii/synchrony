# synchrony
poorly attempting to do something with track analysis and finding similarities or how "in sync" two songs are in a sense. 

# install docker
Windows: https://www.docker.com/get-started/

# essentia docker img
1. First build the image: `docker build -t essentia:latest .`
2. Run the container script (`conatiner.bat` or `container.sh`)
3. Make changes locally (chagnes are propograted due to docker bind mounts)
4. Run your script in the container, e.g. `python3 app.py`