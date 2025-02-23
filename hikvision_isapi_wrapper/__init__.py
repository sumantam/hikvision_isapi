#from dotenv import load_dotenv
import os
from requests.auth import HTTPDigestAuth
from requests import Session
from .tools import LiveServerSession

# Load .env file
#load_dotenv()


HIKVISION_ACT_LOGIN = os.environ.get('HIKVISION_ACT_LOGIN')
HIKVISION_ACT_PASSWORD = os.environ.get('HIKVISION_ACT_PASSWORD')
host = os.environ.get("HIKVISION_ACT_HOST")




class LoginPasswordMissingError(Exception):
    pass


if HIKVISION_ACT_LOGIN is None or HIKVISION_ACT_PASSWORD is None:
    raise LoginPasswordMissingError(
        "All Hikvision Access Control Terminals API methods require login and password!"
    )

auth = HTTPDigestAuth(HIKVISION_ACT_LOGIN, HIKVISION_ACT_PASSWORD)
session = Session()

session.auth = auth


from .person import Person
from .fplib import FaceData, FaceDataLib
from .event import Event
