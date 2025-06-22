# Base de datos adminsitrador de actividades
TABLE_CONTROL_FIELDS = {
    "usercreationid":       "UsuarioCreacionId",
    "creationdate":         "FechaCreacion",
    "usermodificationid":   "UsuarioModificacionId",
    "modificationdate":     "FechaModificacion",
    "userlowid":            "UsuarioBajaId",
    "lowdate":              "FechaBaja",
    "low":                  "Baja"
}

TAREA_TABLE_NAMES = {
    "table":        "TAREA",
    "id":           "TareaId",
    "description":  "Descripcion"
}

RECURSOHUMANO_TABLE_NAMES = {
    "table":            "RECURSOHUMANO",
    "id":               "RecursoHumanoId",
    "name":             "Nombre",
    "paternal_surname": "APP",
    "maternal_surname": "APM",
    "position":         "PUESTO"
}

ACTIVIDAD_TABLE_NAMES = {
    "table":            "ACTIVIDAD",
    "id":               "ActividadId", 
    "tareaid":          TAREA_TABLE_NAMES["id"],
    "recursohumanoid":  RECURSOHUMANO_TABLE_NAMES["id"],
    "note":             "NOTA",
    "startdate":        "FechaInicio",
    "enddate":          "FechaFin",
    "hours":            "HORAS"
}


# Agregar a todas las tablas los campos de control
TAREA_TABLE_NAMES.update( TABLE_CONTROL_FIELDS )
RECURSOHUMANO_TABLE_NAMES.update( TABLE_CONTROL_FIELDS )
ACTIVIDAD_TABLE_NAMES.update( TABLE_CONTROL_FIELDS )




# Nombres de base de datos Administración de Actividad. Tablas
ADA_DATABASE_NAMES = {
    "name":             "administracionDeActividad",
    "tarea":            TAREA_TABLE_NAMES,
    "recursohumano":    RECURSOHUMANO_TABLE_NAMES,
    "actividad":        ACTIVIDAD_TABLE_NAMES
}