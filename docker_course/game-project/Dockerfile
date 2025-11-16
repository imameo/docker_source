FROM ubuntu

WORKDIR /src

RUN apt-get update
RUN apt-get -y install python3

COPY guess_game.py ./guess_game.py

CMD ["python3", "guess_game.py"]
