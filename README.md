# 🚀 Azure Functions VM Management

## 📋 Descripción

Sistema completo de gestión de máquinas virtuales en Azure utilizando Azure Functions. Permite crear, gestionar y monitorear VMs de forma automática con una API REST completa.

## 🏗️ Arquitectura

- **Azure Functions**: API REST para gestión de VMs
- **CosmosDB**: Base de datos para metadata de VMs
- **Azure Key Vault**: Almacenamiento seguro de claves SSH
- **Azure Monitor**: Monitoreo automático de VMs
- **Timer Triggers**: Sincronización automática cada 5 minutos

## 🎯 Funcionalidades

### 🖥️ Gestión de VMs
- ✅ Crear VMs con configuración personalizada
- ✅ Listar todas las VMs
- ✅ Obtener detalles específicos de VM
- ✅ Eliminar VMs y recursos asociados
- ✅ Redimensionar VMs

### 🔑 Gestión SSH
- ✅ Generación automática de claves SSH
- ✅ Almacenamiento seguro en Key Vault
- ✅ Recuperación de claves para acceso

### 📊 Monitoreo
- ✅ Health Check del sistema
- ✅ Monitoreo automático de estado de VMs
- ✅ Sincronización periódica
- ✅ Logs detallados en Application Insights

## 🚀 Endpoints Disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/health` | Health check del sistema |
| GET | `/api/vms` | Listar todas las VMs |
| POST | `/api/vms` | Crear nueva VM |
| GET | `/api/vms/{name}` | Obtener detalles de VM |
| DELETE | `/api/vms/{name}` | Eliminar VM |
| GET | `/api/ssh-keys/{name}` | Obtener claves SSH |
| PUT | `/api/vms/{name}/resize` | Redimensionar VM |

## 🧪 Testing con Postman

### Archivos Incluidos
- `postman_collection_production.json` - Colección completa
- `postman_environment_production.json` - Variables de entorno
- `README_POSTMAN.md` - Guía rápida
- `GUIA_POSTMAN_PRODUCCION.md` - Guía detallada

### Inicio Rápido
1. Importar archivos JSON en Postman
2. Seleccionar entorno de producción
3. Ejecutar secuencia de pruebas

## 📚 Documentación

- **`MIND_MAP_ARQUITECTURA.md`** - Arquitectura completa del sistema
- **`README_POSTMAN.md`** - Guía rápida de testing
- **`GUIA_POSTMAN_PRODUCCION.md`** - Guía detallada de Postman
- **`RESUMEN_COMPLETADO.md`** - Estado actual del proyecto

## 🔧 Configuración

### Variables de Entorno Requeridas
```
AZURE_SUBSCRIPTION_ID=your_subscription_id
AZURE_TENANT_ID=your_tenant_id
AZURE_CLIENT_ID=your_client_id
AZURE_CLIENT_SECRET=your_client_secret
COSMOSDB_CONNECTION_STRING=your_cosmosdb_connection
KEY_VAULT_URL=your_keyvault_url
API_KEY=your_api_key
```

### Tamaños de VM Disponibles
- **small**: Standard_B1s (1 vCPU, 1GB RAM)
- **medium**: Standard_B2s (2 vCPU, 4GB RAM)
- **large**: Standard_B4ms (4 vCPU, 16GB RAM)

## 🌐 Ambientes

### Producción
- **Function App**: `vm-az-functions-demo`
- **URL**: `https://vm-az-functions-demo.azurewebsites.net`
- **Resource Group**: `rg-vm-functions-demo`

### Desarrollo
- **Function App**: `vm-az-functions-dev`
- **Resource Group**: `rg-vm-functions-dev`

## 🔒 Seguridad

- **Autenticación**: API Key en header `x-api-key`
- **Claves SSH**: Almacenadas en Azure Key Vault
- **Network Security Groups**: Configurados automáticamente
- **RBAC**: Permisos mínimos necesarios

## 📊 Monitoreo Automático

- **Timer Trigger**: Cada 5 minutos
- **Health Checks**: Verificación continua
- **Application Insights**: Métricas y logs
- **Azure Monitor**: Alertas automáticas

## 🚨 Consideraciones Importantes

### 💰 Costos
- Las VMs generan costos mientras estén ejecutándose
- Eliminar VMs de prueba después de usar
- Usar tamaños pequeños para testing

### ⏱️ Tiempos Típicos
- Creación de VM: 3-5 minutos
- Eliminación de VM: 2-3 minutos
- Health Check: < 5 segundos

## 🆘 Troubleshooting

### Errores Comunes
- **401 Unauthorized**: Verificar API Key
- **500 Internal Error**: Revisar Health Check
- **Timeout**: Operaciones de VM pueden tomar varios minutos

### Logs
- Azure Portal → Function App → Monitor
- Application Insights para métricas detalladas

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear branch para feature
3. Commit de cambios
4. Push al branch
5. Crear Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

**🎯 Sistema completo y funcional para gestión de VMs en Azure con monitoreo automático y testing integrado.**