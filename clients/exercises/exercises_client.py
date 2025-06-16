from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса для создания упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса, для обновления упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений по courseId.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises",params=query)


    def get_exercise_api(self, exercise_id : str) -> Response:
        """
        Метод получения упражнения по его идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, orderIndex, description,
        estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения по идентификатору.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
