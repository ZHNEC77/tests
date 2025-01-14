from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le=2)
    title: str

    # @field_validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('id is not less than two')
    #     else:
    #         return v
