from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base


class Record(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = None
    temperature: Mapped[float] = None
    humidity: Mapped[float] = None
    device_id: Mapped[str] = mapped_column(ForeignKey("devices.id"))
    device: Mapped["Device"] = relationship("Device", back_populates="records")

    def __repr__(self) -> str:
        return f"Record(id={self.id}, timestamp={self.timestamp}, device_id={self.device_id}, temperature={self.temperature}°C, humidity={self.humidity}%)"


from models.device import Device
