// TOC折りたたみ機能 v4 - MkDocs Material対応
(function() {
  'use strict';

  function init() {
    var sidebar = document.querySelector('.md-sidebar--secondary');
    if (!sidebar) return;

    var navList = sidebar.querySelector('.md-nav__list[data-md-component="toc"]');
    if (!navList) {
      navList = sidebar.querySelector('.md-nav__list');
    }
    if (!navList) return;

    // 既に初期化済みかチェック
    if (navList.getAttribute('data-toc-init') === 'true') return;
    navList.setAttribute('data-toc-init', 'true');

    // 直接の子要素を取得（h2レベル）
    var items = navList.querySelectorAll(':scope > .md-nav__item');

    items.forEach(function(item) {
      // MkDocs MaterialではネストがNav要素の中にある
      var nestedNav = item.querySelector(':scope > nav.md-nav');
      var link = item.querySelector(':scope > .md-nav__link');

      if (nestedNav && link) {
        // 折りたたみクラス追加
        item.classList.add('toc-collapsible');
        item.classList.add('toc-collapsed');

        // ネストNavにもクラス追加（CSS用）
        nestedNav.classList.add('toc-nested-nav');

        // トグルボタン作成
        var toggle = document.createElement('span');
        toggle.className = 'toc-toggle';
        toggle.textContent = '▶';

        // クリックイベント
        toggle.onclick = function(e) {
          e.preventDefault();
          e.stopPropagation();

          var isCollapsed = item.classList.contains('toc-collapsed');

          if (isCollapsed) {
            item.classList.remove('toc-collapsed');
            toggle.textContent = '▼';
          } else {
            item.classList.add('toc-collapsed');
            toggle.textContent = '▶';
          }

          return false;
        };

        // リンクの前に挿入
        link.insertBefore(toggle, link.firstChild);
      }
    });
  }

  // 複数タイミングで初期化を試行
  function tryInit() {
    setTimeout(init, 100);
    setTimeout(init, 500);
    setTimeout(init, 1000);
    setTimeout(init, 2000);
  }

  // DOM準備完了時
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryInit);
  } else {
    tryInit();
  }

  // ページ完全読み込み時
  window.addEventListener('load', tryInit);

  // MkDocs Material instant loading対応
  if (typeof window.document$ !== 'undefined' && window.document$) {
    window.document$.subscribe(function() {
      tryInit();
    });
  }
})();
