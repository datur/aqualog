import os

from dotenv import load_dotenv
from .config import get_api_port, get_website_domain

from supertokens_python import (InputAppInfo, SupertokensConfig
                                , init)
from supertokens_python.recipe import session, thirdparty, emailpassword
from supertokens_python.recipe.thirdpartyemailpassword import (
     Github, Google)

load_dotenv()

def init_supertokens():
    init(
        supertokens_config=SupertokensConfig(
            # connection_uri="https://try.supertokens.com",
            connection_uri='localhost:3567',
            api_key='Akjnv3iunvsoi8=-sackjij3ncisds'
        ),
        app_info=InputAppInfo(
            app_name='Supertokens',
            api_domain='http://localhost:' + get_api_port(),
            website_domain=get_website_domain(),
            api_base_path="/auth",
            website_base_path="/auth"
        ),
        framework='flask',
        recipe_list=[
            session.init(),
            emailpassword.init(
                
            )
        ]
    )