# 🗺️ Mind Map: Arquitectura Azure Functions VM Management

## 🏗️ Estructura General

```
Azure Functions VM Management
├── 🌐 PRODUCCIÓN
│   ├── Function App: vm-az-functions-demo
│   ├── Resource Group: rg-vm-functions-demo
│   ├── Region: East US
│   └── Tier: Consumption Plan
│
├── 🧪 DESARROLLO
│   ├── Function App: vm-az-functions-dev
│   ├── Resource Group: rg-vm-functions-dev
│   ├── Region: East US
│   └── Tier: Consumption Plan
│
└── 🔧 COMPONENTES COMPARTIDOS
    ├── Azure Key Vault
    ├── CosmosDB
    ├── Storage Account
    └── Application Insights
```

## 🎯 Endpoints Principales

### 🏥 Health Check
- **Endpoint**: `GET /api/health`
- **Autenticación**: No requerida
- **Propósito**: Verificar estado del sistema
- **Respuesta**: Estado de servicios Azure

### 🖥️ Gestión de VMs
- **Listar VMs**: `GET /api/vms`
- **Crear VM**: `POST /api/vms`
- **Obtener VM**: `GET /api/vms/{name}`
- **Eliminar VM**: `DELETE /api/vms/{name}`
- **Redimensionar VM**: `PUT /api/vms/{name}/resize`

### 🔑 Gestión SSH
- **Obtener Claves**: `GET /api/ssh-keys/{name}`
- **Ejecutar Comando**: `POST /api/ssh-command/{name}`

### 📊 Monitoreo
- **Estado VM**: `GET /api/vm-status/{name}`
- **Sincronizar VMs**: `POST /api/sync-vms`

## 🤖 Servicios Automáticos

### ⏰ Timer Triggers
- **VMStatusMonitor**: Cada 5 minutos
  - Monitorea estado de VMs
  - Actualiza base de datos
  - Registra cambios de estado

### 🔄 Event Triggers
- **NotifyKyubo**: Notificaciones automáticas
- **SyncVMs**: Sincronización periódica

## 💾 Almacenamiento

### 🗄️ CosmosDB
```
Containers:
├── vms
│   ├── Partition Key: /name
│   ├── Documents: VM metadata
│   └── TTL: No configurado
│
├── ssh_keys
│   ├── Partition Key: /vm_name
│   ├── Documents: Claves SSH
│   └── TTL: No configurado
│
└── vm_status
    ├── Partition Key: /vm_name
    ├── Documents: Estados históricos
    └── TTL: 30 días
```

### 🔐 Azure Key Vault
```
Secrets:
├── cosmosdb-connection-string
├── azure-subscription-id
├── azure-tenant-id
├── azure-client-id
├── azure-client-secret
└── ssh-private-keys (por VM)
```

## ☁️ Infraestructura Azure

### 🏢 Resource Groups
- **Producción**: `rg-vm-functions-demo`
- **Desarrollo**: `rg-vm-functions-dev`
- **VMs Creadas**: `rg-{vm-name}`

### 🌐 Networking
```
Red Virtual:
├── VNet: vnet-{vm-name}
├── Subnet: subnet-{vm-name}
├── NSG: nsg-{vm-name}
│   ├── SSH (22): Permitido
│   ├── HTTP (80): Permitido
│   └── HTTPS (443): Permitido
└── Public IP: pip-{vm-name}
```

### 💻 Compute
```
Tamaños de VM:
├── small: Standard_B1s (1 vCPU, 1GB RAM)
├── medium: Standard_B2s (2 vCPU, 4GB RAM)
└── large: Standard_B4ms (4 vCPU, 16GB RAM)

Sistema Operativo:
├── Ubuntu 20.04 LTS
├── Configuración SSH automática
└── Claves SSH generadas dinámicamente
```

## 🔄 Flujo de Datos

### 📥 Creación de VM
```
1. Request → CreateVM Function
2. Validar parámetros
3. Generar claves SSH
4. Crear recursos Azure
5. Guardar metadata → CosmosDB
6. Almacenar SSH → Key Vault
7. Response con detalles
```

### 📤 Eliminación de VM
```
1. Request → DeleteVM Function
2. Obtener metadata → CosmosDB
3. Eliminar recursos Azure
4. Limpiar CosmosDB
5. Limpiar Key Vault
6. Response confirmación
```

### 📊 Monitoreo Automático
```
1. Timer Trigger (5 min)
2. Listar VMs → Azure
3. Obtener estado → Azure
4. Comparar con CosmosDB
5. Actualizar diferencias
6. Log cambios
```

## ⚙️ Configuración por Ambiente

### 🌐 Producción
```
App Settings:
├── COSMOSDB_CONNECTION_STRING
├── AZURE_SUBSCRIPTION_ID
├── AZURE_TENANT_ID
├── AZURE_CLIENT_ID
├── AZURE_CLIENT_SECRET
├── KEY_VAULT_URL
└── API_KEY
```

### 🧪 Desarrollo
```
App Settings:
├── COSMOSDB_CONNECTION_STRING (dev)
├── AZURE_SUBSCRIPTION_ID
├── AZURE_TENANT_ID
├── AZURE_CLIENT_ID
├── AZURE_CLIENT_SECRET
├── KEY_VAULT_URL (dev)
└── API_KEY (dev)
```

## 🚀 Pipeline de Despliegue

### 📦 GitHub Actions
```
Workflows:
├── ci.yml: Tests y validación
├── deploy.yml: Despliegue automático
└── dependency-update.yml: Actualizaciones
```

### 🔄 Proceso de Deploy
```
1. Push → GitHub
2. Trigger → GitHub Actions
3. Tests → Pytest
4. Build → Azure Functions
5. Deploy → Production/Dev
6. Health Check → Verificación
```

## 🔒 Seguridad

### 🛡️ Autenticación
- **API Key**: Header `x-api-key`
- **Azure AD**: Service Principal
- **Key Vault**: Managed Identity

### 🔐 Secretos
- **Claves SSH**: Almacenadas en Key Vault
- **Connection Strings**: App Settings
- **API Keys**: Configuración segura

### 🚫 Acceso
- **NSG Rules**: Puertos específicos
- **RBAC**: Permisos mínimos
- **Claves SSH**: Almacenadas en Key Vault

## 🧪 Testing y Validación

### Testing con Postman
- **Colección Producción**: `postman_collection_production.json`
- **Variables de Entorno**: `postman_environment_production.json`
- **Tests Automáticos**: Validación de respuestas
- **Secuencia de Pruebas**: Health → List → Create → Details → SSH → Delete

### Testing Automatizado
- **Health Checks**: `/api/health`
- **Unit Tests**: Funciones individuales
- **Integration Tests**: End-to-end
- **Load Testing**: Postman/Newman

### Monitoreo
- **Application Insights**: Métricas y logs
- **Azure Monitor**: Alertas
- **Custom Dashboards**: KPIs
- **Error Tracking**: Excepciones
- **VM Status Monitor**: Timer trigger cada 5 minutos

## 📚 Documentación

### Guías de Usuario
- **README.md**: Información general
- **README_POSTMAN.md**: Guía rápida de testing
- **GUIA_POSTMAN_PRODUCCION.md**: Guía detallada de Postman
- **MIND_MAP_ARQUITECTURA.md**: Este archivo - arquitectura completa
- **PASOS_CREAR_VM_PRODUCCION.md**: Proceso de creación de VMs
- **RESUMEN_COMPLETADO.md**: Estado actual del proyecto

### Documentación Técnica
- **Architecture Diagrams**: Diagramas de arquitectura
- **Database Schema**: Esquema de CosmosDB
- **API Specifications**: Endpoints documentados
- **Deployment Scripts**: `create-vm-prod.sh`

### Archivos de Testing
- **postman_collection_production.json**: Colección completa
- **postman_environment_production.json**: Variables preconfiguradas
- **Tests Automáticos**: Validación integrada en cada endpoint

---

**🎯 Este mind map proporciona una visión completa de la arquitectura, desde la infraestructura hasta el testing, facilitando el entendimiento y mantenimiento del sistema.**