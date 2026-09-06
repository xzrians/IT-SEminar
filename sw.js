/**
 * NextGen Tech Summit 2026 - Service Worker
 * Progressive Web App (PWA) Offline-First Engine
 * Strategy: App Shell Precaching + Stale-While-Revalidate Runtime Caching
 */

const CACHE_NAME = 'nextgen-pwa-v1.0.1';

const PRECACHE_ASSETS = [
  './',
  './index.html',
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
            return caches.delete(name);
          }
        })
      );
    }).then(() => {
      return self.clients.claim();
    })
  );
});

// 3. Fetch Event: Stale-While-Revalidate Strategy
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // Exclude non-http/https schemes (e.g. chrome-extension)
  if (!url.protocol.startsWith('http')) return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      // Background revalidation
      const fetchPromise = fetch(event.request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      }).catch(() => {
        // Network failure (offline mode)
        // If it's a navigation request, return cached index.html
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html') || caches.match('./');
        }
      });

      // Return cached response immediately if available, otherwise wait for network
      return cachedResponse || fetchPromise;
    })
  );
});
