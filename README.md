
# Legal AI MVP

## 구성
- React 프론트엔드 (포트 3000)
- FastAPI 백엔드 (포트 8000)
- LangChain + Chroma 벡터 DB
- `vectorize.py`로 문서 벡터화

## 실행
```bash
docker-compose up --build
```

## 문서 벡터화
```bash
cd backend
python vectorize.py
```
