from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List
from fastapi import HTTPException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Usuario(BaseModel):
    dni: str
    nombre: str
    apellidos: str
    telefono: str
    correo: str
    direccion: str
    prioridad: str
    categoria: str
    descripcion: str
    fotoPerfil:str

class Necesidad(BaseModel):
    direccion: str
    estado: str
    fecha: str
    urgencia: str
    descripcion: str
    tipo: str

class DatosTarea(BaseModel):
    id:int
    nombre: str
    prioridad: str
    categoria: str
    descripcion: str
    estado: str
    voluntariosAsignados: List[Usuario]
    necesidades: List[Necesidad]
    
class Recurso(BaseModel):
    id: int = None # 'id' es opcional para POST, lo genera el backend
    nombre: str
    categoria: str
    prioridad: str
    descripcion: str
    asignados: int
    maximo: int

class RecursoUpdateAsignados(BaseModel):
    asignados: int

class DatosCatastrofe(BaseModel):
    nombre: str
    descripcion: str
    tipo_catastrofe: str = Field(..., alias="tipo_catastrofe")
    magnitud: int = Field(..., alias="magnitud")
    provincia: str = Field(..., alias="provincia")
    estado_catastrofe: str = Field(..., alias="estado_catastrofe")

class DatosCatastrofeID(BaseModel):
    id: int
    nombre: str
    descripcion: str
    tipo_catastrofe: str = Field(..., alias="tipo_catastrofe")
    magnitud: int = Field(..., alias="magnitud")
    provincia: str = Field(..., alias="provincia")
    estado_catastrofe: str

class DatosDonaciones(BaseModel):
    id_tarea: int
    cantidad_donada: float



recursos_db = [
    {
        "id": 1,
        "nombre": "Agua Potable (Botellas 1L)",
        "categoria": "comida",
        "prioridad": "Alta",
        "descripcion": "Agua embotellada para consumo directo.",
        "asignados": 300,
        "maximo": 1000
    },
    {
        "id": 2,
        "nombre": "Medicamento Analgésico",
        "categoria": "medicamentos",
        "prioridad": "Media",
        "descripcion": "Pastillas para aliviar dolores menores.",
        "asignados": 50,
        "maximo": 200
    },
    {
        "id": 3,
        "nombre": "Tiendas de Campaña",
        "categoria": "Construccion",
        "prioridad": "Alta",
        "descripcion": "Tiendas para 4 personas.",
        "asignados": 10,
        "maximo": 30
    }
]

usuarios = [
        {
            "fotoPerfil": "https://randomuser.me/api/portraits/men/10.jpg",
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
            "fotoPerfil": "https://randomuser.me/api/portraits/women/45.jpg",
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
            "fotoPerfil": "https://randomuser.me/api/portraits/men/32.jpg",
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

ayudantes = [
  {
    "id": 6,
    "nombre": "Lucía",
    "apellidos": "Rodríguez Martínez",
    "telefono": "612345678",
    "correo": "lucia.rm@example.com",
    "direccion": "Calle Mayor 5, 3ºB",
    "prioridad": "Alta",
    "categoria": "Sanidad",
    "descripcion": "Enfermera con experiencia en atención de urgencias.",
    "tipo_tarea": "ATENCION_SANITARIA",
    "zona": "Zona Sur",
    "turno": "MANYANA",
    "fotoPerfil": "https://randomuser.me/api/portraits/women/12.jpg"
  },
  {
    "id": 7,
    "nombre": "Miguel",
    "apellidos": "López Serrano",
    "telefono": "623456789",
    "correo": "miguel.lopez@gmail.com",
    "direccion": "Avenida Libertad 22",
    "prioridad": "Media",
    "categoria": "Ingeniería",
    "descripcion": "Arquitecto voluntario especializado en estructuras de emergencia.",
    "tipo_tarea": "RECONSTRUCCION",
    "zona": "Zona Este",
    "turno": "TARDE",
    "fotoPerfil": "https://randomuser.me/api/portraits/men/33.jpg"
  },
  {
    "id": 8,
    "nombre": "Sofía",
    "apellidos": "González Pérez",
    "telefono": "634567890",
    "correo": "sofia.gp@correo.es",
    "direccion": "Plaza España 1",
    "prioridad": "Baja",
    "categoria": "Psicología",
    "descripcion": "Psicóloga especializada en apoyo a víctimas de catástrofes.",
    "tipo_tarea": "PSICOLOGOS",
    "zona": "Centro",
    "turno": "INDIFERENTE",
    "fotoPerfil": "https://randomuser.me/api/portraits/women/25.jpg"
  },
  {
    "id": 9,
    "nombre": "Andrés",
    "apellidos": "Ruiz Torres",
    "telefono": "645678901",
    "correo": "aruiz.torres@mail.com",
    "direccion": "Camino Real 18",
    "prioridad": "Alta",
    "categoria": "Logística",
    "descripcion": "Encargado de coordinar el transporte de alimentos y ropa.",
    "tipo_tarea": "DISTRIBUCION_DE_ALIMENTOS",
    "zona": "Zona Oeste",
    "turno": "NO_DISPONIBLE",
    "fotoPerfil": "https://randomuser.me/api/portraits/men/40.jpg"
  },
  {
    "id": 10,
    "nombre": "Elena",
    "apellidos": "Navarro Gil",
    "telefono": "656789012",
    "correo": "elena.ng@hotmail.com",
    "direccion": "Calle de la Luz 30",
    "prioridad": "Media",
    "categoria": "Otro",
    "descripcion": "Voluntaria polivalente con formación en primeros auxilios.",
    "tipo_tarea": "EQUIPO_DE_RESCATE",
    "zona": "Zona Norte",
    "turno": "TARDE",
    "fotoPerfil": "https://randomuser.me/api/portraits/women/44.jpg"
  }


    ]

Tareas = [
    {
        "id": 1,
        "nombre": "Distribuir alimentos",
        "tipo_tarea": "Logística",
        "zona": "Zona Sur",
        "turno": "Mañana",
        "prioridad": "Alta",
        "categoria": "Comida",
        "descripcion": "Repartir alimentos a los afectados en la zona sur.",
        "estado": "Pendiente",
        "voluntariosAsignados": [
            {
                "dni": "12345678A",
                "nombre": "Laura",
                "apellidos": "Montenegro",
                "telefono": "654987321",
                "correo": "laura.monte@gmail.com",
                "direccion": "Avenida del Sol 45, 3B",
                "prioridad": "Media",
                "categoria": "Inundación",
                "descripcion": "Ayuda en la evacuación de familias afectadas.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Laura"
            },
            {
                "dni": "87654321B",
                "nombre": "Carlos",
                "apellidos": "Del Río",
                "telefono": "789456123",
                "correo": "carlos.delrio@example.com",
                "direccion": "Calle Lluvia 12, Bajo A",
                "prioridad": "Baja",
                "categoria": "Terremoto",
                "descripcion": "Inspección de viviendas en riesgo estructural.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Carlos"
            },
            {
                "dni": "11223344C",
                "nombre": "Paquito",
                "apellidos": "Chocolatero",
                "telefono": "123456789",
                "correo": "Paquito@gmail.com",
                "direccion": "CalledePaco 62 8 4",
                "prioridad": "Alta",
                "categoria": "Comida",
                "descripcion": "Repartir alimentos a los afectados en la zona sur.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Paquito"
            },
            {
                "dni": "22334455D",
                "nombre": "Pepito",
                "apellidos": "Casta",
                "telefono": "234567890",
                "correo": "Pepito@gmail.com",
                "direccion": "CalledePaco 61 8 4",
                "prioridad": "Alta",
                "categoria": "Comida",
                "descripcion": "Repartir alimentos a los afectados en la zona sur.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Pepito"
            }
        ],
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
        "tipo_tarea": "Emergencia Sanitaria",
        "zona": "Zona Este",
        "turno": "Tarde",
        "prioridad": "Media",
        "categoria": "Sanidad",
        "descripcion": "Brindar primeros auxilios a los heridos.",
        "estado": "En proceso",
        "voluntariosAsignados": [
            {
                "dni": "33445566E",
                "nombre": "Andrés",
                "apellidos": "Giménez",
                "telefono": "698745632",
                "correo": "andresgimenez@yahoo.es",
                "direccion": "Calle Roble 9, 1ºA",
                "prioridad": "Media",
                "categoria": "Logística",
                "descripcion": "Gestión de suministros y transporte de materiales.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Andres"
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
            }
        ]
    },
    {
        "id": 3,
        "nombre": "Reconstrucción de viviendas",
        "tipo_tarea": "Reconstrucción",
        "zona": "Zona Norte",
        "turno": "Completo",
        "prioridad": "Alta",
        "categoria": "Reconstrucción",
        "descripcion": "Apoyo en la reconstrucción de viviendas dañadas.",
        "voluntariosAsignados": [
            {
                "dni": "44556677F",
                "nombre": "Pepe",
                "apellidos": "Gomez",
                "telefono": "698007452",
                "correo": "Carlosgsaimenez@yahoo.es",
                "direccion": "Calle Rsaoble 10, 1ºA",
                "prioridad": "Media",
                "categoria": "Logística",
                "descripcion": "Gestión de suministros y transporte de materiales.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Carlos"
            },
            {
                "dni": "55667788G",
                "nombre": "Carlos",
                "apellidos": "Giménez",
                "telefono": "698745632",
                "correo": "Carlosgimenez@yahoo.es",
                "direccion": "Calle Roble 10, 1ºA",
                "prioridad": "Media",
                "categoria": "Logística",
                "descripcion": "Gestión de suministros y transporte de materiales.",
                "fotoPerfil": "https://i.pravatar.cc/150?u=Carlos"
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
            }
        ]
    }
]

Catastrofes = [
        {
            "id": 1,
            "nombre": "ASDSCatastrofe 1",
            "tipo": "Incendio",
            "magnitud": 3,
            "descripcion": "dasdGotzilla",
            "estado":"Activa"
        },
        {
            "id": 2,
            "nombre": "Catastrofe 2",
            "tipo": "Comida",
            "magnitud": 2,
            "descripcion": "Gotzilla Robot",
            "estado":"Activa"
        },
                {
            "id": 3,
            "nombre": "Dsaatastrofe 2",
            "tipo": "Apagón",
            "magnitud": 1,
            "descripcion": "Dementores",
            "estado":"Finalizada"
        },
    ]    

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

# Para generar IDs únicos
next_recurso_id = max([r['id'] for r in recursos_db]) + 1 if recursos_db else 1


#Metodos de catastrofes

@app.get("/api/catastrofe")
def get_catastrofes():
    return JSONResponse(content=Catastrofes, media_type="application/json; charset=utf-8")

@app.post("/api/catastrofe")
async def guardar_catastrofe(datos: DatosCatastrofeID):
    print("post:")
    print("Nombre:", datos.nombre)
    print("Descripción:", datos.descripcion)
    print("Tipo de catástrofe:", datos.tipo_catastrofe)
    print("Magnitud:", datos.magnitud)
    print("Provincia:", datos.provincia)
    print("Estado:", datos.estado_catastrofe)
    print("...")
    print(datos)

    ids_existentes = [catastrof["id"] for catastrof in Catastrofes]
    ida = max(ids_existentes, default=0) + 1
    datos.id = ida

    cata = {
        "id": ida,
        "nombre": datos.nombre,
        "descripcion": datos.descripcion,
        "tipo": datos.tipo_catastrofe,
        "magnitud": datos.magnitud,
        "provincia": datos.provincia,
        "estado": datos.estado_catastrofe,
    }

    Catastrofes.append(cata)
    return JSONResponse(content={"mensaje": "Catástrofe guardada correctamente"}, status_code=200)

@app.put("/api/catastrofe/{id}")
async def actualizar_catastrofe(id: int, datos: DatosCatastrofeID):
    print(f"Actualizando catástrofe con ID {id}:")
    print("ID:", datos.id)
    print("Nombre:", datos.nombre)
    print("Descripción:", datos.descripcion)
    print("Tipo de catástrofe:", datos.tipo_catastrofe)
    print("Magnitud:", datos.magnitud)
    print("Provincia:", datos.provincia)
    print("Estado:", datos.estado_catastrofe)

    
    # Buscar el índice del elemento con el ID dado
    index = next((i for i, c in enumerate(Catastrofes) if c["id"] == id), None)

    if index is None:
        raise HTTPException(status_code=404, detail="Catástrofe no encontrada")

    # Actualizar los datos
    Catastrofes[index] = {
        "id": datos.id,
        "nombre": datos.nombre,
        "descripcion": datos.descripcion,
        "tipo": datos.tipo_catastrofe,
        "magnitud": datos.magnitud,
        "provincia": datos.provincia,
        "estado": datos.estado_catastrofe,
    }

    return JSONResponse(content={"mensaje": f"Catástrofe actualizada correctamente"}, status_code=200)

@app.delete("/api/catastrofe/{idCatastrofe}")
def eliminar_catastrofe(idCatastrofe: int):
    for index, catastrofe in enumerate(Catastrofes):
        if catastrofe["id"] == idCatastrofe:
            print(catastrofe["id"])
            print(idCatastrofe)
            del Catastrofes[index]
            return JSONResponse(
                content={"mensaje": f"Catástrofe con ID {idCatastrofe} eliminada correctamente"},
                status_code=200
            )
    
    raise HTTPException(status_code=404, detail=f"No se encontró catástrofe con ID {idCatastrofe}")




#Metodos de tareas

@app.get("/api/tarea")
def get_tareas():
    return JSONResponse(content=Tareas, media_type="application/json; charset=utf-8")

@app.get("/api/tarea/{idTarea}")
def get_tareas(idTarea):
    
    tarea=[]
    for i in Tareas:
        if i[id]==idTarea:
            tarea=i

    return JSONResponse(content=tarea, media_type="application/json; charset=utf-8")

@app.post("/api/tarea")
async def crear_tarea(datos: DatosTarea):

    print("Nombre:", datos.nombre)
    print("Descripción:", datos.descripcion)
    print("Prioridad:", datos.prioridad)
    print("Categoría:", datos.categoria)
    print("Estado:", datos.estado)
    print("Voluntarios asignados:", datos.voluntariosAsignados)
    print("Necesidades:", datos.necesidades)

    ids_existentes = [t["id"] for t in Tareas]
    nuevo_id = max(ids_existentes, default=0) + 1 if datos.id == 0 else datos.id

    tarea = {
        "id": nuevo_id,
        "nombre": datos.nombre,
        "descripcion": datos.descripcion,
        "prioridad": datos.prioridad,
        "categoria": datos.categoria,
        "estado": datos.estado,
        "voluntariosAsignados": [v.dict() for v in datos.voluntariosAsignados],
        "necesidades": [n.dict() for n in datos.necesidades]
    }

    Tareas.append(tarea)

    return JSONResponse(content={"mensaje": "Datos guardados correctamente"}, status_code=200)

@app.put("/api/tarea/{id}")
async def modificar_tarea(id: int, datos: DatosTarea):
    print("Nombre:", datos.nombre)
    print("Descripción:", datos.descripcion)
    print("Prioridad:", datos.prioridad)
    print("Categoría:", datos.categoria)
    print("Estado:", datos.estado)
    print("Voluntarios asignados:", datos.voluntariosAsignados)
    print("Necesidades:", datos.necesidades)

    index = next((i for i, c in enumerate(Tareas) if c["id"] == id), None)

    if index is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    Tareas[index] = {
        "id": id,
        "nombre": datos.nombre,
        "descripcion": datos.descripcion,
        "prioridad": datos.prioridad,
        "categoria": datos.categoria,
        "estado": datos.estado,
        "voluntariosAsignados": [v.dict() for v in datos.voluntariosAsignados],
        "necesidades": [n.dict() for n in datos.necesidades]
    }

    return JSONResponse(content={"mensaje": "Tarea modificada correctamente"}, status_code=200)

@app.delete("/api/tarea/{idTarea}")
def eliminar_tarea(idTarea: int):
    for index, tareas in enumerate(Tareas):
        if tareas["id"] == idTarea:
            print(tareas["id"])
            print(idTarea)
            del Tareas[index]
            return JSONResponse(
                content={"mensaje": f"Catástrofe con ID {idTarea} eliminada correctamente"},
                status_code=200
            )
    
    raise HTTPException(status_code=404, detail=f"No se encontró catástrofe con ID {idTarea}")








@app.get("/usuariosAfectados")
def get_usuarios_afectados():
    return JSONResponse(content=usuarios, media_type="application/json; charset=utf-8")

@app.get("/api/voluntario")
def get_usuarios_ayudantes():
    
    return JSONResponse(content=ayudantes, media_type="application/json; charset=utf-8")

@app.get("/api/voluntario/{id}")
def get_usuario_ayudante_por_id(id: int):
    
    return JSONResponse(content=ayudantes, media_type="application/json; charset=utf-8")







@app.get("/api/necesidad")
def get_necesidades():
    
    return JSONResponse(content=necesidades, media_type="application/json; charset=utf-8")

@app.get("/api/donacionesMonetariasTotal")
def get_donaciones():
    donaciones = [
        {"total": 243500}
    ]
    return JSONResponse(content=donaciones, media_type="application/json; charset=utf-8")


@app.post("/api/donacionesMonetarias")
async def guardar_donacionescatastrofe(datos: DatosDonaciones):
    print("Id tareas:", datos.id_tarea)
    print("Dinero donado:", datos.cantidad_donada)

    return JSONResponse(content={"mensaje": "Donacion guardada correctamente"}, status_code=200)



@app.get("/api/panelDonaciones")
def panel_donaciones():
    response_data = {
        "totalRecaudado": "243.500€",
        "donacionesFisicas": 125,
        "donantesActivos": 47,
        "recursosDistribuidos": "68%",

        "donaciones": [
            {
                "fecha": "2025-01-15",
                "fuente": "Empresa X",
                "categoria": "Empresas",
                "importe": "15.000€",
                "estado": "Confirmada"
            },
            {
                "fecha": "2025-02-02",
                "fuente": "Subvención estatal",
                "categoria": "Subvenciones",
                "importe": "25.000€",
                "estado": "Confirmada"
            },
            {
                "fecha": "2025-03-10",
                "fuente": "Juan Pérez",
                "categoria": "Donaciones privadas",
                "importe": "500€",
                "estado": "Pendiente"
            },
            {
                "fecha": "2025-04-05",
                "fuente": "Evento solidario",
                "categoria": "Eventos",
                "importe": "3.200€",
                "estado": "Confirmada"
            }
        ],

        "distribucionTipos": {
            "Monetarias": 65,
            "Alimentos": 18,
            "Herramientas": 12,
            "Medicamentos": 5
        },

        "evolucionMensual": [12000, 18000, 14500, 17000, 22000]
    }

    return JSONResponse(content=response_data, media_type="application/json; charset=utf-8")