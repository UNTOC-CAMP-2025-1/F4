from fastapi import APIRouter
from .game_session_schema import GameSessionCreate, GameSessionUpdate, GameSessionResponse
from typing import List

router = APIRouter(
  prefix="/game_session"
)

# ���� ������ (�����δ� �����ͺ��̽����� �������� ������� �ݿ��ϱ�)
game_sessions = [
    {"user_id": 1, "user_score": 500,"session_id": 1, "session_started_at": "2025-03-24T10:00:00", "session_ended_at": "2025-03-24T10:30:00"},
    {"user_id": 2, "user_score": 1000,"session_id": 2, "session_started_at": "2025-03-24T11:00:00", "session_ended_at": "2025-03-24T11:30:00"}
    # �� ���� ������ �߰� ����
]

# / ��Ʈ ���
# API�� ����� �۵��ϴ��� Ȯ���ϴ� �⺻ ���
# /game_session/ ��ο� �����ϸ� �޼��� ��ȯȯ
@router.get("/")
def root():
  return {"message": "Hello from Game Session Router"}

# /get_session ���
# game_sessions ��Ͽ��� skip�� limit�� �̿��Ͽ� ���� ���� ��� ��ȸ
# skip: ��ȸ ���� ����, limit: �� ���� ������ ������ ���� 
@router.get("/get_sessions", response_model=List[GameSessionResponse])
def get_sessions(skip: int=0, limit: int=10): # �⺻�� �����س�����
  return game_sessions[skip: skip + limit]

# /get_sessions/{session_id} ���
# session_id�� ��� �Ű������� �޾Ƽ� �ش� ID�� ���� ���� ��ȸ
# game_sessions ����� ���������� Ȯ���Ͽ� session_id�� ��ġ�ϴ� ������ ã�� ��ȯ
# ������ ã�� �� ���ٸ� {"error": "Session not found"}��� ���� �޼��� ��ȯ
@router.get("/get_session/{session_id}", response_model=GameSessionResponse)
def get_session(session_id: int):
  for session in game_sessions:
    if session["session_id"] == session_id:
      return session
  return {"error": "Session not found"}
  
# ���ο� ���� ���� ����
# session_id�� �ڵ����� �����ǵ��� len(game_sessions)+1�� ����, �������� ��û�� ����
# ���ο� ������ game_sesisons ��Ͽ� �߰��� ��, ������ ���� ���� ��ȯ
@router.post("/create_session", response_model=GameSessionResponse)
def create_session(session: GameSessionCreate):
  new_session = {
    "user_id" : session.user_id,
    "user_score": session.user_score,
    "session_id": len(game_sessions) + 1,
    "session_started_at": session.session_started_at,
    "session_ended_at": session.session_ended_at
  }
  game_sessions.append(new_session)
  return new_session
  
# ���� ���� ������Ʈ 
# GameSessionUpdate ���� Python ��ųʸ��� ��ȯ�Ͽ� ���� ���ǿ� ������Ʈ
@router.put("/update_session/{session_id}", response_model=GameSessionResponse)
def update_session(session_id: int, session: GameSessionUpdate):
  for idx, existing_session in enumerate(game_sessions):
    if existing_session["session_id"] == session_id:
      # Pydantic ���� model_dump()�� ��ųʸ��� ��ȯ�Ͽ� ������ƮƮ
      game_sessions[idx].update(session.model_dump()) 
      return game_sessions[idx]
    return {"error": "Session not found"}
  
# ���� ���� ����
# session_id�� �ش��ϴ� ���� ������ game_sessions ����Ʈ���� ����
@router.delete("/delete_session/{session_id}")
def delete_session(session_id: int):
  for idx, session in enumerate(game_sessions):
    if session["session_id"] == session_id:
      del game_sessions[idx] # ���� ����
      return {"message": f"Session with ID {session_id} has been deleted"}
  return {"error": "Session not found"}
