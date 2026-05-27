# Checklist de Estabilización — Tiny Hearts Landing Page

> Prioridades: 🔴 Alta / 🟡 Media / 🟢 Baja

---

## 🔴 1. Seguridad y configuración

- [ ] **Crear `.gitignore`** — Excluir `__pycache__/`, `tests/screenshots/`, `.DS_Store`, `*.pyc`, `node_modules/` si se agregan en el futuro.
- [ ] **Mover claves de EmailJS a entorno** — Actualmente hardcodeadas en `main.js:273-276`. Aunque EmailJS usa public keys diseñadas para estar en cliente, conviene centralizarlas en un bloque `const CONFIG = {...}` al inicio del archivo para facilitar cambios.
- [ ] **Eliminar placeholders comentados** — Google Analytics (`G-XXXXXXXXXX`) y Google Search Console (`xxxxxxxxx`) tienen placeholders. Decidir si se implementan o se eliminan para no enviar código muerto a producción.
- [ ] **Protección anti-spam en formulario** — EmailJS no tiene rate limiting. Considerar agregar un honeypot field o CAPTCHA (reCAPTCHA v3 invisible o Cloudflare Turnstile).

## 🔴 2. SEO y visibilidad (completar)

- [ ] **Configurar Google Search Console** — Reemplazar placeholder y verificar propiedad.
- [ ] **Configurar Google Analytics 4** — Reemplazar placeholder con ID real.
- [ ] **Verificar og:image** — La URL en las OG tags debe apuntar a una imagen existente y accesible. Actualmente no hay una imagen de preview en el repositorio.
- [ ] **Agregar favicon** — No hay favicon actualmente. Afecta pestañas del navegador y bookmarks.
- [ ] **Crear página 404 personalizada** — GitHub Pages muestra su 404 genérico por defecto.

## 🟡 3. Rendimiento y producción

- [ ] **Minificar CSS y JS para producción** — Usar herramientas simples (cssnano + terser vía CLI, o copy manual) antes de deploy. Una alternativa liviana es minificar manual con `curl` usando servicios como minifier.org, o integrar un script simple.
- [ ] **Verificar lazy loading de imágenes/iframes** — Si hay imágenes o videos, deben tener `loading="lazy"`.
- [ ] **Cache policy** — GitHub Pages ya maneja caché, pero verificar que los assets estáticos tengan cabezales adecuados.
- [ ] **Considerar compresión Brotli** — GitHub Pages lo soporta, pero verificar que los archivos .html, .css, .js se sirvan comprimidos.
- [ ] **Verificar Cumulative Layout Shift (CLS)** — Especialmente Google Fonts. El `font-display: swap` ayuda, pero medir con Lighthouse.

## 🟡 4. Funcionalidad y robustez

- [ ] **Manejo de error en EmailJS** — Verificar que si EmailJS falla (límite de peticiones, timeout), el usuario recibe feedback claro. Revisar el bloque `catch` en `main.js`.
- [ ] **Prevenir reservas duplicadas** — El formulario no valida si el usuario hace doble clic en "Enviar". Deshabilitar botón tras el primer envío.
- [ ] **Validación de fechas en zona horaria** — El servicio es en Costa Rica (UTC-6). El formulario usa `Date` del navegador, que depende de la zona horaria del usuario. Para reservas, conviene forzar UTC-6.
- [ ] **Pruebas en múltiples navegadores** — Playwright solo prueba Chromium. Agregar pruebas en Firefox y WebKit (Playwright lo soporta nativamente).
- [ ] **Verificar comportamiento sin JavaScript** — Si JS falla o está deshabilitado, el formulario no funciona. Agregar un `<noscript>` con mensaje o fallback informativo.

## 🟡 5. Código y deuda técnica

- [ ] **Organizar CSS por secciones** — `style.css` tiene 1667 líneas sin separadores claros. Agregar comentarios de sección (ej. `/* ===== HEADER ===== */`) mejora mantenibilidad.
- [ ] **Revisar CSS no utilizado** — Verificar con cobertura de Lighthouse si hay reglas CSS que no se aplican.
- [ ] **Implementar temas alternativos** — `paletas.svg` define 4 temas, pero solo "Sol y Mar" tiene estilos activos. Si no se van a usar, eliminar la paleta para no confundir. Si se van a usar, implementar las variables CSS faltantes.
- [ ] **Centralizar constantes en JS** — Los strings de EmailJS, selectores de DOM, y config numérica (intervalo del slider, umbral de scroll) están dispersos en `main.js`. Agruparlos en un objeto `CONFIG`.

## 🟢 6. Experiencia de usuario

- [ ] **Agregar política de privacidad** — Si el formulario recolecta datos personales (nombre, teléfono, email), se necesita un enlace a política de privacidad (GDPR/leyes locales).
- [ ] **Agregar términos de servicio** — Opcional pero recomendado para un servicio de cuidado infantil con depósitos de garantía.
- [ ] **Confirmación visual más clara tras envío** — Actualmente hay un mensaje de éxito/error. Considerar un modal de confirmación o redirección suave.
- [ ] **FAQ section** — Preguntas frecuentes ayudarían a reducir consultas directas y mejorar SEO (rich snippets de FAQ).

## 🟢 7. Proyecto y documentación

- [ ] **Documentar despliegue en README.md** — Instrucciones claras de cómo actualizar el sitio (push a main → GitHub Pages).
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
| 🔴 Alta | 11 | Hacer antes del deploy final |
| 🟡 Media | 12 | Hacer en el próximo sprint |
| 🟢 Baja | 9 | Mejora continua / backlog |
