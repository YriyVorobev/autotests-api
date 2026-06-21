from pydantic import BaseModel
from clients.courses.courses_clients import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.files import function_file
from fixtures.users import UserFixture
import pytest

class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def course_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
        course_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema(
        preview_file_id = function_file.response.file.id,
        created_by_user_id = function_user.response.user.id
    )
    response = course_client.create_course(request)
    return CourseFixture(request=request, response=response)