import typing

from fastapi.responses import JSONResponse

import settings


class MainJSONResponce(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        if isinstance(content, typing.Dict):
            content['version'] = settings.API_VERSION

        return super(MainJSONResponce, self).render(content)