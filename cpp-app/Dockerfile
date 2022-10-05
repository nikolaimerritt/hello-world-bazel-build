FROM ubuntu:latest 
RUN apt-get -y update && apt-get install -y
RUN apt-get -y install clang
COPY . /usr/src/docker-test
WORKDIR /usr/src/docker-test 
RUN clang++ -o main src/get-time.cpp src/main.cpp 
CMD ["./main"]