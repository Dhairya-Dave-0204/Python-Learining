from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRE_USER: str
    POSTGRE_PASSWORD: str
    POSTGRE_HOST: str
    POSTGRE_PORT: str = "5432" # You can provide a default value if you want
    POSTGRE_DB: str

    JWT_SECRET_KEY: str
    ALGORITHM: str
    EXP_TIME: int

    @property
    def DB_CONNECTION(self) -> str:
        """
            Dynamically builds the database URL.
            Format: postgresql://user:password@host:port/database
        """

        return f"postgresql://{self.POSTGRE_USER}:{self.POSTGRE_PASSWORD}@{self.POSTGRE_HOST}:{self.POSTGRE_PORT}/{self.POSTGRE_DB}"

settings = Setting()