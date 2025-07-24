# 📋 Guía Completa: Testing con Postman en Producción

## 🎯 Objetivo

Esta guía te permitirá probar completamente la API de gestión de VMs en Azure Functions usando Postman, con todos los endpoints configurados y listos para usar en el ambiente de producción.

## 📋 Requisitos Previos

### 🛠️ Software Necesario
- **Postman Desktop** (versión 9.0 o superior)
- Acceso a internet
- Permisos para crear recursos en Azure (para testing completo)

### 📁 Archivos Requeridos
- `postman_collection_production.json` - Colección de endpoints
- `postman_environment_production.json` - Variables de entorno

## ⚡ Configuración Inicial

### 1. Importar Colección y Entorno

#### Paso 1: Abrir Postman
```
1. Iniciar Postman Desktop
2. Asegurarse de estar logueado (opcional pero recomendado)
```

#### Paso 2: Importar Archivos
```
1. Click en "Import" (botón superior izquierdo)
2. Seleccionar "Upload Files"
3. Arrastrar o seleccionar ambos archivos JSON:
   - postman_collection_production.json
   - postman_environment_production.json
4. Click "Import"
```

#### Paso 3: Configurar Entorno
```
1. En el dropdown superior derecho, seleccionar:
   "Azure Functions VM Management - Producción"
2. Verificar que aparezcan las variables configuradas
```

### 2. Verificar Variables de Entorno

#### Variables Principales
| Variable | Valor | Descripción |
|----------|-------|-------------|
| `base_url` | `https://vm-az-functions-demo.azurewebsites.net` | URL base de la API |
| `api_key` | `pGfZb--H1Svjo_1x5cjcbfssPEAuHflwk_DQEaIzvMk` | Clave de autenticación |
| `test_vm_name` | `postman-test-vm` | Nombre base para VMs de prueba |
| `created_vm_name` | (se llena automáticamente) | Nombre de la VM creada |

#### Variables Adicionales
| Variable | Valor | Uso |
|----------|-------|-----|
| `vm_size_small` | `small` | Tamaño pequeño de VM |
| `vm_size_medium` | `medium` | Tamaño mediano de VM |
| `vm_size_large` | `large` | Tamaño grande de VM |
| `default_region` | `eastus` | Región por defecto |

## 🧪 Secuencia de Pruebas Recomendada

### Orden de Ejecución

| # | Endpoint | Tiempo Estimado | Propósito |
|---|----------|-----------------|----------|
| 1️⃣ | 🏥 Health Check | 5 segundos | Verificar sistema |
| 2️⃣ | 📋 List VMs | 10 segundos | Ver estado actual |
| 3️⃣ | 🆕 Create VM | 3-5 minutos | Crear VM de prueba |
| 4️⃣ | 🔍 Get VM Details | 10 segundos | Verificar creación |
| 5️⃣ | 🔑 Get SSH Key | 5 segundos | Obtener acceso SSH |
| 6️⃣ | 🗑️ Delete VM | 2-3 minutos | Limpiar recursos |

## 📝 Detalles de Cada Endpoint

### 1️⃣ Health Check

#### Configuración
- **Método**: `GET`
- **URL**: `{{base_url}}/api/health`
- **Autenticación**: No requerida
- **Headers**: Ninguno adicional

#### Respuesta Esperada
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00Z",
  "services": {
    "cosmosdb": "connected",
    "keyvault": "connected",
    "azure_compute": "available"
  }
}
```

#### Tests Automáticos
- ✅ Status code es 200
- ✅ Response tiene campo 'status'
- ✅ Status es 'healthy'

### 2️⃣ List VMs

#### Configuración
- **Método**: `GET`
- **URL**: `{{base_url}}/api/vms`
- **Autenticación**: x-api-key
- **Headers**: Automático via colección

#### Respuesta Esperada
```json
{
  "vms": [
    {
      "name": "vm-example",
      "status": "running",
      "size": "medium",
      "region": "eastus",
      "public_ip": "20.1.2.3",
      "created_at": "2024-01-01T10:00:00Z"
    }
  ],
  "total_count": 1
}
```

#### Tests Automáticos
- ✅ Status code es 200
- ✅ Response tiene array 'vms'
- ✅ Array es válido

### 3️⃣ Create VM

#### Configuración
- **Método**: `POST`
- **URL**: `{{base_url}}/api/vms`
- **Autenticación**: x-api-key
- **Content-Type**: application/json

#### Body de la Solicitud
```json
{
  "name": "{{test_vm_name}}-{{$randomInt}}",
  "size": "medium",
  "region": "eastus",
  "tags": {
    "Environment": "Testing",
    "CreatedBy": "Postman",
    "Purpose": "API Testing"
  }
}
```

#### Respuesta Esperada
```json
{
  "vm_name": "postman-test-vm-12345",
  "public_ip": "20.1.2.4",
  "ssh_private_key": "-----BEGIN OPENSSH PRIVATE KEY-----\n...",
  "status": "creating",
  "resource_group": "rg-postman-test-vm-12345",
  "estimated_completion": "2024-01-01T12:05:00Z"
}
```

#### Tests Automáticos
- ✅ Status code es 200
- ✅ Response tiene 'vm_name'
- ✅ Response tiene 'public_ip'
- ✅ Response tiene 'ssh_private_key'
- ✅ Guarda vm_name en variable de colección

#### ⚠️ Consideraciones Importantes
- **Tiempo**: La creación toma 3-5 minutos
- **Costo**: Genera costos en Azure
- **Nombre único**: Se usa {{$randomInt}} para evitar conflictos

### 4️⃣ Get VM Details

#### Configuración
- **Método**: `GET`
- **URL**: `{{base_url}}/api/vms/{{created_vm_name}}`
- **Autenticación**: x-api-key
- **Dependencia**: Requiere VM creada en paso anterior

#### Respuesta Esperada
```json
{
  "name": "postman-test-vm-12345",
  "status": "running",
  "size": "medium",
  "region": "eastus",
  "public_ip": "20.1.2.4",
  "private_ip": "10.0.0.4",
  "resource_group": "rg-postman-test-vm-12345",
  "created_at": "2024-01-01T12:00:00Z",
  "tags": {
    "Environment": "Testing",
    "CreatedBy": "Postman",
    "Purpose": "API Testing"
  }
}
```

#### Tests Automáticos
- ✅ Status code es 200
- ✅ Response tiene 'name'
- ✅ Response tiene 'status'

### 5️⃣ Get SSH Key

#### Configuración
- **Método**: `GET`
- **URL**: `{{base_url}}/api/ssh-keys/{{created_vm_name}}`
- **Autenticación**: x-api-key
- **Dependencia**: Requiere VM creada

#### Respuesta Esperada
```json
{
  "vm_name": "postman-test-vm-12345",
  "ssh_private_key": "-----BEGIN OPENSSH PRIVATE KEY-----\n...",
  "ssh_public_key": "ssh-rsa AAAAB3NzaC1yc2E...",
  "username": "azureuser",
  "connection_command": "ssh -i private_key.pem azureuser@20.1.2.4"
}
```

#### Tests Automáticos
- ✅ Status code es 200
- ✅ Response tiene 'ssh_private_key'

#### 💡 Uso de la Clave SSH
```bash
# Guardar la clave privada en un archivo
echo "-----BEGIN OPENSSH PRIVATE KEY-----..." > private_key.pem
chmod 600 private_key.pem

# Conectar a la VM
ssh -i private_key.pem azureuser@[PUBLIC_IP]
```

### 6️⃣ Delete VM

#### Configuración
- **Método**: `DELETE`
- **URL**: `{{base_url}}/api/vms/{{created_vm_name}}`
- **Autenticación**: x-api-key
- **Dependencia**: Requiere VM creada

#### Respuesta Esperada
```json
{
  "message": "VM postman-test-vm-12345 deleted successfully",
  "vm_name": "postman-test-vm-12345",
  "resources_deleted": [
    "Virtual Machine",
    "Network Interface",
    "Public IP",
    "Network Security Group",
    "Virtual Network",
    "Resource Group"
  ],
  "estimated_completion": "2024-01-01T12:08:00Z"
}
```

#### Tests Automáticos
- ✅ Status code es 200
- ✅ Response tiene 'message'
- ✅ Message contiene 'deleted successfully'

#### ⚠️ Consideraciones
- **Tiempo**: La eliminación toma 2-3 minutos
- **Irreversible**: No se puede deshacer
- **Limpieza completa**: Elimina todos los recursos asociados

## 🔧 Scripts de Prueba Avanzados

### Script Pre-request Global
```javascript
// Verificar que las variables estén configuradas
if (!pm.environment.get("base_url")) {
    throw new Error("Variable base_url no configurada");
}

if (!pm.environment.get("api_key")) {
    throw new Error("Variable api_key no configurada");
}

// Log de inicio de request
console.log(`Ejecutando: ${pm.info.requestName}`);
console.log(`URL: ${pm.request.url}`);
```

### Script Test Global
```javascript
// Verificar tiempo de respuesta
pm.test("Response time is less than 30 seconds", function () {
    pm.expect(pm.response.responseTime).to.be.below(30000);
});

// Verificar headers de respuesta
pm.test("Response has correct content-type", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});

// Log de resultado
console.log(`Status: ${pm.response.status}`);
console.log(`Time: ${pm.response.responseTime}ms`);
```

## ⏱️ Consideraciones de Tiempo

### Tiempos Típicos por Operación
| Operación | Tiempo Mínimo | Tiempo Típico | Tiempo Máximo |
|-----------|---------------|---------------|---------------|
| Health Check | 1s | 3s | 10s |
| List VMs | 2s | 5s | 15s |
| Create VM | 180s | 240s | 300s |
| Get VM Details | 2s | 5s | 15s |
| Get SSH Key | 1s | 3s | 10s |
| Delete VM | 120s | 180s | 240s |

### Configuración de Timeouts
```javascript
// En Postman Settings → General
// Request timeout: 300000ms (5 minutos)
// Response timeout: 300000ms (5 minutos)
```

## 🚨 Manejo de Errores

### Errores Comunes y Soluciones

#### Error 401 - Unauthorized
```json
{
  "error": "Unauthorized",
  "message": "Invalid or missing API key"
}
```
**Solución**:
1. Verificar que el entorno esté seleccionado
2. Confirmar que la variable `api_key` tenga valor
3. Revisar que el header `x-api-key` esté presente

#### Error 409 - Conflict
```json
{
  "error": "VM name already exists",
  "message": "A VM with this name already exists"
}
```
**Solución**:
1. Cambiar el nombre de la VM en el body
2. Usar `{{$randomInt}}` para generar nombres únicos
3. Verificar VMs existentes con List VMs

#### Error 500 - Internal Server Error
```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```
**Solución**:
1. Ejecutar Health Check primero
2. Revisar logs en Azure Portal
3. Verificar que los servicios de Azure estén disponibles
4. Intentar nuevamente después de unos minutos

#### Timeout Errors
```
Error: timeout of 30000ms exceeded
```
**Solución**:
1. Aumentar timeout en Postman Settings
2. Verificar conectividad a internet
3. Las operaciones de VM pueden tomar varios minutos

## 📊 Monitoreo y Logs

### Logs en Postman Console
```javascript
// Ver logs detallados
console.log("Request Headers:", pm.request.headers);
console.log("Response Body:", pm.response.text());
console.log("Response Headers:", pm.response.headers);
```

### Logs en Azure Portal
1. Ir a Azure Portal
2. Buscar "vm-az-functions-demo"
3. Ir a "Monitor" → "Logs"
4. Usar queries KQL para debugging

### Application Insights
```kusto
traces
| where timestamp > ago(1h)
| where message contains "postman"
| order by timestamp desc
```

## 🔄 Automatización con Newman

### Instalación
```bash
npm install -g newman
```

### Ejecución
```bash
# Ejecutar colección completa
newman run postman_collection_production.json \
  -e postman_environment_production.json \
  --reporters cli,json \
  --reporter-json-export results.json

# Ejecutar solo Health Check
newman run postman_collection_production.json \
  -e postman_environment_production.json \
  --folder "Health Check"
```

## 📋 Checklist de Testing

### Antes de Empezar
- [ ] Postman instalado y actualizado
- [ ] Archivos JSON importados correctamente
- [ ] Entorno de producción seleccionado
- [ ] Variables de entorno verificadas
- [ ] Conexión a internet estable

### Durante las Pruebas
- [ ] Health Check exitoso
- [ ] List VMs funciona correctamente
- [ ] Create VM completa sin errores
- [ ] VM Details muestra información correcta
- [ ] SSH Key se obtiene correctamente
- [ ] Delete VM limpia todos los recursos

### Después de las Pruebas
- [ ] Todas las VMs de prueba eliminadas
- [ ] No hay recursos huérfanos en Azure
- [ ] Logs revisados para errores
- [ ] Resultados documentados

## 🆘 Troubleshooting Avanzado

### Verificar Conectividad
```bash
# Ping a la Function App
ping vm-az-functions-demo.azurewebsites.net

# Test HTTP básico
curl -I https://vm-az-functions-demo.azurewebsites.net/api/health
```

### Debug de Variables
```javascript
// En Pre-request Script
console.log("Environment:", pm.environment.name);
console.log("Base URL:", pm.environment.get("base_url"));
console.log("API Key:", pm.environment.get("api_key") ? "[SET]" : "[NOT SET]");
```

### Validar JSON
```javascript
// En Tests
try {
    const jsonData = pm.response.json();
    console.log("Valid JSON received");
} catch (e) {
    console.log("Invalid JSON:", pm.response.text());
    pm.test("Response is valid JSON", () => {
        pm.expect.fail("Response is not valid JSON");
    });
}
```

## 📞 Soporte y Recursos

### Documentación Adicional
- **README.md** - Información general del proyecto
- **MIND_MAP_ARQUITECTURA.md** - Arquitectura completa
- **README_POSTMAN.md** - Guía rápida

### Contacto
- Revisar logs en Azure Portal
- Consultar documentación de Azure Functions
- Verificar estado de servicios Azure

---

**🎯 Con esta guía completa, deberías poder probar exitosamente todos los endpoints de la API de gestión de VMs. ¡Happy Testing! 🚀**