# Schema.org JSON‑LD Examples

Complete, validated examples for the entity types relevant to a local business
website. Copy, adapt, and embed each block inside the `<head>` of the corresponding
page. Replace all placeholder values (in UPPERCASE) with real data.

---

## LocalBusiness (or Organization)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "YOUR BUSINESS NAME",
  "image": "https://www.yoursite.com/images/logo.png",
  "logo": "https://www.yoursite.com/images/logo.png",
  "@id": "https://www.yoursite.com/#organization",
  "url": "https://www.yoursite.com",
  "telephone": "+1-555-123-4567",
  "email": "contact@yoursite.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main Street",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "Country"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/yourbusiness",
    "https://www.linkedin.com/company/yourbusiness",
    "https://www.instagram.com/yourbusiness",
    "https://www.wikidata.org/wiki/Q12345"
  ]
}
```

## Services (Offered Services)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "SERVICE NAME",
  "description": "Detailed description of the service provided.",
  "provider": {
    "@type": "LocalBusiness",
    "@id": "https://www.yoursite.com/#organization"
  },
  "areaServed": {
    "@type": "City",
    "name": "SERVICE CITY"
  },
  "offers": {
    "@type": "Offer",
    "price": "149.00",
    "priceCurrency": "USD"
  }
}
```

## FAQPage (Frequently Asked Questions)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the return policy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can return any item within 30 days of purchase for a full refund."
      }
    },
    {
      "@type": "Question",
      "name": "Do you offer installation services?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, our certified technicians can install the product at your location."
      }
    }
  ]
}