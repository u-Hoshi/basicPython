## アプリケーションの起動

main.py の起動方法：`uvicorn sql_app.main:app --reload`

streamlit(app.py)の起動方法：`streamlit run app.py`

自動ドキュメント：`http://localhost:8000/redoc` or `http://localhost:8000/docs`

### メモ

models.py は SQLAlchemy 側の構造

schemas.py は FastAPI 側の構造
