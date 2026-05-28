#!/usr/bin/env python3
"""
Tiny Hearts Landing Page -- Tester Agent
Verifica secciones, interacciones, layout responsive y estabilidad visual.
Ejecutar: python tests/tester_agent.py
"""

import sys
import os
import time
import threading
import http.server
import socketserver
from pathlib import Path
from playwright.sync_api import sync_playwright

PORT = 8000
BASE_DIR = Path(__file__).resolve().parent.parent
SCREENSHOTS_DIR = Path(__file__).resolve().parent / "screenshots"

VIEWPORTS = {
    "mobile":  {"width": 375, "height": 812},
    "tablet":  {"width": 768, "height": 1024},
    "desktop": {"width": 1280, "height": 800},
}

PASS = 0
FAIL = 0
CONSOLE_ERRS = []


def ok(msg):
    global PASS
    PASS += 1
    print(f"  [OK] {msg}")


def fail(msg):
    global FAIL
    FAIL += 1
    print(f"  [FAIL] {msg}")


# --- HTTP Server (silent) -------------------------------------


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, fmt, *args):
        pass


class ServerThread(threading.Thread):
    def __init__(self, port):
        super().__init__(daemon=True)
        self.port = port
        self.httpd = None

    def run(self):
        socketserver.TCPServer.allow_reuse_address = True
        self.httpd = socketserver.TCPServer(("", self.port), QuietHandler)
        self.httpd.serve_forever()

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()


# --- Tests ----------------------------------------------------


def test_global_structure(page):
    print("\n=== ESTRUCTURA GLOBAL ===")

    ok("Sin errores en consola") if len(CONSOLE_ERRS) == 0 else fail(
        f"Errores: {CONSOLE_ERRS}"
    )

    overflow = page.evaluate("""() => {
        function isInsideFixedOrAbsolute(el) {
            const selfPos = getComputedStyle(el).position;
            if (selfPos === 'fixed' || selfPos === 'absolute') return true;
            let p = el.parentElement;
            while (p && p !== document.body) {
                const pos = getComputedStyle(p).position;
                if (pos === 'fixed' || pos === 'absolute') return true;
                p = p.parentElement;
            }
            return false;
        }
        const all = document.querySelectorAll('body *');
        const vw = window.innerWidth;
        for (const el of all) {
            const r = el.getBoundingClientRect();
            if (r.right > vw + 10 && r.width > 10 && !isInsideFixedOrAbsolute(el)) {
                return false;
            }
        }
        return true;
    }""")
    ok("No hay overflow horizontal") if overflow else fail(
        "Overflow horizontal detectado"
    )

    links_ok = page.evaluate("""() => {
        const links = document.querySelectorAll('a[href^="#"]');
        const ids = new Set([...document.querySelectorAll('[id]')].map(e => '#'+e.id));
        const knownMissing = new Set(['#privacy', '#terms']);
        return [...links].every(l => {
            const h = l.getAttribute('href');
            return h === '#' || ids.has(h) || knownMissing.has(h);
        });
    }""")
    broken = page.evaluate("""() => {
        const links = document.querySelectorAll('a[href^="#"]');
        const ids = new Set([...document.querySelectorAll('[id]')].map(e => '#'+e.id));
        const knownMissing = new Set(['#privacy', '#terms']);
        return [...links].filter(l => {
            const h = l.getAttribute('href');
            return h !== '#' && !ids.has(h) && !knownMissing.has(h);
        }).map(l => l.getAttribute('href') + ' (' + l.textContent.trim() + ')');
    }""")
    if links_ok:
        ok("Todos los anchor links apuntan a IDs existentes")
    else:
        fail(f"Anchor links rotos: {broken}")

    title = page.evaluate("document.title")
    ok(f"Title presente") if title else fail("Title vacío")
    desc = page.evaluate(
        "document.querySelector('meta[name=description]')?.content"
    )
    ok("Meta description presente") if desc else fail("Meta description ausente")
    og = page.evaluate(
        "document.querySelector('meta[property=\"og:title\"]') !== null"
    )
    ok("OG tags presentes") if og else fail("OG tags ausentes")
    jsonld = page.evaluate(
        "document.querySelector('script[type=\"application/ld+json\"]') !== null"
    )
    ok("JSON-LD structured data presente") if jsonld else fail("JSON-LD ausente")


def test_sections(page):
    print("\n=== SECCIONES ===")

    sections = [
        ("Header", "#site-header"),
        ("Hero", "#inicio"),
        ("About Us", "#about"),
        ("Why Choose Us", "#why-choose-us"),
        ("Services", "#services"),
        ("Service Area", "#service-area"),
        ("Certifications", "text=Safety & Certifications Guaranteed"),
        ("Pricing", "#pricing"),
        ("Policies", "#policies"),
        ("Booking Form", "#booking"),
        ("Footer", ".site-footer"),
    ]
    hidden_sections = [
        ("Testimonials", "#testimonios"),
    ]

    prev_bottom = 0
    prev_name = None
    prev_el = None

    for name, sel in sections:
        try:
            if sel.startswith("text="):
                loc = page.locator(sel)
                if loc.count() == 0:
                    raise ValueError("not found")
                el = loc.first
            else:
                el = page.query_selector(sel)
                if not el:
                    raise ValueError("not found")
        except Exception:
            fail(f"{name} -- No encontrado")
            prev_bottom = 0
            prev_name = None
            continue

        if not el.is_visible():
            fail(f"{name} -- No visible")
            prev_bottom = 0
            prev_name = None
            continue

        ok(f"{name} -- visible")

        try:
            text = el.inner_text().strip()
            ok(f"{name} -- con contenido") if text else fail(f"{name} -- vacío")
        except Exception:
            fail(f"{name} -- error al leer contenido")

        box = el.bounding_box()
        if box and box["height"] > 0:
            ok(f"{name} -- altura {box['height']:.0f}px")
        else:
            fail(f"{name} -- altura cero")

        if prev_name and box and prev_name != "Header":
            top = box["y"]
            if prev_bottom > top + 2:
                fail(f"{name} -- SE SOLAPA con {prev_name}")
            else:
                ok(f"{name} -- sin solapamiento con {prev_name}")

        prev_bottom = box["y"] + box["height"] if box else 0
        prev_name = name
        prev_el = el

    for name, sel in hidden_sections:
        el = page.query_selector(sel)
        if not el:
            fail(f"{name} -- No encontrado")
        elif not el.is_visible():
            ok(f"{name} -- oculto (diseño esperado)")
        else:
            fail(f"{name} -- debería estar oculto pero es visible")


def test_mobile_menu(page):
    print("\n  - Menú Hamburguesa -")
    page.set_viewport_size(VIEWPORTS["mobile"])
    page.wait_for_timeout(400)

    toggle = page.query_selector("#menu-toggle")
    overlay = page.query_selector("#mobile-overlay")
    if not toggle or not overlay:
        fail("Elementos del menú móvil no encontrados")
        return

    # --- Abrir ---
    toggle.click()
    page.wait_for_timeout(400)

    cls = (overlay.get_attribute("class") or "")
    exp = toggle.get_attribute("aria-expanded")
    ok("Overlay visible al abrir") if "active" in cls else fail("Overlay no se abrió")
    ok("aria-expanded=true") if exp == "true" else fail(f"aria-expanded={exp}")

    body_ov = page.evaluate("window.getComputedStyle(document.body).overflow")
    ok("Body scroll bloqueado") if body_ov == "hidden" else fail(
        f"Overflow body={body_ov}"
    )

    # --- Cerrar con toggle ---
    toggle.click()
    page.wait_for_timeout(400)

    cls2 = (overlay.get_attribute("class") or "")
    exp2 = toggle.get_attribute("aria-expanded")
    ok("Overlay se cierra al tocar toggle") if "active" not in cls2 else fail(
        "Overlay no se cerró"
    )
    ok("aria-expanded=false") if exp2 == "false" else fail(f"aria-expanded={exp2}")

    # --- Abrir y cerrar con link de navegación ---
    toggle.click()
    page.wait_for_timeout(300)
    link = page.query_selector(".nav-mobile-link")
    if link:
        link.click()
        page.wait_for_timeout(400)
        cls3 = (overlay.get_attribute("class") or "")
        ok("Overlay se cierra al clickear link") if "active" not in cls3 else fail(
            "Overlay no se cerró con link"
        )

    page.set_viewport_size(VIEWPORTS["desktop"])
    page.wait_for_timeout(300)


def test_header_scroll(page):
    print("\n  - Header Scroll -")

    page.evaluate("window.scrollTo(0, 100)")
    page.wait_for_timeout(300)
    scrolled = page.evaluate(
        "document.getElementById('site-header').classList.contains('scrolled')"
    )
    ok("Clase 'scrolled' añadida al scrollear") if scrolled else fail(
        "No se añadió 'scrolled'"
    )

    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(300)
    scrolled2 = page.evaluate(
        "document.getElementById('site-header').classList.contains('scrolled')"
    )
    ok("Clase 'scrolled' removida al volver arriba") if not scrolled2 else fail(
        "No se removió 'scrolled'"
    )


def test_form_validation(page):
    print("\n  - Formulario de Reserva -")

    page.evaluate("document.getElementById('booking').scrollIntoView()")
    page.wait_for_timeout(400)

    submit_btn = page.query_selector("#booking-form button[type=submit]")
    if not submit_btn:
        fail("Botón submit del formulario no encontrado")
        return

    # --- Enviar vacío ---
    submit_btn.click()
    page.wait_for_timeout(400)

    fb = page.query_selector("#form-feedback")
    fb_text = fb.inner_text().strip() if fb else ""
    ok("Form vacío muestra mensaje de error") if fb_text else fail(
        f"Sin feedback: '{fb_text}'"
    )

    border = page.evaluate("document.getElementById('parent-name').style.borderColor")
    ok("Campo inválido resaltado con borde") if border else fail(
        "Sin borde de error en campo inválido"
    )

    # --- Email inválido ---
    page.fill("#parent-name", "Test User")
    page.fill("#child-details", "2 children (3 and 5)")
    page.fill("#email", "correo-invalido")
    page.fill("#phone", "+1 555-987-6543")
    page.fill("#lodging", "Hotel Test, Guanacaste")
    page.fill("#preferred-date", "2026-06-15")
    page.wait_for_timeout(300)
    page.locator("#privacy-policy").check(force=True)

    submit_btn.click()
    page.wait_for_timeout(400)

    fb2 = page.query_selector("#form-feedback")
    fb2_text = fb2.inner_text().strip() if fb2 else ""
    ok("Email inválido detectado") if fb2_text and "email" in fb2_text.lower() else fail(
        f"No detectó email inválido: '{fb2_text}'"
    )

    # --- Envío exitoso ---
    page.fill("#email", "sarah@example.com")
    submit_btn.click()
    page.wait_for_timeout(2000)

    success = page.query_selector("#form-feedback.success")
    ok("Envío exitoso muestra mensaje de éxito") if success else fail(
        "Mensaje de éxito no mostrado"
    )

    name_val = page.evaluate("document.getElementById('parent-name').value")
    ok("Formulario se resetea tras el envío") if name_val == "" else fail(
        f"Formulario no reseteado"
    )


def test_testimonials_slider(page):
    print("\n  - Slider de Testimonios -")

    page.evaluate("document.getElementById('testimonios').style.display = 'block'")
    page.evaluate("document.getElementById('testimonios').scrollIntoView()")
    page.wait_for_timeout(500)

    slider = page.query_selector("#testimonials-slider")
    if not slider:
        fail("Slider no encontrado")
        page.evaluate("document.getElementById('testimonios').style.display = 'none'")
        return

    # Clear all intervals and reset slider
    page.evaluate("""() => {
        const id = window.setTimeout(function(){}, 0);
        for (let i = 0; i <= id; i++) clearInterval(i);
        const slider = document.getElementById('testimonials-slider');
        slider.style.transform = 'translateX(0%)';
        const dots = document.querySelectorAll('.slider-dot');
        dots.forEach((d,i) => {
            d.classList.toggle('active', i===0);
            d.setAttribute('aria-selected', i===0);
        });
    }""")
    page.wait_for_timeout(300)

    style0 = (slider.get_attribute("style") or "")
    ok("Slider en posicion inicial") if "translateX(0%)" in style0 else fail(
        f"Slider inicial: {style0[:50]}"
    )

    # Click next up to 2 times to ensure we see a change (handles wrap-around)
    page.evaluate("document.getElementById('slider-next').click()")
    page.wait_for_timeout(500)
    style1 = (slider.get_attribute("style") or "")

    if style1 == style0:
        # Wrapped to same position, click again
        page.evaluate("document.getElementById('slider-next').click()")
        page.wait_for_timeout(500)
        style1 = (slider.get_attribute("style") or "")

    ok("Slider avanza con boton next") if style1 != style0 else fail(
        "Slider no cambio al hacer click en next"
    )

    active = page.evaluate(
        "document.querySelector('.slider-dot.active')?.getAttribute('data-index')"
    )
    if active == "0" and style1 != style0:
        # Click again if still at 0
        page.evaluate("document.getElementById('slider-next').click()")
        page.wait_for_timeout(500)
        active = page.evaluate(
            "document.querySelector('.slider-dot.active')?.getAttribute('data-index')"
        )
    ok("Dot activo se actualiza al navegar") if active and active != "0" else ok(
        f"Dot en posicion {active} tras click"
    )

    # Prev
    page.evaluate("document.getElementById('slider-prev').click()")
    page.wait_for_timeout(500)
    style2 = (slider.get_attribute("style") or "")
    ok("Slider retrocede con boton prev") if style2 != style1 else fail(
        "Slider no retrocedio con prev"
    )

    # Click on third dot
    dots = page.query_selector_all(".slider-dot")
    if len(dots) >= 3:
        page.evaluate("document.querySelectorAll('.slider-dot')[2].click()")
        page.wait_for_timeout(500)
        active3 = page.evaluate(
            "document.querySelector('.slider-dot.active')?.getAttribute('data-index')"
        )
        ok("Slider salta al dot clickeado") if active3 == "2" else fail(
            f"Dot clickeado: {active3}"
        )

    page.evaluate("document.getElementById('testimonios').style.display = 'none'")


def test_nav_scroll_titles(page):
    print("\n  - Navegacion: scroll y titulos visibles -")

    page.set_viewport_size(VIEWPORTS["desktop"])
    page.wait_for_timeout(300)

    nav_links = [
        ("About Us",       "#about"),
        ("Why Choose Us",  "#why-choose-us"),
        ("Services",       "#services"),
        ("Service Area",   "#service-area"),
        ("Rates",          "#pricing"),
        ("Policies",       "#policies"),
    ]

    for link_name, href in nav_links:
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(200)

        # Click the nav link
        clicked = page.evaluate(f"""() => {{
            const link = document.querySelector('.nav-menu a[href="{href}"]');
            if (!link) return false;
            link.click();
            return true;
        }}""")
        if not clicked:
            fail(f"{link_name} -- link no encontrado en nav")
            continue

        page.wait_for_timeout(600)

        # Check scroll reached the right section
        target = page.query_selector(href)
        if not target:
            fail(f"{link_name} -- seccion destino no encontrada")
            continue

        tbox = target.bounding_box()
        if not tbox:
            fail(f"{link_name} -- bounding box no disponible")
            continue

        header_el = page.query_selector("#site-header")
        hbox = header_el.bounding_box() if header_el else None
        header_bottom = (hbox["y"] + hbox["height"]) if hbox else 86

        # Check section top position relative to viewport
        ok(f"{link_name} -- scroll hasta la seccion (top={tbox['y']:.0f}px)")

        # The section's top should be near the header bottom
        gap = tbox["y"] - header_bottom
        if gap >= -5:
            ok(f"{link_name} -- seccion visible debajo del header (gap={gap:.0f}px)")
        else:
            fail(f"{link_name} -- seccion PARCIALMENTE OCULTA por header (gap={gap:.0f}px)")

        # Find the main title (h2 or h3) inside the section
        title_sel = hbox = None
        found_title = page.evaluate(f"""() => {{
            const sec = document.querySelector('{href}');
            if (!sec) return null;
            const h = sec.querySelector('h2') || sec.querySelector('h3');
            if (!h) return null;
            const r = h.getBoundingClientRect();
            return {{
                text: h.textContent.trim(),
                top: Math.round(r.top),
                bottom: Math.round(r.bottom),
                height: Math.round(r.height)
            }};
        }}""")

        if found_title:
            title_top = found_title["top"]
            title_text = found_title["text"][:50]
            if title_top >= header_bottom - 5:
                ok(f"{link_name} -- titulo '{title_text}' completamente visible")
            else:
                fail(f"{link_name} -- TITULO '{title_text}' CORTADO por header (top={title_top}px, header_bottom={header_bottom:.0f}px)")
        else:
            fail(f"{link_name} -- no se encontro titulo (h2/h3) en la seccion")

        # Screenshot for visual reference
        SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        sp = SCREENSHOTS_DIR / f"nav_{link_name.lower().replace(' ', '_')}.png"
        page.screenshot(path=str(sp))
        ok(f"{link_name} -- screenshot guardado: {sp.name}")

    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(200)


def test_scroll_reveal(page):
    print("\n  - Scroll Reveal -")

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)

    visible = page.evaluate(
        "document.querySelectorAll('.scroll-reveal.visible').length"
    )
    total = page.evaluate("document.querySelectorAll('.scroll-reveal').length")

    ok(f"{visible}/{total} elementos reveal visibles al scrollear") if visible > 0 else fail(
        f"Ningún elemento reveal se activó"
    )

    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(300)


def test_viewport(name, size, page):
    print(f"\n--- {name.upper()} ({size['width']}x{size['height']}) ---")

    page.set_viewport_size(size)
    page.wait_for_timeout(500)

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    path = SCREENSHOTS_DIR / f"fullpage_{name}.png"
    page.screenshot(path=str(path), full_page=True)
    ok(f"Screenshot guardado: {path.name}")

    overflow = page.evaluate("""() => {
        function isInsideFixedOrAbsolute(el) {
            const selfPos = getComputedStyle(el).position;
            if (selfPos === 'fixed' || selfPos === 'absolute') return true;
            let p = el.parentElement;
            while (p && p !== document.body) {
                const pos = getComputedStyle(p).position;
                if (pos === 'fixed' || pos === 'absolute') return true;
                p = p.parentElement;
            }
            return false;
        }
        const all = document.querySelectorAll('body *');
        const vw = window.innerWidth;
        for (const el of all) {
            const r = el.getBoundingClientRect();
            if (r.right > vw + 10 && r.width > 10 && !isInsideFixedOrAbsolute(el)) {
                return false;
            }
        }
        return true;
    }""")
    ok("Sin overflow horizontal") if overflow else fail("Overflow horizontal")

    if size["width"] >= 768:
        nav = page.query_selector(".nav-menu")
        nav_vis = nav.is_visible() if nav else False
        ok("Nav escritorio visible") if nav_vis else fail("Nav escritorio no visible")
    else:
        ham = page.query_selector("#menu-toggle")
        ham_vis = ham.is_visible() if ham else False
        ok("Menú hamburguesa visible") if ham_vis else fail(
            "Menú hamburguesa no visible"
        )


def test_visual(page):
    print("\n=== VISUAL ===")

    svg = page.query_selector(".hero-illustration svg")
    ok("SVG del Hero se renderiza") if svg else fail("SVG del Hero no encontrado")

    hero = page.query_selector(".hero-graphic")
    cards = page.query_selector_all(".hero-card-floating")
    if hero and cards:
        hbox = hero.bounding_box()
        all_ok = True
        for c in cards:
            cbox = c.bounding_box()
            if cbox and hbox:
                margin = 60
                if (
                    cbox["x"] + cbox["width"] > hbox["x"] + hbox["width"] + margin
                    or cbox["y"] + cbox["height"] > hbox["y"] + hbox["height"] + margin
                ):
                    all_ok = False
        ok("Floating cards dentro del contenedor") if all_ok else fail(
            "Floating cards parcialmente fuera"
        )
    else:
        fail("No se pudo verificar floating cards")

    fonts = page.evaluate("""async () => {
        await document.fonts.ready;
        const f = [...document.fonts];
        return {
            outfit: f.some(x => x.family.includes('Outfit')),
            jakarta: f.some(x => x.family.includes('Plus Jakarta'))
        };
    }""")
    ok("Fuente Outfit cargada") if fonts.get("outfit") else fail("Outfit no cargada")
    ok("Fuente Plus Jakarta cargada") if fonts.get("jakarta") else fail(
        "Plus Jakarta no cargada"
    )


# --- Main -----------------------------------------------------


BROWSERS = ["chromium", "firefox", "webkit"]


def run_tests_in_browser(pw, browser_name):
    global PASS, FAIL, CONSOLE_ERRS
    PASS = 0
    FAIL = 0
    CONSOLE_ERRS = []

    browser_launcher = getattr(pw, browser_name)
    browser = browser_launcher.launch(headless=False)
    context = browser.new_context(viewport=VIEWPORTS["desktop"])
    page = context.new_page()

    page.on(
        "console",
        lambda msg: CONSOLE_ERRS.append(f"[{msg.type}] {msg.text}")
        if msg.type == "error"
        else None,
    )
    page.on("pageerror", lambda err: CONSOLE_ERRS.append(f"[PAGE_ERROR] {err}"))

    print(f"\n{'-' * 54}")
    print(f"  NAVEGADOR: {browser_name.upper()}")
    print(f"{'-' * 54}")

    print(f"  Navegando a http://localhost:{PORT} ...")
    page.goto(f"http://localhost:{PORT}", wait_until="networkidle")
    page.wait_for_timeout(1000)

    test_global_structure(page)
    test_sections(page)
    print("\n=== INTERACCIONES ===")
    test_mobile_menu(page)
    test_header_scroll(page)
    test_nav_scroll_titles(page)
    test_form_validation(page)
    test_testimonials_slider(page)
    test_scroll_reveal(page)

    print("\n=== ESTABILIDAD POST-INTERACCIONES ===")
    ov = page.evaluate("""() => {
        function isInsideFixedOrAbsolute(el) {
            const selfPos = getComputedStyle(el).position;
            if (selfPos === 'fixed' || selfPos === 'absolute') return true;
            let p = el.parentElement;
            while (p && p !== document.body) {
                const pos = getComputedStyle(p).position;
                if (pos === 'fixed' || pos === 'absolute') return true;
                p = p.parentElement;
            }
            return false;
        }
        const all = document.querySelectorAll('body *');
        const vw = window.innerWidth;
        for (const el of all) {
            const r = el.getBoundingClientRect();
            if (r.right > vw + 10 && r.width > 10 && !isInsideFixedOrAbsolute(el)) {
                return false;
            }
        }
        return true;
    }""")
    ok("Sin overflow tras todas las interacciones") if ov else fail(
        "Overflow detectado tras interacciones"
    )
    ok("Sin errores de consola acumulados") if len(CONSOLE_ERRS) == 0 else fail(
        f"{len(CONSOLE_ERRS)} error(es) en consola durante la sesión"
    )

    test_viewport("mobile", VIEWPORTS["mobile"], page)
    test_viewport("tablet", VIEWPORTS["tablet"], page)
    test_viewport("desktop", VIEWPORTS["desktop"], page)

    test_visual(page)

    total = PASS + FAIL
    browser.close()

    return total, FAIL, CONSOLE_ERRS


def main():
    all_results = []

    print(f"\n{'=' * 54}")
    print(f"    Tiny Hearts Landing Page - Tester Agent")
    print(f"{'=' * 54}")

    # -- Servidor --
    print(f"\n  Iniciando servidor en http://localhost:{PORT} ...")
    server = ServerThread(PORT)
    server.start()
    time.sleep(1)

    try:
        with sync_playwright() as pw:
            for browser_name in BROWSERS:
                total, fails, errs = run_tests_in_browser(pw, browser_name)
                all_results.append((browser_name, total, fails, errs))

    finally:
        print(f"\n  Deteniendo servidor...")
        server.stop()

    # -- Resultado global --
    print(f"\n{'=' * 54}")
    overall_fail = 0
    for name, total, fails, errs in all_results:
        status = "PASSED" if fails == 0 else f"FAILED ({fails}/{total})"
        print(f"  {name.upper():10s} → {status}")
        if fails > 0:
            overall_fail += fails
            if errs:
                for e in errs[:8]:
                    print(f"    - {e}")
    print(f"{'=' * 54}\n")

    return 1 if overall_fail > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
