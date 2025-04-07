from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model para definir la estructura de los datos
class Usuario(BaseModel):
    nombre: str
    apellidos: str
    telefono: str
    correo: str
    direccion: str
    prioridad: str
    categoria: str
    descripcion: str

class DatosGuardar(BaseModel):
    afectados: List[Usuario]
    voluntarios: List[Usuario]
    urgencia: str
    categoria: str
    descripcion: str

@app.get("/usuariosAfectados")
def get_usuarios_afectados():
    usuarios = [
        {
            "foto_perfil": "https://randomuser.me/api/portraits/men/10.jpg",
            "nombre": "Carlos",
            "apellidos": "Martínez López",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle Río Guadalquivir 14",
            "prioridad": "Alta",
            "categoria": "Reconstrucción",
            "descripcion": "Casa gravemente dañada por inundaciones. Necesita reconstrucción urgente."
        },
        {
            "foto_perfil": "https://randomuser.me/api/portraits/women/45.jpg",
            "nombre": "Lucía",
            "apellidos": "Gómez Pérez",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Avenida del Sol 22",
            "prioridad": "Media",
            "categoria": "Limpieza",
            "descripcion": "Zona afectada por barro y escombros. Se requiere equipo de limpieza."
        },
        {
            "foto_perfil": "https://randomuser.me/api/portraits/men/32.jpg",
            "nombre": "Andrés",
            "apellidos": "Ruiz Sánchez",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Camino de la Sierra 5",
            "prioridad": "Baja",
            "categoria": "Solicitar recursos",
            "descripcion": "Falta de agua potable y alimentos. Solicita recursos básicos."
        }
    ]
    return JSONResponse(content=usuarios, media_type="application/json; charset=utf-8")

@app.get("/usuariosAyudantes")
def get_usuarios_ayudantes():
    ayudantes = [
        {
            "foto_perfil": "https://randomuser.me/api/portraits/men/15.jpg",
            "nombre": "Javier",
            "apellidos": "García Hernández",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle Gran Vía 10",
            "prioridad": "Baja",
            "categoria": "Logística",
            "descripcion": "Encargado de la distribución de materiales y recursos a las zonas afectadas."
        },
        {
            "foto_perfil": "https://randomuser.me/api/portraits/women/22.jpg",
            "nombre": "Ana",
            "apellidos": "Fernández López",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Avenida Diagonal 50",
            "prioridad": "Media",
            "categoria": "Sanidad",
            "descripcion": "Médica especializada en urgencias y atención a heridos."
        },
        {
            "foto_perfil": "https://randomuser.me/api/portraits/men/27.jpg",
            "nombre": "David",
            "apellidos": "Martínez González",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle de la Paz 7",
            "prioridad": "Alta",
            "categoria": "Ingeniería",
            "descripcion": "Ingeniero civil encargado de la evaluación de daños estructurales."
        }
    ]
    return JSONResponse(content=ayudantes, media_type="application/json; charset=utf-8")

@app.post("/guardarDatos")
async def guardar_datos(datos: DatosGuardar):
    afectados = datos.afectados
    voluntarios = datos.voluntarios
    urgencia = datos.urgencia
    categoria = datos.categoria
    descripcion = datos.descripcion

    print("Afectados:", afectados)
    print("Voluntarios:", voluntarios)
    print("Uregencia:", urgencia)
    print("Categoria:", categoria)
    print("Descripcion:", descripcion)

    return JSONResponse(content={"mensaje": "Datos guardados correctamente"}, status_code=200)


@app.get("/tareas")
def get_tareas():
    tareas = [
        {
            "id": 1,
            "nombre": "Distribuir alimentos",
            "prioridad": "Alta",
            "categoria": "Comida",
            "descripcion": "Repartir alimentos a los afectados en la zona sur.",
            "estado": "Pendiente",
            "voluntarios": [],
            "afectados": []
        },
        {
            "id": 2,
            "nombre": "Atención médica",
            "prioridad": "Media",
            "categoria": "Sanidad",
            "descripcion": "Brindar primeros auxilios a los heridos.",
            "estado": "En proceso",
            "voluntarios": [],
            "afectados": []
        },
        {
            "id": 3,
            "nombre": "Reconstrucción de viviendas",
            "prioridad": "Alta",
            "categoria": "Reconstrucción",
            "descripcion": "Apoyo en la reconstrucción de viviendas dañadas.",
            "estado": "Completada",
            "voluntarios": [],
            "afectados": []
        }
    ]
    return JSONResponse(content=tareas, media_type="application/json; charset=utf-8")
