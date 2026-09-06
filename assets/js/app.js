/**
 * NextGen Tech Summit 2026 - Master Interactive Logic
 * Optimized for Jekyll Static Site Architecture & GitHub Pages.
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Lucide Icons
  if (window.lucide) {
    window.lucide.createIcons();
  }

  // 2. Restore checklist state from localStorage
  initChecklist();

  // 3. Scroll Spy for active navigation highlighting
  initScrollSpy();

  // 4. Setup mobile navigation listener
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

// Attach functions to global window object
window.toggleNav = toggleNav;
window.switchBudgetVariant = switchBudgetVariant;
window.switchOpsTab = switchOpsTab;
window.toggleQuiz = toggleQuiz;
window.toggleTaskCheck = toggleTaskCheck;
