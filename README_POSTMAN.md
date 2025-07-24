# 🚀 Guía Rápida: Testing con Postman

## 📁 Archivos Incluidos

- **`postman_collection_production.json`** - Colección completa con todos los endpoints
- **`postman_environment_production.json`** - Variables de entorno preconfiguradas
- **`GUIA_POSTMAN_PRODUCCION.md`** - Guía detallada paso a paso

## ⚡ Inicio Rápido (5 minutos)

### 1. Importar en Postman
```
1. Abrir Postman
2. Import → Upload Files
3. Seleccionar ambos archivos JSON
4. Confirmar importación
```

### 2. Configurar Entorno
```
1. Seleccionar entorno "Azure Functions VM Management - Producción"
2. Verificar que las variables estén cargadas
3. ¡Listo para probar!
```

### 3. Secuencia de Pruebas Recomendada

| Orden | Endpoint | Propósito |
|-------|----------|----------|
| 1️⃣ | 🏥 Health Check | Verificar que el sistema esté funcionando |
| 2️⃣ | 📋 List VMs | Ver VMs existentes |
| 3️⃣ | 🆕 Create VM | Crear VM de prueba |
| 4️⃣ | 🔍 Get VM Details | Verificar detalles de la VM creada |
| 5️⃣ | 🔑 Get SSH Key | Obtener claves SSH |
| 6️⃣ | 🗑️ Delete VM | Limpiar recursos de prueba |

## 🎯 Endpoints Disponibles

### 🏥 Health Check
- **URL**: `GET /api/health`
- **Auth**: No requerida
- **Propósito**: Verificar estado del sistema

### 📋 List VMs
- **URL**: `GET /api/vms`
- **Auth**: x-api-key
- **Propósito**: Listar todas las VMs

### 🆕 Create VM
- **URL**: `POST /api/vms`
- **Auth**: x-api-key
- **Body**: JSON con configuración de VM
- **Propósito**: Crear nueva VM

### 🔍 Get VM Details
- **URL**: `GET /api/vms/{vm_name}`
- **Auth**: x-api-key
- **Propósito**: Obtener detalles específicos

### 🔑 Get SSH Key
- **URL**: `GET /api/ssh-keys/{vm_name}`
- **Auth**: x-api-key
- **Propósito**: Obtener claves SSH

### 🗑️ Delete VM
- **URL**: `DELETE /api/vms/{vm_name}`
- **Auth**: x-api-key
- **Propósito**: Eliminar VM

## 🔧 Variables de Entorno

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `base_url` | `https://vm-az-functions-demo.azurewebsites.net` | URL base de la API |
| `api_key` | `pGfZb--H1Svjo_1x5cjcbfssPEAuHflwk_DQEaIzvMk` | Clave de autenticación |
| `test_vm_name` | `postman-test-vm` | Nombre base para VMs de prueba |
| `created_vm_name` | (automático) | Se llena al crear una VM |

## ✅ Tests Automáticos

Cada endpoint incluye tests automáticos que verifican:
- ✅ Código de estado HTTP correcto
- ✅ Estructura de respuesta válida
- ✅ Campos requeridos presentes
- ✅ Valores esperados

## 🚨 Consideraciones Importantes

### 💰 Costos
- Crear VMs genera costos en Azure
- Siempre eliminar VMs de prueba después de usar
- Usar tamaños pequeños para testing

### ⏱️ Tiempos
- Creación de VM: 3-5 minutos
- Eliminación de VM: 2-3 minutos
- Health Check: < 5 segundos
- List VMs: < 10 segundos

### 🔒 Seguridad
- La API Key está incluida para facilitar testing
- En producción real, usar variables de entorno seguras
- No compartir la API Key públicamente

## 🆘 Troubleshooting

### Error 401 - Unauthorized
```
- Verificar que la API Key esté correcta
- Confirmar que el header x-api-key esté presente
- Revisar que el entorno esté seleccionado
```

### Error 500 - Internal Server Error
```
- Verificar el Health Check primero
- Revisar logs en Azure Portal
- Confirmar que los servicios de Azure estén disponibles
```

### VM Creation Timeout
```
- La creación puede tomar hasta 5 minutos
- Verificar en Azure Portal si la VM se está creando
- Revisar logs de la Function App
```

## 📞 Soporte

Para más detalles, consultar:
- `GUIA_POSTMAN_PRODUCCION.md` - Guía completa
- `MIND_MAP_ARQUITECTURA.md` - Arquitectura del sistema
- Logs en Azure Portal para debugging

---

**¡Happy Testing! 🎉**