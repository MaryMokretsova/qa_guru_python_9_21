import os

import dotenv
import pydantic


class Settings(pydantic.BaseModel):
    dotenv.load_dotenv()

    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    remote_url: str = os.getenv('REMOTE_URL')

    deviceName: str = 'Samsung Galaxy S23'
    platformVersion: str = '13.0'
    app: str = 'bs://sample.app'
    timeout: float = 10.0


settings = Settings()
