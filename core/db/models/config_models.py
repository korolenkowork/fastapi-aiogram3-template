from sqlalchemy.orm import mapped_column, Mapped

from core.shared.models import Base


class Config(Base):
    __tablename__ = "config"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]