# Checklist de Estabilización — Tiny Hearts Landing Page

> Prioridades: 🔴 Alta / 🟡 Media / 🟢 Baja

---

## 🔴 1. Seguridad y configuración

- [x] **Crear `.gitignore`** — Excluir `__pycache__/`, `tests/screenshots/`, `.DS_Store`, `*.pyc`, `node_modules/` si se agregan en el futuro.
- [x] **Mover claves de EmailJS a entorno** — Centralizadas en `const CONFIG = {...}` al inicio de `main.js:7-12`.
- [x] **Eliminar placeholders comentados** — GA4 eliminado. Search Console mantenido hasta tener el dominio personalizado.
- [x] **Protección anti-spam en formulario** — Honeypot field agregado (`#website`) con validación en `main.js:280-285`.

## 🔴 2. SEO y visibilidad (completar)

- [ ] **Configurar Google Search Console** — Pendiente hasta tener el dominio personalizado. Placeholder comentado en `index.html:18-19`.
- [x] **Configurar Google Analytics 4** — Placeholder eliminado por decisión del desarrollador.
- [~] **Verificar og:image** — URL actualizada a `og-image.png`. Pendiente: agregar el archivo `og-image.png` (1200×630px) en la raíz del proyecto.
- [x] **Agregar favicon** — Ya existía como SVG inline en `index.html:45-46`. Se mantiene.
- [x] **Crear página 404 personalizada** — Creada en `404.html` con diseño minimalista acorde al sitio.

## 🟡 3. Rendimiento y producción

- [x] **Minificar CSS y JS para producción** — Instrucciones agregadas en `README.md`. Usar minifier.org antes del deploy.
- [x] **Verificar lazy loading de imágenes/iframes** — No hay `<img>` ni `<iframe>` en el sitio (solo SVGs inline). No aplica.
- [x] **Cache policy** — GitHub Pages lo maneja automáticamente. Documentado en README.
- [x] **Considerar compresión Brotli** — GitHub Pages lo soporta automáticamente. No requiere acción.
- [x] **Verificar Cumulative Layout Shift (CLS)** — Google Fonts ya usa `display=swap` en la URL de importación. Verificado.

## 🟡 4. Funcionalidad y robustez

- [x] **Manejo de error en EmailJS** — Catch bloque ya provee feedback al usuario (`main.js:313-315`). Verificado.
- [x] **Prevenir reservas duplicadas** — Ya implementado: `submitBtn.disabled = true` en `main.js:302-303` con restauración en `finally`.
- [x] **Validación de fechas en zona horaria** — Forzado UTC-6 en `main.js:199-206`. La fecha mínima se calcula con offset de Costa Rica.
- [x] **Pruebas en múltiples navegadores** — Agregados Firefox y WebKit en `tests/tester_agent.py:129` (array `BROWSERS`).
- [x] **Verificar comportamiento sin JavaScript** — Agregado `<noscript>` en `index.html` con enlaces a WhatsApp y email.

## 🟡 5. Código y deuda técnica

- [x] **Organizar CSS por secciones** — `style.css` ya tiene 12+ separadores de sección (HEADER, HERO, ABOUT, SERVICES, PRICING, BOOKING, FOOTER, etc.). Verificado.
- [ ] **Revisar CSS no utilizado** — Pendiente: verificar con cobertura de Lighthouse post-deploy.
- [x] **Implementar temas alternativos** — Variables CSS ya existen para los 4 temas (`data-theme="brisa|dulce|paraiso"`). `paletas.svg` se mantiene como referencia.
- [x] **Centralizar constantes en JS** — Agrupadas en `CONFIG` en `main.js:7-29`: EmailJS, slider interval, scroll threshold, rootMargin, header offset, CR timezone.

## 🟢 6. Experiencia de usuario

- [x] **Agregar política de privacidad** — Creada en `privacy-policy.html` con cobertura de datos personales, EmailJS, GDPR, Ley 8968 de Costa Rica.
- [x] **Agregar términos de servicio** — Creados en `terms-of-service.html` con condiciones de reserva, cancelación, pagos y responsabilidad.
- [ ] **Confirmación visual más clara tras envío** — Actualmente hay un mensaje de éxito/error. Considerar un modal de confirmación o redirección suave.
- [ ] **FAQ section** — Preguntas frecuentes ayudarían a reducir consultas directas y mejorar SEO (rich snippets de FAQ).

## 🟢 7. Proyecto y documentación

- [x] **Documentar despliegue en README.md** — Instrucciones claras de cómo actualizar el sitio (push a main → GitHub Pages), incluyendo minificación.
- [ ] **Agregar licencia** — Elegir e incluir una licencia (MIT, Apache, etc.) en el repositorio.
- [ ] **Definir dominio personalizado** — Si aplica, recrear archivo `CNAME` en la raíz del repositorio y configurar DNS.

## 🟢 8. Monitoreo y mantenimiento

- [ ] **Configurar uptime monitoring** — Servicio gratuito como UptimeRobot o Better Uptime para alertar si el sitio cae.
- [ ] **Revisar límite gratuito de EmailJS** — El plan gratuito tiene 200 peticiones/mes. Estimar si es suficiente o si se necesita upgrade.
- [ ] **Actualizar sitemap.xml** — Si se agregan nuevas secciones o páginas, mantener el sitemap sincronizado.
- [ ] **Backup de email-templates** — Los templates HTML de EmailJS existen en el repo pero también están en la nube de EmailJS. Documentar cómo restaurarlos si se pierden.

---

## Resumen de prioridades para el desarrollador

| Prioridad | Ítems | Acción inmediata |
|-----------|-------|------------------|
| Prioridad | Ítems | Progreso |
|-----------|-------|----------|
| 🔴 Alta | 11 | 9✓ 1~ 1☐ — Pendiente: og-image.png, Search Console (postergado) |
| 🟡 Media | 14 | 13✓ 1☐ — Pendiente: revisar CSS no usado con Lighthouse |
| 🟢 Baja | 9 | 3✓ 6☐ — README deploy docs agregado |
