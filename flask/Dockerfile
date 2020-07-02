FROM python:3
ADD . /request.py

# Use subdirectory as working directory
WORKDIR /app

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install flask_cors

USER 1001
CMD [ "python", "request.py" ]
