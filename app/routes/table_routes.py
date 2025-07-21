from fastapi import APIRouter, Request
from fastapi.params import Body, Depends

from app.controllers.table_controller import TableController
from app.shared.middlewares.auth import auth_middleware
from app.factories.controllers import table_controller_factory
from app.shared.types.session import AuthSession

router = APIRouter(prefix = "/table", tags=["Table"])

@router.post("/")
async def create_table(
  request: Request,
  data: dict = Body(...),
  controller: TableController = Depends(table_controller_factory),
  _: None = Depends(auth_middleware)
):
  session: AuthSession = request.session
  return await controller.create_table(session, data)

@router.put("/{table_id}")
async def update_table(
  request: Request,
  table_id: str,
  data: dict = Body(...),
  controller: TableController = Depends(table_controller_factory),
  _: None = Depends(auth_middleware),
):
  session: AuthSession = request.session
  return await controller.update_table(session, table_id, data)