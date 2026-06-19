from fastapi import APIRouter

from routes.create_task import create_task
from routes.delete_task import delete_task
from routes.done_task import done_task
from routes.list_tasks import list_tasks

router = APIRouter(prefix="/v1/tasks")

router.add_api_route("", list_tasks, methods=["GET"], tags=["tasks"])
router.add_api_route("", create_task, methods=["POST"], tags=["tasks"])
router.add_api_route("/{task_id}/done", done_task, methods=["PATCH"], tags=["tasks"])
router.add_api_route("/{task_id}", delete_task, methods=["DELETE"], tags=["tasks"])
