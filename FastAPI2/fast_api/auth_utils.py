import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta
from decouple import config

JWT_KEY = config("JWT_KEY")

# 認証関連をまとめたクラス
class AuthJwtCsrf:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_key = JWT_KEY

    def generate_hashed_pw(self, password) -> str:
        # 引数にはユーザーがフォームでタイピングしたパスワード(pw)を受け取り、それをハッシュ化したものを返す
        return self.pwd_ctx.hash(password)

    def verify_pw(self, plain_pw, hashed_pw) -> bool:
        # 引数にはユーザーがフォームに入力した平文のpwとdbに保存されてるハッシュ化したpwを受け取る
        # 二つを比較し一致したらTrueを返す
        return self.pwd_ctx.verify(plain_pw, hashed_pw)

    def encode_jwt(self, email) -> str:
        # JWTを生成する
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),  # JWTの有効期限
            "iat": datetime.utcnow(),  # JWTが生成された日時
            "sub": email,  # ユーザーを判断する一意のもの
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def decode_jwt(self, token) -> str:
        # JWTを解析するメソッド
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="The JWT has expired")
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="JWT is not valid")
