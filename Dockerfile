FROM python:2.7
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app/
RUN pip install --no-cache-dir -r requirements.txt

ADD ./supervisord.conf /etc/supervisord.conf
CMD supervisord -c /etc/supervisord.conf -n

# expose port(s)
EXPOSE 5000
