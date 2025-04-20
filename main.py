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

class Necesidad(BaseModel):
    direccion: str
    estado: str
    fecha: str
    urgencia: str
    descripcion: str
    tipo: str

class DatosTarea(BaseModel):
    afectados: List[Necesidad]
    voluntarios: List[Usuario]
    urgencia: str
    categoria: str
    descripcion: str

class DatosCatastrofe(BaseModel):
    #id: int
    nombre: str
    descripcion: str
    TipoCatastrofe: str
    Magnitud: int
    Provincia: str
    EstadoCatastrofe: str

class DatosCatastrofeID(BaseModel):
    id: int
    nombre: str
    descripcion: str
    TipoCatastrofe: str
    Magnitud: int
    Provincia: str
    EstadoCatastrofe: str


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

@app.get("/api/voluntario")
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
            "descripcion": "Encargado de la distribución de materiales y recursos a las zonas afectadas.",
            "id":1
        },
        {
            "foto_perfil": "https://randomuser.me/api/portraits/men/15.jpg",
            "nombre": "Kaladin",
            "apellidos": "García Hernández",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle Gran Vía 10",
            "prioridad": "Baja",
            "categoria": "Logística",
            "descripcion": "Encargado de la distribución de materiales y recursos a las zonas afectadas.",
            "id":2
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
            "descripcion": "Médica especializada en urgencias y atención a heridos.",
            "id":3
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
            "descripcion": "Ingeniero civil encargado de la evaluación de daños estructurales.",
            "id":4
        }
    ]
    return JSONResponse(content=ayudantes, media_type="application/json; charset=utf-8")

@app.get("/api/voluntario/{id}")
def get_usuario_ayudante_por_id(id: int):
    ayudantes = [
        {
            "id":1,
            "foto_perfil": "https://randomuser.me/api/portraits/men/15.jpg",
            "nombre": "Javier",
            "apellidos": "García Hernández",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle Gran Vía 10",
            "prioridad": "Baja",
            "categoria": "Logística",
            "descripcion": "Encargado de la distribución de materiales y recursos a las zonas afectadas.",

        },
        {
            "id":2,
            "foto_perfil": "https://randomuser.me/api/portraits/men/15.jpg",
            "nombre": "Kaladin",
            "apellidos": "García Hernández",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle Gran Vía 10",
            "prioridad": "Baja",
            "categoria": "Logística",
            "descripcion": "Encargado de la distribución de materiales y recursos a las zonas afectadas.",
        },
        {
            "id":3,
            "foto_perfil": "https://randomuser.me/api/portraits/women/22.jpg",
            "nombre": "Ana",
            "apellidos": "Fernández López",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Avenida Diagonal 50",
            "prioridad": "Media",
            "categoria": "Sanidad",
            "descripcion": "Médica especializada en urgencias y atención a heridos.",
        },
        {
            "id":4,
            "foto_perfil": "https://randomuser.me/api/portraits/men/27.jpg",
            "nombre": "David",
            "apellidos": "Martínez González",
            "telefono": "321123321",
            "correo": "ejemplo@gmail.com",
            "direccion": "Calle de la Paz 7",
            "prioridad": "Alta",
            "categoria": "Ingeniería",
            "descripcion": "Ingeniero civil encargado de la evaluación de daños estructurales.",
        }
    ]
    return JSONResponse(content=ayudantes, media_type="application/json; charset=utf-8")




@app.post("/api/tarea")
async def guardar_datos(datos: DatosTarea):
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


@app.put("/api/tarea")
async def guardar_datos(datos: DatosTarea):
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


@app.get("/api/tarea")
def get_tareas():
    tareas = [
        {
            "id": 1,
            "nombre": "Distribuir alimentos",
            "prioridad": "Alta",
            "categoria": "Comida",
            "descripcion": "Repartir alimentos a los afectados en la zona sur.",
            "estado": "Pendiente",
            "usuarios_voluntarios": [
                {
                    "nombre": "Paquito",
                    "apellidos": "Chocolatero",
                    "telefono": "123456789",
                    "correo": "Paquito@gmail.com",
                    "direccion": "CalledePaco 62 8 4",
                    "prioridad": "Alta",
                    "categoria": "Comida",
                    "descripcion": "Repartir alimentos a los afectados en la zona sur.",
                    "foto_perfil": "https://i.pravatar.cc/150?u=Paquito"
                },
                {
                    "nombre": "Pepito",
                    "apellidos": "Casta",
                    "telefono": "234567890",
                    "correo": "Pepito@gmail.com",
                    "direccion": "CalledePaco 61 8 4",
                    "prioridad": "Alta",
                    "categoria": "Comida",
                    "descripcion": "Repartir alimentos a los afectados en la zona sur.",
                    "foto_perfil": "https://i.pravatar.cc/150?u=Pepito"
                }
            ],
            "usuarios_asignados": [{
                "nombre": "Laura",
                "apellidos": "Montenegro",
                "telefono": "654987321",
                "correo": "laura.monte@gmail.com",
                "direccion": "Avenida del Sol 45, 3B",
                "prioridad": "Media",
                "categoria": "Inundación",
                "descripcion": "Ayuda en la evacuación de familias afectadas.",
                "foto_perfil": "https://i.pravatar.cc/150?u=Laura"
                },
                {
                "nombre": "Carlos",
                "apellidos": "Del Río",
                "telefono": "789456123",
                "correo": "carlos.delrio@example.com",
                "direccion": "Calle Lluvia 12, Bajo A",
                "prioridad": "Baja",
                "categoria": "Terremoto",
                "descripcion": "Inspección de viviendas en riesgo estructural.",
                "foto_perfil": "https://i.pravatar.cc/150?u=Carlos"
                }],
            "necesidades": [
                {
                    "direccion": "Avenida de la Libertad 34, Madrid",
                    "estado": "PENDIENTE",
                    "fecha": "2025-04-10",
                    "urgencia": "Media",
                    "descripcion": "Reparación de tendido eléctrico en zona rural.",
                    "tipo": "Incendio"
                },
                {
                    "direccion": "Calle del Mar 14, Valencia",
                    "estado": "CONFIRMADA",
                    "fecha": "2025-04-04",
                    "urgencia": "Baja",
                    "descripcion": "Inspección de viviendas afectadas por inundaciones.",
                    "tipo": "Comida"
                }
            ]
        },
        {
            "id": 2,
            "nombre": "Atención médica",
            "prioridad": "Media",
            "categoria": "Sanidad",
            "descripcion": "Brindar primeros auxilios a los heridos.",
            "estado": "En proceso",
            "usuarios_voluntarios": [{
                "nombre": "Susana",
                "apellidos": "Valverde",
                "telefono": "612345678",
                "correo": "susana.valverde@mail.com",
                "direccion": "Paseo de la Esperanza 21, 2ºD",
                "prioridad": "Alta",
                "categoria": "Rescate",
                "descripcion": "Coordinación de equipos de búsqueda y rescate.",
                "foto_perfil": "https://i.pravatar.cc/150?u=Susana"
                },
            ],
            "usuarios_asignados": [{
                "nombre": "Andrés",
                "apellidos": "Giménez",
                "telefono": "698745632",
                "correo": "andresgimenez@yahoo.es",
                "direccion": "Calle Roble 9, 1ºA",
                "prioridad": "Media",
                "categoria": "Logística",
                "descripcion": "Gestión de suministros y transporte de materiales.",
                "foto_perfil": "https://i.pravatar.cc/150?u=Andres"
                }
            ],
            "necesidades": [
                {
                    "direccion": "Avenida de la Constitución 25, Cádiz",
                    "estado": "EN_ESTUDIO",
                    "fecha": "2025-04-09",
                    "urgencia": "Media",
                    "descripcion": "Evaluación de daños en infraestructuras viales.",
                    "tipo": "Comida"
                },
                {
                    "direccion": "Plaza del Sol 18, Córdoba",
                    "estado": "CONFIRMADA",
                    "fecha": "2025-04-06",
                    "urgencia": "Alta",
                    "descripcion": "Distribución de alimentos y agua a los afectados.",
                    "tipo": "Comida"
                },
                {
                    "direccion": "Carrer de Balmes 45, Barcelona",
                    "estado": "EN_ESTUDIO",
                    "fecha": "2025-04-08",
                    "urgencia": "Alta",
                    "descripcion": "Atención a personas con discapacidad en albergues temporales.",
                    "tipo": "Comida"
                },
            ]
        },
        {
            "id": 3,
            "nombre": "Reconstrucción de viviendas",
            "prioridad": "Alta",
            "categoria": "Reconstrucción",
            "descripcion": "Apoyo en la reconstrucción de viviendas dañadas.",
            "estado": "Completada",
            "usuarios_voluntarios": [{
                "nombre": "Carlos",
                "apellidos": "Giménez",
                "telefono": "698745632",
                "correo": "Carlosgimenez@yahoo.es",
                "direccion": "Calle Roble 10, 1ºA",
                "prioridad": "Media",
                "categoria": "Logística",
                "descripcion": "Gestión de suministros y transporte de materiales.",
                "foto_perfil": "https://i.pravatar.cc/150?u=Andres"
                }],
            "usuarios_asignados": [],
            "necesidades": [
                {
                    "direccion": "Avenida de la Constitución 25, Cádiz",
                    "estado": "EN_ESTUDIO",
                    "fecha": "2025-04-09",
                    "urgencia": "Media",
                    "descripcion": "Evaluación de daños en infraestructuras viales."
                },
                {
                    "direccion": "Plaza del Sol 18, Córdoba",
                    "estado": "CONFIRMADA",
                    "fecha": "2025-04-06",
                    "urgencia": "Alta",
                    "descripcion": "Distribución de alimentos y agua a los afectados."
                },
                {
                    "direccion": "Carrer de Balmes 45, Barcelona",
                    "estado": "EN_ESTUDIO",
                    "fecha": "2025-04-08",
                    "urgencia": "Alta",
                    "descripcion": "Atención a personas con discapacidad en albergues temporales."
                },
            ]
        }
    ]
    return JSONResponse(content=tareas, media_type="application/json; charset=utf-8")


@app.post("/api/catastrofe")
async def guardar_catastrofe(datos: DatosCatastrofe):
    print("Nombre:", datos.nombre)
    print("Descripción:", datos.descripcion)
    print("Tipo de catástrofe:", datos.TipoCatastrofe)
    print("Magnitud:", datos.Magnitud)
    print("Provincia:", datos.Provincia)
    print("Estado:", datos.EstadoCatastrofe)

    return JSONResponse(content={"mensaje": "Catástrofe guardada correctamente"}, status_code=200)


@app.put("/api/catastrofe")
async def actualizar_catastrofe(datos: DatosCatastrofe):
    print("Nombre:", datos.nombre)
    print("Descripción:", datos.descripcion)
    print("Tipo de catástrofe:", datos.TipoCatastrofe)
    print("Magnitud:", datos.Magnitud)
    print("Provincia:", datos.Provincia)
    print("Estado:", datos.EstadoCatastrofe)

    return JSONResponse(content={"mensaje": f"Catástrofe actualizada correctamente"}, status_code=200)

# @app.put("/api/catastrofe/id")
# async def actualizar_catastrofe(id: int, datos: DatosCatastrofe):
#     #print(f"Actualizando catástrofe con ID {id}:")
#     #print("ID:", datos.id)
#     print("Nombre:", datos.nombre)
#     print("Descripción:", datos.descripcion)
#     print("Tipo de catástrofe:", datos.TipoCatastrofe)
#     print("Magnitud:", datos.Magnitud)
#     print("Provincia:", datos.Provincia)
#     print("Estado:", datos.EstadoCatastrofe)

#     return JSONResponse(content={"mensaje": f"Catástrofe actualizada correctamente"}, status_code=200)


@app.get("/api/catastrofe")
def get_tareas():
    tareas = [
        {
            "id": 1,
            "nombre": "Catastrofe 1",
            "tipo": "Comida",
            "magnitud": "Alta",
            "descripcion": "Gotzilla",
            "fechain": "Pendiente",
            "fechaout": "01/04/2001",
            "estado":"Activa"
        },
                {
            "id": 2,
            "nombre": "Catastrofe 2",
            "tipo": "Comida",
            "magnitud": "Alta",
            "descripcion": "Gotzilla Robot",
            "fechain": "Pendiente",
            "fechaout": "01/04/2001",
            "estado":"Activa"
        },
    ]    
    return JSONResponse(content=tareas, media_type="application/json; charset=utf-8")


@app.get("/api/necesidad")
def get_necesidades():
    necesidades = [
        {
            "direccion": "Calle Mayor 12, Sevilla",
            "estado": "EN_ESTUDIO",
            "fecha": "2025-04-10",
            "urgencia": "Alta",
            "descripcion": "Falta de suministros médicos en la zona.",
            "tipo": "Comida"
            
        },
        {
            "direccion": "Av. Andalucía 34, Córdoba",
            "estado": "APROBADA",
            "fecha": "2025-04-09",
            "urgencia": "Media",
            "descripcion": "Necesidad de limpieza de calles.",
            "tipo": "Limpieza"
        
        },
        {
            "direccion": "Calle Real 101, Cádiz",
            "estado": "EN_VIVO",
            "fecha": "2025-04-08",
            "urgencia": "Alta",
            "descripcion": "Entrega urgente de alimentos.",
            "tipo": "Comida"
         
        },
        {
            "direccion": "Camino del Monte 7, Málaga",
            "estado": "CONFIRMADA",
            "fecha": "2025-04-07",
            "urgencia": "Baja",
            "descripcion": "Revisión estructural de viviendas.",
            "tipo": "Comida"  
        },
        {
            "direccion": "Camino de los reyes 7, Málaga",
            "estado": "CONFIRMADA",
            "fecha": "2025-04-07",
            "urgencia": "Baja",
            "descripcion": "Revisión estructural de viviendas.",
            "tipo": "Comida"  
        }
    ]
    return JSONResponse(content=necesidades, media_type="application/json; charset=utf-8")
