from api_client_create_course import create_course_response
from api_client_create_course import authentication_user

from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_client import CreateExercisesRequestDict
from clients.exercises.exercises_client import UpdateExercisesRequestDict
from clients.exercises.exercises_client import GetExercisesQueryDict


exercises_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExercisesRequestDict(
    title="Python",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=0,
    description="Python API",
    estimatedTime="2 weeks"
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)

exercise_id = create_exercise_response['id']
course_id = create_exercise_response['courseId']

get_exercise_response = exercises_client.get_exercise(exercise_id)
print("Get exercise data: ", get_exercise_response)

get_exercises_query = GetExercisesQueryDict(courseId=course_id)
get_exercises_response = exercises_client.get_exercises(get_exercises_query)
print("Get exercises list: ", get_exercises_response)


update_request = UpdateExercisesRequestDict(
    title="Update Python",
    maxScore=100,
    minScore=10,
    orderIndex=1,
    description="Update_Python API",
    estimatedTime="3 weeks"
)

update_exercise_response = exercises_client.update_exercise(exercise_id, update_request)
print("Update exercise data: ", update_exercise_response)
