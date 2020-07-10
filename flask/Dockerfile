FROM python:3
ADD . /request.py

# Use subdirectory as working directory
WORKDIR /request

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip3 install flask
RUN pip3 install flask_cors
RUN pip3 install requests

COPY . /request

ENTRYPOINT [ "python3" ]

CMD ["request.py"]
