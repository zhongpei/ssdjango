FROM python:2.7
RUN mkdir -p /opt/app
WORKDIR /opt/app
ONBUILD COPY requirements.txt /opt/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
ONBUILD COPY . /opt/app

ADD ./supervisord.conf /etc/supervisord.conf
CMD supervisord -c /etc/supervisord.conf -n

# expose port(s)
EXPOSE 5000
