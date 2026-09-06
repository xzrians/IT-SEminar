/**
 * NextGen Celik Digital 2026 - Service Worker
 * Progressive Web App (PWA) Offline-First Engine
 * Strategy: App Shell Precaching + Stale-While-Revalidate Runtime Caching
 */

const CACHE_NAME = 'nextgen-pwa-v1.0.8';

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './slides/',
  './assets/css/styles.css',
  './assets/js/app.js',
  './manifest.webmanifest',
  './assets/icons/icon.svg'
];

// 1. Service Worker Installation: Precache App Shell
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => {
      return self.skipWaiting();
    })
  );
});

// 2. Service Worker Activation: Purge Outdated Caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((name) => {
          if (name !== CACHE_NAME) {
            console.log('[SW] Purging stale cache:', name);
            return caches.delete(name);
          }
        })
      );
    }).then(() => {
      return self.clients.claim();
    })
  );
});

// 3. Fetch Event: Network-First for Navigation (HTML) + Stale-While-Revalidate for Assets
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // Exclude non-http/https schemes (e.g. chrome-extension)
  if (!url.protocol.startsWith('http')) return;

  // A. Navigation requests (HTML documents): Network-First with Offline Cache Fallback
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseToCache);
            });
          }
          return networkResponse;
        })
        .catch(() => {
          // Offline fallback: serve cached index.html or root
          return caches.match('./index.html') || caches.match('./');
        })
    );
    return;
  }

  // B. Static Assets (CSS, JS, Icons, Images): Stale-While-Revalidate
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      }).catch(() => {
        // Offline handling for assets
      });

      return cachedResponse || fetchPromise;
    })
  );
});
