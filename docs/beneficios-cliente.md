# Beneficios del Desarrollo — Tiny Hearts Landing Page

## 1. Sin dependencias técnicas (Cero vendor lock-in)
HTML, CSS y JavaScript puro. No usa React, Vue, Angular ni ningún framework. Cualquier desarrollador web puede mantenerlo sin necesidad de aprender herramientas específicas. No hay `npm`, `node_modules` ni build steps.

## 2. Infraestructura de costo cero
Hosteado en **GitHub Pages** (gratuito). Sin servidores, sin bases de datos, sin costos recurrentes de hosting. El dominio personalizado es el único costo opcional.

## 3. Rendimiento extremo
- Sin librerías pesadas ni bundlers.
- Google Fonts con `preconnect` y `font-display: swap`.
- JavaScript con `defer` (no bloquea renderizado).
- Animaciones con aceleración GPU (CSS transforms).
- `IntersectionObserver` para revelación eficiente al hacer scroll.
- Carga instantánea incluso en conexiones lentas.

## 4. SEO integral (diseñado para Google)
- **JSON-LD Structured Data**: 7 bloques (LocalBusiness, Services, Products) para rich snippets en Google.
- **Open Graph + Twitter Cards**: Compartir en redes sociales con vista previa enriquecida.
- **Sitemap XML + robots.txt**: Crawleable y descubrible.
- **Semántica HTML5**: Jerarquía H1→H2→H3 correcta, `article`, `section`, `nav`.
- **Canonical URL**: Evita contenido duplicado.
- **Meta tags descriptivos**: Title y description optimizados con keywords locales.

## 5. Accesibilidad (WCAG)
- ARIA attributes completos (`aria-label`, `aria-expanded`, `aria-controls`, `aria-selected`, `role="alert"`).
- Navegación por teclado (flechas en slider, focus visible).
- Contraste de color adecuado (`--text-dark: #232c28`).
- Formulario con `<label>` y validación con mensajes de error role="alert".
- Etiquetas `aria-hidden` en elementos decorativos.

## 6. Mobile-first responsive
Diseñado desde cero para móviles, tablets y desktop con `clamp()` para tipografía y espaciado fluidos. Menú hamburguesa con overlay animado para dispositivos táctiles.

## 7. Single Page Application (navegación fluida)
Toda la información en una sola página con anclas suaves (`scroll-behavior: smooth`). Sin recargas, sin esperas.

## 8. Formulario funcional sin backend
Integración con **EmailJS** que envía:
- Notificación al negocio cuando alguien reserva.
- Confirmación automática al cliente.

Sin necesidad de servidor, API propia ni base de datos.

## 9. Fácil mantenimiento
- 1 archivo HTML → todo el contenido.
- 1 archivo CSS → todos los estilos.
- 1 archivo JS → toda la interactividad.

Cualquier cambio se hace editando un archivo y haciendo push.

## 10. Testing automatizado
Suite de pruebas con **Playwright** (23 categorías) que verifica:
- Estructura global, secciones, menú móvil, formulario, slider, scroll, responsive.
- Errores de consola, overflow horizontal, integridad de anclas.
- Capturas de pantalla automáticas en desktop, tablet y móvil.

## 11. Propiedad total del código
Código abierto, sin licencias, sin vendor lock-in. El cliente es dueño absoluto de su sitio.

## 12. Escalable por diseño
Arquitectura limpia que permite agregar secciones (blog, FAQ, galería) sin reestructurar. Sistema de temas con paletas de colores intercambiables vía `data-theme` (4 temas pre-diseñados: Sol y Mar, Brisa Costera, Dulce Infantil, Paraíso Natural).


Viewed beneficios-cliente.md:1-63

Aquí tienes la versión simplificada para tu cliente:

---

## Lo que incluye tu sitio web — en palabras sencillas

**2. Sin costos de servidor**
El sitio vive en internet de forma gratuita. No pagas mensualidades de hosting. El único costo adicional es el dominio.

**3. Carga muy rápido**
El sitio está optimizado para abrir al instante, incluso si el visitante tiene internet lento.
**4. Diseñado para que Google te encuentre**
Se configuraron todas las herramientas que Google necesita para posicionar tu negocio en los primeros resultados de búsqueda. También se ve bien cuando alguien comparte tu página en redes sociales.

**5. Accesible para todos**
Funciona para personas con discapacidades visuales o que navegan solo con el teclado. Cumple con los estándares internacionales de accesibilidad.

**6. Se ve bien en cualquier dispositivo**
Celular, tableta o computadora — la pagina se adapta automáticamente para verse perfecto en cualquier pantalla.

**7. Todo en una sola página, sin interrupciones**
No hay páginas que cargar de nuevo. Una Sola carga con la informacion necesaria.

**8. Recibe correos de reservas automáticamente**
Cuando alguien llena el formulario, tú recibes un aviso y el cliente recibe una confirmación — todo automático, sin que tengas que hacer nada.

**10. Probado antes de entregarte**
El sitio pasó por pruebas automáticas que verifican que todo funciona correctamente en celular, tableta y computadora.

**12. Puede crecer contigo**
Si en el futuro quieres agregar una sección (como un blog, galería de fotos o preguntas frecuentes), se puede hacer sin reconstruir todo.