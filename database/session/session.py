import os
import sys
import traceback
import yaml

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool


class SQLSession:

    def __init__(self, database_name):
        self.url = 'mysql+mysqlconnector://{0}:{1}@localhost/{2}'
        self.credentials = self.get_credentials()
        self.database_name = database_name
        self.engine = None

    def get_credentials(self):
        try:
            basepath = os.path.dirname(__file__)
            credentials_filepath = os.path.abspath(os.path.join(basepath, "..", "credentials.yml")) # Up to parent dir
            stream = open(credentials_filepath, "r")
        except FileNotFoundError:
            print("Error: no credentials.yml file found in top-level project directory.")
            return None
        try:
            return yaml.load(stream)
        except:
            print("Error reading credentials from credentials.yml. Ensure the file is properly formatted.")
            return None

    def make_engine(self):
        if self.credentials is not None:
            username, password = self.credentials['username'], self.credentials['password']
            url = self.url.format(username, password, self.database_name)
            try:
                self.engine = create_engine(url, echo=False, poolclass=NullPool, connect_args={'connect_timeout': 10000})#, connect_args={'connect_timeout': 60}
            except:
                traceback.print_exc()
                print("Error creating SQLAlchemy engine. Check credentials and DATABASE name.")
                return None
        else:
            sys.exit()

    def get_session(self):
        if not self.engine:
            self.make_engine()

        Session = sessionmaker(autoflush=False, bind=self.engine)
        return Session()
