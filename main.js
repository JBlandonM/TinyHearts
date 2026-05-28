/**
 * Tiny Hearts Childcare Services - Landing Page JS
 * Main interactive behaviors, sliders, scroll reveals, and elegant validation
 */

/**
 * App configuration — centralized constants
 * Edit values here instead of hunting through functions.
 */
const CONFIG = {
  // --- EmailJS ---
  EMAILJS_PUBLIC_KEY: 'ocEUMfpfn5vd21Yiw',
  SERVICE_ID: 'service_1u09odc',
  TEMPLATE_NOTIFY: 'template_aufy52e',
  TEMPLATE_CONFIRM: 'template_47swull',

  // --- Slider (ms) ---
  SLIDER_INTERVAL: 8000,
  SLIDER_RESET_INTERVAL: 10000,

  // --- Scroll Reveal (IntersectionObserver) ---
  SCROLL_THRESHOLD: 0.1,
  SCROLL_ROOT_MARGIN: '0px 0px -80px 0px',

  // --- Header ---
  HEADER_SCROLL_OFFSET: 50,

  // --- Booking ---
  CR_TIMEZONE_OFFSET: '-06:00',
};

document.addEventListener('DOMContentLoaded', () => {
  initHeaderScroll();
  initMobileMenu();
  initScrollReveal();
  initTestimonialsSlider();
  initBookingForm();
  initBlobScrollPause();
});

/**
 * 1. HEADER SCROLL EFFECTS
 * Adjusts header styling (background blur, padding, shadow) as the user scrolls.
 */
function initHeaderScroll() {
  const header = document.getElementById('site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > CONFIG.HEADER_SCROLL_OFFSET) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  // Run on load in case page is refreshed scrolled down
  handleScroll();
  window.addEventListener('scroll', handleScroll, { passive: true });
}

/**
 * 2. MOBILE MENU & OVERLAY NAVIGATION
 * Handles drawer menu toggling with accessibility ARIA attribute management.
 */
function initMobileMenu() {
  const toggleBtn = document.getElementById('menu-toggle');
  const overlay = document.getElementById('mobile-overlay');

  if (!toggleBtn || !overlay) return;

  const toggleMenu = () => {
    const isExpanded = toggleBtn.getAttribute('aria-expanded') === 'true';

    // Toggle state
    toggleBtn.classList.toggle('active');
    overlay.classList.toggle('active');

    // Accessibility
    toggleBtn.setAttribute('aria-expanded', !isExpanded);
    overlay.setAttribute('aria-hidden', isExpanded);

    // Prevent body scroll when menu is active (with position save/restore)
    if (!isExpanded) {
      const scrollY = window.scrollY;
      document.body.dataset.scrollY = scrollY;
      document.body.style.top = `-${scrollY}px`;
      document.body.classList.add('no-scroll');
    } else {
      document.body.classList.remove('no-scroll');
      document.body.style.top = '';
      const savedScrollY = parseFloat(document.body.dataset.scrollY || '0');
      window.scrollTo(0, savedScrollY);
    }
  };

  toggleBtn.addEventListener('click', toggleMenu);

  // Close menu when clicking on any mobile nav links
  const mobileLinks = overlay.querySelectorAll('.nav-mobile-link, .btn');
  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (overlay.classList.contains('active')) {
        toggleMenu();
      }
    });
  });
}

/**
 * 3. SCROLL REVEAL ANIMATION (INTERSECTION OBSERVER)
 * Smoothly fades and slides in elements as they scroll into the viewport.
 */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.scroll-reveal');

  if (!revealElements.length) return;

  const observerOptions = {
    root: null,
    rootMargin: CONFIG.SCROLL_ROOT_MARGIN,
    threshold: CONFIG.SCROLL_THRESHOLD,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Stop observing once visible to maintain performance
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  revealElements.forEach(el => observer.observe(el));
}

/**
 * 3b. BLOB ANIMATION PAUSE ON SCROLL
 * Pauses heavy blur/transform animations while scrolling to reduce GPU load.
 */
function initBlobScrollPause() {
  const blobs = document.querySelectorAll('.blob');
  if (!blobs.length) return;

  let scrollTimeout;
  window.addEventListener('scroll', () => {
    blobs.forEach(b => b.classList.add('paused'));
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
      blobs.forEach(b => b.classList.remove('paused'));
    }, 150);
  }, { passive: true });
}

/**
 * 4. TESTIMONIALS SLIDER
 * Elegant, responsive slide mechanism with dot indicator binding and swipe simulation.
 */
function initTestimonialsSlider() {
  const slider = document.getElementById('testimonials-slider');
  const prevBtn = document.getElementById('slider-prev');
  const nextBtn = document.getElementById('slider-next');
  const dotsContainer = document.getElementById('slider-dots');

  if (!slider || !prevBtn || !nextBtn) return;

  const slides = slider.querySelectorAll('.testimonial-slide');
  const totalSlides = slides.length;
  let currentIndex = 0;

  const updateSlider = () => {
    // Perform GPU accelerated slide transform
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;

    // Update dots active status
    const dots = dotsContainer.querySelectorAll('.slider-dot');
    dots.forEach((dot, index) => {
      if (index === currentIndex) {
        dot.classList.add('active');
        dot.setAttribute('aria-selected', 'true');
      } else {
        dot.classList.remove('active');
        dot.setAttribute('aria-selected', 'false');
      }
    });
  };

  const nextSlide = () => {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlider();
  };

  const prevSlide = () => {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateSlider();
  };

  // Button Listeners
  nextBtn.addEventListener('click', nextSlide);
  prevBtn.addEventListener('click', prevSlide);

  // Dot Click binding
  const dots = dotsContainer.querySelectorAll('.slider-dot');
  dots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      currentIndex = parseInt(e.target.getAttribute('data-index'));
      updateSlider();
    });
  });

  // Keyboard navigation for accessibility
  dotsContainer.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
      nextSlide();
    } else if (e.key === 'ArrowLeft') {
      prevSlide();
    }
  });

  let autoSlideTimer = setInterval(nextSlide, CONFIG.SLIDER_INTERVAL);

  const resetTimer = () => {
    clearInterval(autoSlideTimer);
    autoSlideTimer = setInterval(nextSlide, CONFIG.SLIDER_RESET_INTERVAL);
  };

  [prevBtn, nextBtn, dotsContainer].forEach(element => {
    element.addEventListener('click', resetTimer);
  });
}

/**
 * 5. BOOKING FORM VALIDATION & SUBMISSION
 * Highly interactive client-side form validator with immediate user feedback.
 */
function initBookingForm() {
  const form = document.getElementById('booking-form');
  const feedback = document.getElementById('form-feedback');

  if (!form || !feedback) return;

  // Set minimum date using Costa Rica timezone (UTC-6)
  const dateInput = document.getElementById('preferred-date');
  if (dateInput) {
    const crNow = new Date();
    const crOffset = -360; // UTC-6 in minutes
    const localOffset = crNow.getTimezoneOffset();
    const crTime = new Date(crNow.getTime() + (crOffset + localOffset) * 60000);
    const today = crTime.toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Clear previous states
    feedback.style.display = 'none';
    feedback.className = 'form-message';

    // Elements to validate
    const parentName = document.getElementById('parent-name');
    const childDetails = document.getElementById('child-details');
    const email = document.getElementById('email');
    const phone = document.getElementById('phone');
    const lodging = document.getElementById('lodging');
    const preferredDate = document.getElementById('preferred-date');
    const privacy = document.getElementById('privacy-policy');

    let errors = [];

    // Simple custom validations
    if (!parentName.value.trim()) {
      errors.push('Please enter your full name.');
      highlightError(parentName);
    } else {
      clearHighlight(parentName);
    }

    if (!childDetails.value.trim()) {
      errors.push('Please enter child details (number of children & ages).');
      highlightError(childDetails);
    } else {
      clearHighlight(childDetails);
    }

    if (!email.value.trim() || !validateEmail(email.value)) {
      errors.push('Please enter a valid email address.');
      highlightError(email);
    } else {
      clearHighlight(email);
    }

    if (!phone.value.trim()) {
      errors.push('Please enter your phone number.');
      highlightError(phone);
    } else {
      clearHighlight(phone);
    }

    if (!lodging.value.trim()) {
      errors.push('Please enter your staying location in Costa Rica.');
      highlightError(lodging);
    } else {
      clearHighlight(lodging);
    }

    if (!preferredDate.value) {
      errors.push('Please select a date.');
      highlightError(preferredDate);
    } else {
      clearHighlight(preferredDate);
    }

    if (!privacy.checked) {
      errors.push('You must agree to the privacy policy.');
      highlightError(privacy.parentElement);
    } else {
      clearHighlight(privacy.parentElement);
    }

    // Display validation status
    if (errors.length > 0) {
      showFeedback(errors[0], 'error');
      return;
    }

    // Honeypot check — reject if bot filled the hidden field
    const honeypot = document.getElementById('website');
    if (honeypot && honeypot.value.trim() !== '') {
      showFeedback('Your request could not be processed. Please try again.', 'error');
      return;
    }

    emailjs.init(CONFIG.EMAILJS_PUBLIC_KEY);

    const message = document.getElementById('message');
    const templateParams = {
      name: parentName.value.trim(),
      child_details: childDetails.value.trim(),
      email: email.value.trim(),
      phone: phone.value.trim(),
      lodging: lodging.value.trim(),
      preferred_date: preferredDate.value,
      message: message ? message.value.trim() : '',
    };

    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending request...';
    submitBtn.disabled = true;

    const notifyBusiness = emailjs.send(CONFIG.SERVICE_ID, CONFIG.TEMPLATE_NOTIFY, templateParams);
    const confirmClient = emailjs.send(CONFIG.SERVICE_ID, CONFIG.TEMPLATE_CONFIRM, templateParams);

    Promise.all([notifyBusiness, confirmClient])
      .then(() => {
        showFeedback('Thank you! Your booking inquiry has been sent successfully. We will get back to you within 24 hours to arrange the perfect care for your little ones.', 'success');
        form.reset();
      })
      .catch(() => {
        showFeedback('There was an error sending your request. Please try again or email us directly.', 'error');
      })
      .finally(() => {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
        feedback.scrollIntoView({ behavior: 'smooth', block: 'center' });
      });
  });

  // Helpers
  function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }

  function highlightError(element) {
    element.style.borderColor = 'var(--color-coral)';
    element.style.boxShadow = '0 0 0 4px rgba(229, 106, 84, 0.1)';
  }

  function clearHighlight(element) {
    element.style.borderColor = '';
    element.style.boxShadow = '';
  }

  function showFeedback(message, type) {
    feedback.textContent = message;
    feedback.classList.add(type);
    feedback.style.display = 'block';
  }
}
