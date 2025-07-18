from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class NotificacionCaso(BaseModel):
    denunciante_id: Optional[str]
    device_id: Optional[str]
    fecha_hora: Optional[str]
    razon_sentencia: Optional[str]
    veredicto: Optional[str]
    lugar_reclusion: Optional[str]
    conclusion: Optional[str]
    fecha_creacion: Optional[datetime]
