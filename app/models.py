from app import db
from sqlalchemy import Text, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime, timezone
import zoneinfo

class Pokemon(db.Model):
  __tablename__ = 'pokemon'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
  description: Mapped[str] = mapped_column(Text, nullable=False)
  weight: Mapped[float] = mapped_column(Float, nullable=False)
  height: Mapped[float] = mapped_column(Float, nullable=False)
  img_url: Mapped[str] = mapped_column(Text, nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(zoneinfo.ZoneInfo('localtime')))
  # created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

  def __repr__(self):
    return f'<Pokemon: {self.name}>'