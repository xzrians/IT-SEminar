/**
 * NextGen Celik Digital 2026 - Master Interactive Logic
 * Optimized for Jekyll Static Site Architecture & GitHub Pages.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Lucide Icons
  if (window.lucide) {
    window.lucide.createIcons();
  }

  // 2. Restore checklist state from localStorage
  initChecklist();

  // 3. Initialize Mobile App Shell Hubs
  initAppShellHubs();

  // 4. Initialize PWA Service Worker & Network Monitor
  initPwaServiceWorker();

  // 5. Setup mobile navigation listener
  const mobileBtn = document.getElementById('mobileMenuBtn');
  const navMenu = document.getElementById('navMenu');
  if (mobileBtn && navMenu) {
    mobileBtn.addEventListener('click', () => {
      toggleNav();
    });

    // Auto-close menu when clicking any nav link
    navMenu.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('show');
      });
    });
  }
});

/**
 * Mobile Navigation Menu Toggle
 */
function toggleNav() {
  const navMenu = document.getElementById('navMenu');
  if (navMenu) {
    navMenu.classList.toggle('show');
  }
}

/**
 * Budget Variant Tab Switcher
 * Statically rendered by Jekyll; toggles active visibility instantaneously.
 */
function switchBudgetVariant(variantId) {
  // Update Tab Header Styles
  const tabs = document.querySelectorAll('.variant-tab');
  tabs.forEach(tab => tab.classList.remove('active'));

  const activeTab = document.getElementById(`budget-tab-${variantId}`);
  if (activeTab) {
    activeTab.classList.add('active');
  }

  // Update Display Panes
  const panes = document.querySelectorAll('.budget-pane');
  panes.forEach(pane => pane.classList.remove('active'));

  const activePane = document.getElementById(`budget-pane-${variantId}`);
  if (activePane) {
    activePane.classList.add('active');
  }

  // Refresh icons if needed
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

/**
 * Quiz Flashcard Answer Reveal Toggle
 */
function toggleQuiz(no) {
  const card = document.getElementById(`quiz-${no}`);
  if (card) {
    card.classList.toggle('revealed');
  }
}

/**
 * Interactive Checklist Persistence with LocalStorage
 */
function initChecklist() {
  const checkboxes = document.querySelectorAll('.check-item input[type="checkbox"]');
  checkboxes.forEach(chk => {
    const id = chk.id.replace('chk-', '');
    const isChecked = localStorage.getItem(`asdaf_task_${id}`);
    if (isChecked === 'true') {
      chk.checked = true;
    }
  });
}

function toggleTaskCheck(taskId) {
  const chk = document.getElementById(`chk-${taskId}`);
  if (!chk) return;

  if (chk.checked) {
    localStorage.setItem(`asdaf_task_${taskId}`, 'true');
  } else {
    localStorage.removeItem(`asdaf_task_${taskId}`);
  }
}

/**
 * Scroll Spy for Smooth Header Highlighting
 */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.pageYOffset + 140;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        currentId = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (currentId && link.getAttribute('href') === `#${currentId}`) {
        link.classList.add('active');
      }
    });
  });
}

/**
 * Operations Tab Switcher (Dokumen, Makanan, Goodies, Utiliti)
 */
function switchOpsTab(tabId) {
  // Update Buttons
  const tabs = document.querySelectorAll('.ops-tab');
  tabs.forEach(tab => tab.classList.remove('active'));

  const activeTab = document.getElementById(`ops-tab-btn-${tabId}`);
  if (activeTab) {
    activeTab.classList.add('active');
  }

  // Update Panes
  const panes = document.querySelectorAll('.ops-pane');
  panes.forEach(pane => pane.classList.remove('active'));

  const activePane = document.getElementById(`ops-pane-${tabId}`);
  if (activePane) {
    activePane.classList.add('active');
  }

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

/**
 * Curriculum Tab Switcher (Modul, Slaid, Aktiviti)
 */
function switchCurrTab(tabId) {
  // Update Buttons
  const buttons = document.querySelectorAll('#modul .ops-tab');
  buttons.forEach(btn => btn.classList.remove('active'));

  const activeBtn = document.getElementById(`curr-tab-btn-${tabId}`);
  if (activeBtn) {
    activeBtn.classList.add('active');
  }

  // Update Panes
  const panes = document.querySelectorAll('.curr-pane');
  panes.forEach(pane => {
    pane.style.display = 'none';
    pane.classList.remove('active');
  });

  const activePane = document.getElementById(`curr-pane-${tabId}`);
  if (activePane) {
    activePane.style.display = 'block';
    activePane.classList.add('active');
  }

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

/**
 * Jekyll Timeline: Category Filtering
 */
function filterTimeline(category) {
  const buttons = document.querySelectorAll('.timeline-filter-btn');
  buttons.forEach(btn => {
    if (btn.getAttribute('data-category') === category) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  const items = document.querySelectorAll('.timeline-event-item');
  items.forEach(item => {
    const itemCat = item.getAttribute('data-category');
    if (category === 'all' || itemCat === category) {
      item.classList.remove('hidden-slot');
    } else {
      item.classList.add('hidden-slot');
    }
  });

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

/**
 * Jekyll Timeline: Quick-Jump to Slot
 */
function jumpToTimelineSlot(slotId) {
  const target = document.getElementById(slotId);
  if (!target) return;

  // If item is currently hidden by category filter, reset filter to 'all'
  if (target.classList.contains('hidden-slot')) {
    filterTimeline('all');
  }

  // Smooth scroll with offset for sticky header
  const yOffset = -90;
  const y = target.getBoundingClientRect().top + window.pageYOffset + yOffset;
  window.scrollTo({ top: y, behavior: 'smooth' });

  // Add pulse glow highlight
  target.classList.remove('target-highlight');
  void target.offsetWidth;
  target.classList.add('target-highlight');
  setTimeout(() => {
    target.classList.remove('target-highlight');
  }, 2000);
}

/**
 * Mobile App Shell: Map URL Hash to Hub
 */
function getHubFromHash(hash) {
  if (!hash) return 'home';
  const clean = hash.replace('#', '').toLowerCase();
  if (['home', 'tab-home', 'hub-home', 'asdaf', 'stats'].includes(clean)) return 'home';
  if (['timeline', 'tab-timeline', 'hub-timeline', 'jadual', 'modul'].includes(clean)) return 'timeline';
  if (['people', 'tab-people', 'hub-people', 'meja', 'kru', 'kuiz'].includes(clean)) return 'people';
  if (['ops', 'tab-ops', 'hub-ops', 'bajet', 'operasi', 'checklist'].includes(clean)) return 'ops';
  return 'home';
}

/**
 * Mobile App Shell: Switch Active Hub (home, timeline, people, ops)
 */
function switchHub(hubId, shouldScroll = true) {
  const hubs = ['home', 'timeline', 'people', 'ops'];
  if (!hubs.includes(hubId)) hubId = 'home';

  // 1. Update Hub Panes
  document.querySelectorAll('.hub-pane').forEach(pane => {
    pane.classList.remove('active');
  });
  const targetPane = document.getElementById(`hub-${hubId}`);
  if (targetPane) {
    targetPane.classList.add('active');
  }

  // 2. Update Bottom Nav Buttons
  document.querySelectorAll('.bottom-nav-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  const activeBottomBtn = document.getElementById(`btn-nav-${hubId}`);
  if (activeBottomBtn) {
    activeBottomBtn.classList.add('active');
  }

  // 3. Update Desktop Nav Links
  document.querySelectorAll('#navMenu .nav-link').forEach(link => {
    link.classList.remove('active');
  });
  const activeDeskBtn = document.getElementById(`desk-nav-${hubId}`);
  if (activeDeskBtn) {
    activeDeskBtn.classList.add('active');
  }

  // 4. Smooth scroll to top on switch if requested
  if (shouldScroll) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // 5. Update browser history hash without reload
  if (history.replaceState) {
    history.replaceState(null, null, `#hub-${hubId}`);
  }

  // 6. Refresh Lucide Icons in newly visible pane
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

/**
 * Initialize App Shell Hubs & Hash Routing
 */
function initAppShellHubs() {
  const initialHash = window.location.hash;
  const initialHub = getHubFromHash(initialHash);
  switchHub(initialHub, false);

  // Listen to hash changes (back/forward button)
  window.addEventListener('hashchange', () => {
    const hub = getHubFromHash(window.location.hash);
    switchHub(hub, false);
  });
}

/**
 * Progressive Web App (PWA): Service Worker, Network Monitor & Cache-Busting Live Update Engine
 */
let deferredInstallPrompt = null;
let swRegistration = null;

function showUpdatePrompt(worker) {
  console.log('[PWA] New update detected! Showing update prompt...');
  
  // 1. Highlight navbar update button & show pulsing badge
  const updateBtn = document.getElementById('btnUpdatePrompt');
  const updateBadge = document.getElementById('updateBadgeDot');
  if (updateBtn) {
    updateBtn.classList.add('has-update');
  }
  if (updateBadge) {
    updateBadge.style.display = 'inline-block';
  }

  // 2. Display the floating update toast
  const toast = document.getElementById('pwaUpdateToast');
  if (toast) {
    toast.style.display = 'block';
  }

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

function dismissUpdateToast() {
  const toast = document.getElementById('pwaUpdateToast');
  if (toast) {
    toast.style.display = 'none';
  }
}

async function applyLatestUpdateAndClearCache() {
  const updateBtn = document.getElementById('btnUpdatePrompt');
  const toastBtn = document.getElementById('btnToastApplyUpdate');
  
  if (updateBtn) {
    updateBtn.classList.add('loading');
    updateBtn.innerHTML = '<i data-lucide="loader-2"></i> <span class="update-text">Memuat Kod...</span>';
  }
  if (toastBtn) {
    toastBtn.disabled = true;
    toastBtn.innerHTML = '<i data-lucide="loader-2"></i> <span>Mengemas Kini...</span>';
  }
  if (window.lucide) {
    window.lucide.createIcons();
  }

  try {
    // 1. Tell all waiting / active service workers to SKIP_WAITING
    if ('serviceWorker' in navigator) {
      const registrations = await navigator.serviceWorker.getRegistrations();
      for (const reg of registrations) {
        if (reg.waiting) {
          reg.waiting.postMessage({ type: 'SKIP_WAITING' });
        }
        if (reg.installing) {
          reg.installing.postMessage({ type: 'SKIP_WAITING' });
        }
        if (reg.active) {
          reg.active.postMessage({ type: 'SKIP_WAITING' });
        }
      }
    }

    // 2. Completely purge all CacheStorage caches so no stale CSS/HTML/JS is kept
    if ('caches' in window) {
      const cacheNames = await caches.keys();
      await Promise.all(cacheNames.map(name => caches.delete(name)));
      console.log('[PWA] Purged all CacheStorage:', cacheNames);
    }

    // 3. Clear any cached version flags in localStorage
    localStorage.removeItem('pwa_known_version');

    // 4. Force hard reload bypassing browser HTTP cache with timestamp query
    const targetUrl = new URL(window.location.href);
    targetUrl.searchParams.set('reload', Date.now().toString());
    window.location.href = targetUrl.toString();
  } catch (error) {
    console.error('[PWA] Error purging cache and updating:', error);
    window.location.reload();
  }
}

async function checkForRemoteUpdates() {
  if (!navigator.onLine) return;
  try {
    const res = await fetch(`./sw.js?nocache=${Date.now()}`, { cache: 'no-store' });
    if (!res.ok) return;
    const content = await res.text();
    const match = content.match(/CACHE_NAME\s*=\s*['"]([^'"]+)['"]/);
    if (match && match[1]) {
      const remoteVersion = match[1];
      const localVersion = localStorage.getItem('pwa_known_version');
      if (localVersion && localVersion !== remoteVersion) {
        console.log(`[PWA] Remote version detected: ${remoteVersion} (current local: ${localVersion})`);
        showUpdatePrompt();
      } else if (!localVersion) {
        localStorage.setItem('pwa_known_version', remoteVersion);
      }
    }
  } catch (e) {
    // Silently ignore network check errors
  }
}

function initPwaServiceWorker() {
  // 1. Register Service Worker with instant update checking
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('./sw.js')
        .then(registration => {
          swRegistration = registration;
          console.log('[PWA] Service Worker registered successfully, scope:', registration.scope);

          // If a worker is already waiting (e.g. from previous visit), prompt immediately
          if (registration.waiting) {
            showUpdatePrompt(registration.waiting);
          }

          // Listen for new worker installation
          registration.addEventListener('updatefound', () => {
            const installingWorker = registration.installing;
            if (installingWorker) {
              installingWorker.addEventListener('statechange', () => {
                if (installingWorker.state === 'installed') {
                  if (navigator.serviceWorker.controller) {
                    showUpdatePrompt(installingWorker);
                  }
                }
              });
            }
          });

          // Check for worker updates
          registration.update();

          // Poll for updates every 45 seconds while page is open
          setInterval(() => {
            registration.update();
            checkForRemoteUpdates();
          }, 45000);
        })
        .catch(error => {
          console.warn('[PWA] Service Worker registration failed:', error);
        });

      // Quick remote version check 3 seconds after page load
      setTimeout(checkForRemoteUpdates, 3000);
    });

    // Auto-reload once when a new service worker takes control
    let isRefreshing = false;
    navigator.serviceWorker.addEventListener('controllerchange', () => {
      if (!isRefreshing) {
        isRefreshing = true;
        console.log('[PWA] New Service Worker activated. Reloading page for latest content...');
        window.location.reload();
      }
    });
  }

  // 2. Monitor Online / Offline Network Status
  const statusPill = document.getElementById('networkStatusPill');
  const statusText = document.getElementById('networkStatusText');
  const offlineBanner = document.getElementById('offlineBanner');

  function updateNetworkStatus() {
    if (navigator.onLine) {
      if (statusPill) {
        statusPill.classList.remove('offline');
        statusPill.classList.add('online');
      }
      if (statusText) statusText.textContent = 'Online';
      if (offlineBanner) offlineBanner.style.display = 'none';
    } else {
      if (statusPill) {
        statusPill.classList.remove('online');
        statusPill.classList.add('offline');
      }
      if (statusText) statusText.textContent = 'Offline';
      if (offlineBanner) offlineBanner.style.display = 'block';
      if (window.lucide) window.lucide.createIcons();
    }
  }

  window.addEventListener('online', updateNetworkStatus);
  window.addEventListener('offline', updateNetworkStatus);
  updateNetworkStatus();

  // 3. Capture PWA Install Prompt
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredInstallPrompt = e;
    const installBtn = document.getElementById('btnInstallPwa');
    if (installBtn) {
      installBtn.style.display = 'inline-flex';
      if (window.lucide) window.lucide.createIcons();
    }
  });

  window.addEventListener('appinstalled', () => {
    deferredInstallPrompt = null;
    const installBtn = document.getElementById('btnInstallPwa');
    if (installBtn) installBtn.style.display = 'none';
    console.log('[PWA] NextGen 2026 application installed successfully.');
  });
}

function promptPwaInstall() {
  if (!deferredInstallPrompt) return;
  deferredInstallPrompt.prompt();
  deferredInstallPrompt.userChoice.then(choiceResult => {
    if (choiceResult.outcome === 'accepted') {
      console.log('[PWA] User accepted installation prompt');
    } else {
      console.log('[PWA] User dismissed installation prompt');
    }
    deferredInstallPrompt = null;
    const installBtn = document.getElementById('btnInstallPwa');
    if (installBtn) installBtn.style.display = 'none';
  });
}

function dismissOfflineBanner() {
  const offlineBanner = document.getElementById('offlineBanner');
  if (offlineBanner) {
    offlineBanner.style.display = 'none';
  }
}

// Attach functions to global window object
window.toggleNav = toggleNav;
window.switchBudgetVariant = switchBudgetVariant;
window.switchOpsTab = switchOpsTab;
window.switchCurrTab = switchCurrTab;
window.toggleQuiz = toggleQuiz;
window.toggleTaskCheck = toggleTaskCheck;
window.filterTimeline = filterTimeline;
window.jumpToTimelineSlot = jumpToTimelineSlot;
window.switchHub = switchHub;
window.promptPwaInstall = promptPwaInstall;
window.dismissOfflineBanner = dismissOfflineBanner;
window.applyLatestUpdateAndClearCache = applyLatestUpdateAndClearCache;
window.dismissUpdateToast = dismissUpdateToast;
window.showUpdatePrompt = showUpdatePrompt;

