from src.enums.global_enums import GlobalErrorMessage


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code
        self.parsed_obj = None

    def validate(self, schemas):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_obj = schemas.model_validate(item)
                self.parsed_obj = parsed_obj
        else:
            schemas.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            # GlobalErrorMessage.WRONG_STATUS_CODE.value
            assert self.response_status in status_code, self
        else:
            # GlobalErrorMessage.WRONG_STATUS_CODE.value
            assert self.response_status == status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_obj

    def __str__(self):
        return f"""Status code: {self.response_status}\n
Requsted url: {self.response.url}\n
Response body: {self.response_json}"""
