from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = None
    records: Mapped[list["Record"]] = relationship("Record", back_populates="device")

    def __repr__(self) -> str:
        return f"Device(id={self.id}, name={self.name})"

from models.record import Record
