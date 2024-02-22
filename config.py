import os

import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    USER_NAME: str = os.environ.get('USER_NAME')
    ACCESS_KEY: str = os.environ.get('ACCESS_KEY')
    remote_url: str = os.environ.get('REMOTE_URL')

    deviceName_android: str = 'Samsung Galaxy S23'
    platformVersion_android: str = '13.0'
    deviceName_ios: str = 'iPhone 12'
    platformVersion_ios: str = '17'
    app: str = 'bs://sample.app'
    timeout: float = 10.0


settings = Settings()
