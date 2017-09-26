from flask import Flask
import logging
from src.servicehost.RoutesRegistration import RoutesRegistration
logger = logging.getLogger(__name__)

f = Flask(__name__)

application = RoutesRegistration().register_in_app(f)

def main():
    application.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
