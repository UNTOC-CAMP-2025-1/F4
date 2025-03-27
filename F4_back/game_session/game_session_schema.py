'''from pydantic import BaseModel
from datetime import datetime

# ���� ���� �� ���� Pydantic ��. Ŭ���̾�Ʈ�� ���� ������ ���� ������
class GameSessionCreate(BaseModel):
  user_id: int
  user_score: int
  session_started_at: datetime
  session_ended_at: datetime

# ���� ������Ʈ �� ���� Pydantic ��
class GameSessionUpdate(BaseModel):
  user_score: int
  session_started_at: datetime
  session_ended_at: datetime

# ���� �� ����� ��. API���� ��ȯ�� ���� �𵨵�
class GameSessionResponse(BaseModel):
  user_id: int
  user_score: int
  session_id: int
  session_started_at: datetime
  session_ended_at: datetime
'''
from pydantic import BaseModel
from datetime import datetime

class GameSessionCreate(BaseModel):
    user_score: int | None = None
    session_started_at: datetime
    session_ended_at: datetime

class GameSessionResponse(BaseModel):
    session_id: int
    user_id: int
    user_score: int | None = None
    session_started_at: datetime
    session_ended_at: datetime

    class Config:
        orm_mode = True