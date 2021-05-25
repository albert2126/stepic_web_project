# Notes

Running GuniCorn:

sudo gunicorn -b 0.0.0.0:8080 hello &

Testing:

* curl -vv 127.0.0.1:8080/?a=b
* curl -i 127.0.0.1/hello/?a=b